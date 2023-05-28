from pyrogram import Client, filters

from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton


api_id = *****  # دریافت از my.telegram.org

api_hash = '*****' 

bot_token = '*****'  


app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("start"))

def start_handler(client, message):
    keyboard = [
        [KeyboardButton("خرید")],
        [KeyboardButton("فروش")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    client.send_message(message.chat.id, "لطفاً یک گزینه را انتخاب کنید:", reply_markup=reply_markup)


@app.on_message(filters.text)
def reply_handler(client, message):
    text = message.text

    if text == "خرید":
        client.send_message(message.chat.id, "شما دکمه خرید را انتخاب کردید!")
    
    elif text == "فروش":
        keyboard = [
            ["فروش عادی"],
            ["فروش وی ای پی"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        client.send_message(message.chat.id, "لطفاً نوع فروش را انتخاب کنید:", reply_markup=reply_markup)

    elif text == "فروش عادی":
        client.send_message(message.chat.id, "شما فروش عادی را انتخاب کردید!")
    
    elif text == "فروش وی ای پی":
        client.send_message(message.chat.id, "شما فروش وی ای پی را انتخاب کردید!")

app.run()