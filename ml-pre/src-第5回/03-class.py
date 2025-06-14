# -*- coding: utf-8 -*-
"""資料作成#5-3-スライド用03-クラス化.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14oAGus7C7PleIFTMhwXNG89LQpaCmlTW
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

""" digitsデータ読み込み """
digits = load_digits()
X_orig, Y_orig = digits.data, digits.target
X_train, X_test, Y_train, Y_test= train_test_split(
    X_orig, Y_orig, test_size=0.2, random_state=19)

# data取得状態確認用
def print_data():
    # データサイズ確認
    print(f'All: X:{X_orig.shape}, Y:{Y_orig.shape}, type:{type(X_orig)}, {type(Y_orig)}')
    print(f'Train: X_train:{X_train.shape}, Y_train:{Y_train.shape}')
    print(f'Test: X_test:{X_test.shape}, Y_test:{Y_test.shape}')

    # 念のため画像確認
    print(X_orig[0].shape)
    print(Y_orig[0])
    plt.figure(figsize=(2, 2))
    plt.imshow(X_orig[0].reshape(8, 8), cmap='gray')
    plt.show()

print_data()

""" 部品 """
# step function - np配列に対応
def step_function(x):
    y = x > 0
    return y.astype(int)

# sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# relu
def relu(x):
    return np.maximum(0, x)

# sotmax - 複数データセットに対応
def softmax(x):
    x = x if x.ndim >= 2 else x.reshape(1, x.size)
    M = np.max(x, axis=1, keepdims=True) # M: 各行ごとの最大値
    exp_x = np.exp(x - M)
    S = np.sum(exp_x, axis=1, keepdims=True) # 各行ごとの合計
    return exp_x / S

def one_hot_batch(k_list, num_classes=10):
    """ n個のリストから(n,10)サイズのワンホットベクトルリストを作る """
    return np.eye(num_classes)[k_list]

def loss_mse(Y_pred, Y):
    """ 平均二乗誤差 """
    Y_vec = one_hot_batch(Y) # 正解をワンホットベクトル化
    rss = np.sum((Y_pred - Y_vec)**2, axis=1) # 列方向に平方和
    return np.mean(rss)

def cross_entropy(Y_pred, Y):
    """ クロスエントロピー誤差（改訂版） """
    d = 1e-8 # 1e-8, 1e-3
    if Y_pred.ndim == 1:
        Y = Y.reshape(1, Y.size)
        Y_pred = Y_pred.reshape(1, Y_pred.size)

    batch_size = Y.shape[0]
    correct_probs = Y_pred[np.arange(batch_size), Y]  # ←ここでバッチ全体をまとめて取り出す
    log_likelihood = -np.log(correct_probs + d)
    loss = np.mean(log_likelihood)
    return loss

def loss_cross_entropy(Y_pred, Y):
    """ 損失関数（cross_entropy） """
    loss = cross_entropy(Y_pred, Y) # 評価値算出（合算、割り算済み）
    return loss

def accuracy(Y_pred, Y):
    """ 正解率（Python的実装） """
    return np.mean(np.argmax(Y_pred, axis=1) == Y)

class MyActivationLayer():
    """ 活性化関数だけ適用する層（実験用） """
    def __init__(self, activation=softmax):
        self.activation = activation

    def __call__(self, X):
        return self.activation(X)

""" 微分関数。名前だけ確保。あとで実装 """
def step_function_prime(x): # placeholder
    return
def sigmoid_prime(x): # placeholder
    return
def relu_prime(x): # placeholder
    return
def softmax_prime(x): # placeholder
    return
def loss_mse_prime(x): # placeholder
    return
def loss_cross_entropy_prime(x): # placeholder
    return

# 活性化関数/損失関数の名前から関数と導関数を紐付ける辞書
funcs_map = {
    'step': (step_function, step_function_prime),
    'relu': (relu, relu_prime),
    'softmax': (softmax, softmax_prime),
    'mse': (loss_mse, loss_mse_prime),
    'cross_entropy': (loss_cross_entropy, loss_cross_entropy_prime),
    # 別名定義（入力を容易に）
    'ReLU': (relu, relu_prime),
    'MSE': (loss_mse, loss_mse_prime),
    'Entropy': (loss_cross_entropy, loss_cross_entropy_prime),
}

class MyLinearLayer():
    """ 線形層 """
    def __init__(self, input_size, output_size, bias=True, activation='relu'):
        self.activation, self.activation_prime = funcs_map[activation]
        self.W = np.random.randn(input_size, output_size)
        self.b = np.array([np.zeros(output_size)])

    @property
    def shape(self):
        return self.W.shape # デバッグ用

    def forward(self, X):
        """ 順伝播 """
        #self.X = X # 入力を保存 (N, input_size)
        self.Z = X @ self.W + self.b # 線形出力 (N, output_size)
        self.A = self.activation(self.Z) # 活性化出力 (N, output_size)
        return self.A

    __call__ = predict = forward

    def grad(self, X, Y, loss_fn, param, h=1e-5):
        """ 数値微分 """
        grad = np.zeros_like(param)
        iter = np.nditer(param, flags=['multi_index'])
        while not iter.finished:
            idx = iter.multi_index
            original = param[idx].copy()

            param[idx] = original + h
            L1 = loss_fn()
            param[idx] = original - h
            L2 = loss_fn()
            grad[idx] = (L1 - L2) / (2 * h)

            param[idx] = original
            iter.iternext()
        return grad

    def train_numeric(self, X, Y, loss_fn, lr=1e-3):
        """ 数値微分でパラメータ更新 """
        dW = self.grad(X, Y, loss_fn, self.W)
        db = self.grad(X, Y, loss_fn, self.b)
        self.W -= lr * dW
        self.b -= lr * db


class MyNetwork():
    def __init__(self, loss_name='cross_entropy', activation='relu'):
        self.loss_fn, self.loss_prime = funcs_map[loss_name]
        self.layers = [
            MyLinearLayer(input_size, hidden_size, activation=activation),
            MyLinearLayer(hidden_size, output_size, activation='softmax'),
        ]

    def forward(self, X):
        """ 順伝播 """
        for layer in self.layers:
            X = layer.forward(X)
        return X

    __call__ = predict = forward # 全部同じ処理

    def loss(self, X, Y, L2=0):
        Y_pred = self.forward(X)
        loss_value = self.loss_fn(Y_pred, Y)
        return loss_value

    def train_numeric(self, X, Y, lr=1e-2):
        """ 数値微分でパラメータ更新 """
        L = lambda: self.loss(X, Y) # layer.train内で実行する
        for layer in self.layers:
            layer.train_numeric(X, Y, L, lr)
        return

""" トレーニング """
def train_minibatch(X, Y):
    global lr # スコープ対策
    print_metrics(X_test, Y_test) # 初期状態表示

    # エポック毎にループ
    for i in range(max_epoch):
        print(f'epoch: {i+1} -> ', end='')
        # 1エポック内で訓練データをシャッフル
        num = X.shape[0] # データ個数取得
        indices = np.arange(num) # データ個数分の順列を取得
        np.random.shuffle(indices) # シャッフル

        # バッチサイズごとにループ
        for j in range(0, num, batch_size):
            # バッチセットを取得
            batch_indices = indices[j:min(j + batch_size, num)]
            X_batch = X[batch_indices]
            Y_batch = Y[batch_indices]
            # パラメータ更新
            model.train_numeric(X_batch, Y_batch, lr)

        print_metrics(X_test, Y_test) # エポック毎に検証

    return loss_list, acc_list

""" 状況表示 """
def print_metrics(x, y):
    # 現在値を取得
    loss = model.loss(x, y)
    acc = accuracy(model.forward(x), y)
    now = time.perf_counter()
    # グラフ表示用に値を保存
    loss_list.append(loss)
    acc_list.append(acc)
    time_list.append(now - start)
    # 現在値表示
    print(f'Loss: {loss:.10f}, Accuracy: {acc:.5f}, ' \
          f'Time: {(now-start)/60:.5f}[min]')
    return loss, acc, now

def graph(loss, acc, times, y_range=[0,2], y_step=0.2, title="loss, accuracy"):
    plt.rcParams["font.size"] = 14
    fig, ax1 = plt.subplots(figsize=(8.0, 6.0))
    step = len(loss)
    idx_mid, idx_max = int(step/2), step - 1
    t = np.linspace(0, idx_max, step)  # start, end, step

    # loss軸設定
    ax1.set_title(title, fontsize=13)
    ax1.set_xlabel('epoch')
    ax1.set_xlim([-5, idx_max+5]) # -1
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True, axis='x')

    # loss plot
    ax1.plot(t, loss, color="blue", label="Loss")
    ax1.plot(0, loss[0], color="blue",marker = 'x', markersize = 15)
    ax1.plot(idx_mid, loss[idx_mid], color="blue",marker = 'x', markersize = 15)
    ax1.plot(idx_max, loss[idx_max], color="blue",marker = 'x', markersize = 15)

    # accuracy軸設定
    ax2 = ax1.twinx()
    ax2.set_ylabel('accuracy', color='red')
    ax2.set_ylim([0, 1])
    ax2.set_yticks(np.arange(0, 1, 0.1))
    ax2.tick_params(axis='y', right=True, labelright=True)
    ax2.grid(True)

    # accuracy plot
    ax2.plot(t, acc, color="red", label="Accuracy")
    ax2.plot(0, acc[0], color="red",marker = 'x', markersize = 15)
    ax2.plot(idx_mid, acc[idx_mid], color="red",marker = 'x', markersize = 15)
    ax2.plot(idx_max, acc[idx_max], color="red",marker = 'x', markersize = 15)
    ax2.tick_params(axis='y', labelcolor='red')

    # loss text
    ymin, ymax = ax1.get_ylim()
    d = ymax - ymin
    h = 0.06
    y = (loss[0] - ymin) / d + h
    ax2.text(0.01, 0.997, f'{(loss[0]):.5f}', color='blue', \
             va='top', ha='left', transform=ax1.transAxes, fontsize=15)
    y = (loss[idx_mid] - ymin) / d + h
    ax2.text(0.5, y, f'{(loss[idx_mid]):.5f}', color='blue', \
             va='center', ha='center', transform=ax1.transAxes, fontsize=15)
    y = (loss[-1] - ymin) / d + h
    ax2.text(0.99, y, f'{(loss[-1]):.5f}', color='blue', \
             va='center', ha='right', transform=ax1.transAxes, fontsize=15)

    # time text
    ax2.text(0.01, 0.015, f'{(times[0])/60:.5f}min', \
             va='center', ha='left', transform=ax1.transAxes)
    ax2.text(0.5, 0.015, f'{(times[idx_mid])/60:.5f}min', \
             va='center', ha='center', transform=ax1.transAxes)
    ax2.text(0.99, 0.015, f'{(times[-1])/60:.5f}min', \
             va='center', ha='right', transform=ax1.transAxes)

    # accuracy text
    y = acc[0] - h * np.sign(acc[0] - 0.3)
    ax2.text(0.01, y, f'{(acc[0]):.5f}', color='red', \
             va='center', ha='left', transform=ax1.transAxes, fontsize=15)
    y = acc[idx_mid] - h * np.sign(acc[idx_mid] - 0.3)
    ax2.text(0.5, y, f'{(acc[idx_mid]):.5f}', color='red', \
             va='center', ha='center', transform=ax1.transAxes, fontsize=15)
    y = acc[-1] - h * np.sign(acc[idx_mid] - 0.3)
    ax2.text(0.99, y, f'{(acc[-1]):.5f}', color='red', \
             va='center', ha='right', transform=ax1.transAxes, fontsize=15)

    # 凡例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    y = acc[-1] - 0.1 if acc[-1] > 0.5 else 0.9
    ax2.legend(lines2 + lines1, labels2 + labels1, \
               loc='upper right', bbox_to_anchor=(1, y))

    fig.tight_layout()
    plt.show()
    return plt

def title_text():
    title = f'{activation},{loss_name},lr:{lr:.4f}'
    title += f'{"/" + str(lr_decay) if lr_decay != 1 else ""},'
    title += f'batch:{batch_size if batch_size != X_train.shape[0] else "Full"},'
    title += f'nodes:' + str(model.layers[0].shape[0])
    for i in range(len(model.layers)):
        title += '-' + str(model.layers[i].shape[1])
    title += '(' \
            f'{"L2," if L2!=0 else ""}' \
            f'{"HE," if he else ""}' \
            f'{"backward" if backward else "numeric"}' \
            ')'
    return title

""" 実験室 """
# ハイパーパラメータ
np.random.seed(19) # 乱数初期化
input_size = 8*8
hidden_size = 64 # 27
output_size = 10
max_epoch = 400
batch_size = 50 # ミニバッチ
lr = 1e-1
#lr = 1e-2
#lr = 1

# あとで実装
backward = False
lr_decay = 1
decay_step = 10
L2=0
he = False

# 利用関数を指定
activation = 'step' # step, ReLU
loss_name = 'MSE' # MSE, Entropy

# 実行準備
model = MyNetwork(loss_name=loss_name,activation=activation)
loss_list, acc_list, time_list = [], [], []
title = title_text()
print(title)

# 開始
start = time.perf_counter()
train_minibatch(X_train, Y_train)
print(title_text())
graph(loss_list, acc_list, time_list, title=title)

graph(loss_list, acc_list, time_list, [0,15], 1.5,title)
print(loss_list[0], acc_list[0], len(loss_list), acc_list[len(acc_list)-1])