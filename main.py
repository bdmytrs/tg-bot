from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from keep_alive import keep_alive
import time

# ВСТАВЬ СЮДА СВОЙ ТОКЕН
TOKEN = '8004137089:AAHCPyGULe6ON6nqcQoK5zXWjQKOfTGCkIA'

# Список chat_id групп, куда пересылать (нужен минус перед ID!)
GROUP_CHAT_IDS = [
    -4773983672,
    -4628960734,
    # ... до 250 групп
]

def start(update, context):
    update.message.reply_text("Бот работает и готов пересылать сообщения!")

def forward_all(update, context):
    message = update.message

    for group_id in GROUP_CHAT_IDS:
        try:
            if message.text:
                context.bot.send_message(chat_id=group_id, text=message.text)

            elif message.photo:
                context.bot.send_photo(chat_id=group_id, photo=message.photo[-1].file_id, caption=message.caption or '')

            elif message.document:
                context.bot.send_document(chat_id=group_id, document=message.document.file_id, caption=message.caption or '')

            elif message.video:
                context.bot.send_video(chat_id=group_id, video=message.video.file_id, caption=message.caption or '')

            elif message.audio:
                context.bot.send_audio(chat_id=group_id, audio=message.audio.file_id, caption=message.caption or '')

            elif message.voice:
                context.bot.send_voice(chat_id=group_id, voice=message.voice.file_id)

            elif message.sticker:
                context.bot.send_sticker(chat_id=group_id, sticker=message.sticker.file_id)

            # Спим 0.1 секунды между отправками (чтобы не словить блокировку)
            time.sleep(0.1)

        except Exception as e:
            print(f"Ошибка при пересылке в {group_id}: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all & ~Filters.command, forward_all))

    updater.start_polling()
    updater.idle()

keep_alive()
main()
