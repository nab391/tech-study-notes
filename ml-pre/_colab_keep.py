import sys
import time
import datetime
import webbrowser
import platform

# 前処理：引数チェック
if len(sys.argv) < 2:
    print("Usage: python " + sys.argv[0] + " <url>")
    exit()
else:
    url = sys.argv[1]

# OS 判定とブラウザ設定
os_name = platform.system()

if os_name == 'Windows':
    browser_path = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" %s'
elif os_name == 'Darwin':  # macOS
    browser_path = '"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" %s'
else:
    print(f"Unsupported OS: {os_name}")
    exit()

# ブラウザ取得
try:
    browser = webbrowser.get(browser_path)
except webbrowser.Error as e:
    print(f"Could not get browser: {e}")
    exit()

# 1時間毎に指定のノートブックを開く
for i in range(12):
    browser.open(url)
    #print(i, datetime.datetime.today())
    print(f"{i+1}回目: {datetime.datetime.now()}")
    time.sleep(60 * 60)
