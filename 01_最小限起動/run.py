from flask import Flask #Flaskクラスのインポート
app = Flask(__name__) #appという名前のFlaskクラスのインスタンスを作成
@app.route("/") #ルーティング(URLの設定）
def hello(): #"/"のURLで呼び出される関数
    return "Hello World!"
if __name__ == "__main__":
    app.run() #Webサーバーを立ち上げる
