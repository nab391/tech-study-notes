---
marp: true
title: "Markdown記法サンプル"
theme: default
size: 16:9
style: |
  .flex { display: flex; gap: 2em; }
---

# Markdown記法サンプル
作成日：2025-07-31  
作成者：デモ用

---

## 📔Front Matter（YAML）の記述

<div class="flex">
<div class="_">

**📝冒頭のYAMLに下記を追記します**

```yaml
style: |
  .flex { display: flex; gap: 2em; }
```

markdown内に下記コードを記述します

```html
<div class="flex">
<div class="_">
⬅ 左側ブロック
</div>
<div class="_">
右側ブロック ➡
</div>
</div>
```
</div>
<div class="_">

**💻表示サンプル**

<div class="flex">
<div class="_">
⬅ 左側ブロック
</div>
<div class="_">
右側ブロック ➡
</div>
</div>
<br>

**💡コメント**
- スライドを分割できます
- 左右分割は説明の為の導入です
- 理解・実用は後回しでOKです

</div>
</div>

---

## 📔見出し

<div class="flex">
<div class="_">

**📝markdown書式**

`# 見出し`で見出しになります。  
`#`の数が見出しレベル（階層）です

```markdown
# 見出し：レベル1
## 見出し：レベル2
### 見出し：レベル3
#### 見出し：レベル4
```
</div>
<div class="_">

**💻表示サンプル**


# 見出し：レベル1
## 見出し：レベル2
### 見出し：レベル3
#### 見出し：レベル4
</div>
</div>

---

## 📔強調・装飾・絵文字
<div class="flex">
<div class="_">

**📝markdown書式**

文字を特定の記号で囲うことで  
強調や装飾ができます。  
絵文字は普通に使えます

```text
- **太字**
- *斜体*
- **太字と *斜体* の組み合わせ**
- ~~打ち消し~~
- 絵文字: 😄 🎉 ⚡
```
</div>
<div class="_">

**💻表示サンプル**

- **太字**
- *斜体*
- **太字と *斜体* の組み合わせ**
- ~~打ち消し~~
- 絵文字: 😄 🎉 ⚡
</div>
</div>

---

## 📔段落
<div class="flex">
<div class="_">

**📝markdown書式**

テキスト中に空行があると段落分けになります。

```text
1行目：2行目との間に空行を入れない
2行目：1行目と同じ段落扱い

↑3行目は空行、4行目は1〜2行めと別段落
```

</div>
<div class="_">

**💻表示サンプル**

1行目：2行目との間に空行を入れない
2行目：1行目と同じ段落扱い

↑3行目は空行、4行目は1〜2行目と別段落

</div>
</div>

---

## 📔箇条書き
<div class="flex">
<div class="_">

**📝markdown書式**

`- リスト項目`で箇条書きになります。  
`-`の前に空白を入れると入れ子になります

```markdown
- リスト項目1
- リスト項目2
  - ネスト項目A
  - ネスト項目B
```
</div>
<div class="_">

**💻表示サンプル**

- リスト項目1
- リスト項目2
  - ネスト項目A
  - ネスト項目B
</div>
</div>

---

## 📔引用
<div class="flex">
<div class="_">

**📝markdown書式**
```text
> これは引用文です。
> 複数行の引用も可能です。
```
</div>
<div class="_">

**💻表示サンプル**
> これは引用文です。
> 複数行の引用も可能です。
</div>
</div>

---

## 📔コードブロック

<div class="flex">
<div class="_">

**📝markdown書式**
文章中にプログラムコードを記述する場合は `` ` ``で  
囲みます。`` `Hello` ``は`Hello`と表示されます

ブロック全体をコード表示する場合は`` ` ``3つで  
囲みます。後ろに言語を付けると色がつきます

````text
```python
# Pythonコード
def greet(name):
    print(f"Hello, {name}!")

greet("Pikachu")
```
````
</div>
<div class="_">

**💻表示サンプル**
```python
# Pythonコード
def greet(name):
    print(f"Hello, {name}!")

greet("Pikachu")
```
</div>
</div>

---

## 📔テーブル（表）

<div class="flex">
<div class="_">

**📝markdown書式**

markdownで表を作る場合は`|`を使います。
詳しくは下記参照。  
（結構めんどくさいです）

```text

| 名前    | 種類    | 攻撃技     |
| ----- | ----- | ------- |
| ピカチュウ | でんき   | 10まんボルト |
| フシギダネ | くさ／どく | つるのムチ   |
| ヒトカゲ  | ほのお   | かえんほうしゃ |
```
</div>
<div class="_">

**💻表示サンプル**

| 名前    | 種類    | 攻撃技     |
| ----- | ----- | ------- |
| ピカチュウ | でんき   | 10まんボルト |
| フシギダネ | くさ／どく | つるのムチ   |
| ヒトカゲ  | ほのお   | かえんほうしゃ |
</div>
</div>

---

## 📔リンク

<div class="flex">
<div class="_">

**📝markdown書式**

Markdown(HTML)でのリンクとは、  
「クリックすると別の情報（ページやファイル）を開く  
“導線”」です。

書式は`[タイトル](URL)`となります  
URLはPDFなどのファイルでもOKです

```text
[ゼルダの伝説](https://www.nintendo.com/jp/character/zelda/)
```
</div>
<div class="_">

**💻表示サンプル**

[ゼルダの伝説](https://www.nintendo.com/jp/character/zelda/)
</div>
</div>

---

## 📔画像

<div class="flex">
<div class="_">

**📝markdown書式**

スライド内に画像を表示する場合は  
`![タイトル](画像URL)`を使います。  
リンクとの違いは先頭の`!`の有無です

画像URLは外部のWEBサイトでも、  
ローカルの相対ファイルパスでもOKです


```text
![GitHub](https://github.githubassets.com/assets/inbox-zero-86555dddc82e.svg)
```
</div>
<div class="_">

**💻表示サンプル**

![GitHub](https://github.githubassets.com/assets/inbox-zero-86555dddc82e.svg)

**💡応用**(画像がリンクになってます)

[![GitHub](img/github-mark.png)](https://github.com/)

</div>
</div>

---

## 📔HTML直接記述

<div class="flex">
<div class="_">

**📝markdown書式**

markdownでは直接HTMLを記述することも  
できます

元々markdownはHTMLをシンプルに記述する  
為の省略記法で、ベースはHTMLそのもの  
です。よってHTMLはそのまま記述できます  
（HTMLについては後述します）

```text
<p><b>HTMLで</b><u>装飾</u>や
<strike>スタイル</strike>を指定</p>
```
</div>
<div class="_">

**💻表示サンプル**

<p><b>HTMLで</b><u>装飾</u>や
<strike>スタイル</strike>を指定</p>
</div>
</div>

---

## 📔数式

<div class="flex">
<div class="_">

**📝markdown書式**

数式はインライン表記とブロック表記の  
2種があります。インライン表記は文章中で  
数式部分を`$`で囲みます。

インライン：`$E = mc^2$`

ブロック表記は数式全体を`$$`で囲みます。

```latex
$$
\mathrm{i}\hbar \frac{\partial \psi}{\partial t}
= \hat{H}\psi(\bf{r},t)
$$
```
</div>
<div class="_">

**💻表示サンプル**

インライン：$E = mc^2$

$$
\mathrm{i}\hbar \frac{\partial \psi}{\partial t}
= \hat{H}\psi(\bf{r},t)
$$

**💡数式自体の書式 → $\LaTeX$**

数式部分は`LaTeX`という記法  
を使います。これはmarkdown  
とは別の規格であり、HTML以前  
から存在する数式特化の記法です

↓ LaTeXサンプル
[Easy Copy MathJax](https://easy-copy-mathjax.nakaken88.com/)

</div>
</div>

---

## 📔Marp独自機能

<div class="flex">
<div class="_">

**📝marp独自書式**

markdownからは離れるのですが、  
marp独自の書式・機能があります  
ディレクティブと呼びます

[Marp公式の説明](https://marpit.marp.app/directives)
[Qiitaの解説記事](https://qiita.com/takeshisakuma/items/5a61e6eac123d28602fb)

```text
<!-- _backgroundColor: #def -->
<!-- _header: ヘッダー -->
<!-- _footer: フッター -->
<!-- _paginate: true -->
```
</div>
<div class="_">

**💻表示サンプル**

表示は次のページで確認です  
項目は次の4つです

- 背景色が変わる
- 左上にヘッダー表示
- 左下にフッター表示
- 右下にページ表示

</div>
</div>

---

## 📔Marp独自機能（実践）

<div class="flex">
<div class="_">

**📝marp独自書式**

markdownからは離れるのですが、  
marp独自の書式・機能があります  
ディレクティブと呼びます

[Marp公式の説明](https://marpit.marp.app/directives)
[Qiitaの解説記事](https://qiita.com/takeshisakuma/items/5a61e6eac123d28602fb)

```text
<!-- _backgroundColor: #def -->
<!-- _header: ヘッダー -->
<!-- _footer: フッター -->
<!-- _paginate: true -->
```
</div>
<div class="_">

**💻表示サンプル**

表示は次のページで確認です  
項目は次の4つです

- 背景色が変わる
- 左上にヘッダー表示
- 左下にフッター表示
- 右下にページ表示

<!-- _backgroundColor: #def -->
<!-- _header: ヘッダー -->
<!-- _footer: フッター -->
<!-- _paginate: true -->

</div>
</div>

---

## 📔改ページ（これもmarp独自機能）

<div class="flex">
<div class="_">

**📝markdown書式**

Marpでは`---`で改ページになります

**💡`---`の本来の定義**

`---`が改ページというのはMarpの独自機能です。
本来は`<hr>`を意味します。

↓ `<hr>`サンプル
<hr>
</div>
<div class="_">

**💻表示サンプル**
ここまでの改ページ全てです

**💡見出しを改ページにする**
Front Matterで下記を指定することで
見出し（`# 見出し`）を改ページ＆見出しにできます
```YAML
headingDivider: 2
```

※数字で改ページとなる見出しレベルを指定します

</div>
</div>



