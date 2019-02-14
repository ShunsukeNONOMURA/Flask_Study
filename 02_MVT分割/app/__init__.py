from flask import Flask, render_template #Flaskクラスのインポート

#appという名前のFlaskクラスのインスタンスを作成
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# 404エラーを逃がす
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# コントローラモジュールに接続
from app.controllers.moduleA import mod_moduleA
app.register_blueprint(mod_moduleA)
