from flask import Flask  # 載入 Flask
app = Flask(__name__)  # 建立 Application 物件

# 建立網站首頁的回應方式


@app.route("/YunHui")
def index():    # 用來回應網站首頁連線的函式
    return "Hello Flask"  # 回傳網站首頁的內容

app.run()
