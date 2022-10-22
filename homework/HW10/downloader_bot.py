from aiogram import *
from pytube import YouTube


bot = Bot('5559753149:AAGazCkcwIH824jcD2qP3Wn_ErTwPq4vUY8')
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Привет от бота-пирата! Можем скачать ролик с <b>YouTube</b> по твоему завпросу.\n'
                                    'Введи ссылку на видео: ', parse_mode='html')

@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f'Йо-хо-хо, загрузка ролика <b>"{yt.title}"</b> началась!', parse_mode='html')
        await downloader(url, message, bot)

async def downloader(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption='<b>А вот и ролик!</b>', parse_mode='html')
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')


if __name__ == '__main__':
    executor.start_polling(dp)