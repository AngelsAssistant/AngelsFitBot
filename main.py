from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = "Привет, я — твой AngelaFitBot! Готова к работе."
    bot.send_message(chat_id=chat_id, text=message)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "AngelaFitBot работает!"

if __name__ == "__main__":
    app.run()