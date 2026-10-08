
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import json
import urllib.request
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

TELEGRAM_TOKEN = "8782557859:AAGGpwAn1Iu4SMg7J53vSUXLtGE_Q0XKYsg"

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")
    def log_message(self, format, *args):
        return

def run_health_server():
    server = HTTPServer(('0.0.0.0', 10000), HealthCheckHandler)
    server.serve_forever()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Привіт, {message.from_user.first_name}! 🚀\nЯ твій особистий Штучний Інтелект. Можеш запитати мене про що завгодно українською мовою!")

@dp.message()
async def talk_to_ai(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    encoded_text = urllib.parse.quote(message.text)
    url = f"https://duckduckgo.com{encoded_text}&format=json"
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            if res.get("AbstractText"):
                reply = res["AbstractText"]
            elif res.get("RelatedTopics") and len(res["RelatedTopics"]) > 0 and "Text" in res["RelatedTopics"][0]:
                reply = res["RelatedTopics"][0]["Text"]
            else:
                reply = f"Я отримав твоє повідомлення: {message.text}. Моя база даних оновлюється!"
            await message.answer(f"🤖 ШІ відповів:\n\n{reply}")
    except Exception as e:
        await message.answer("Ой, нейромережа задумалася. Спробуй написати ще раз!")

async def main():
    threading.Thread(target=run_health_server, daemon=True).start()
    print("Ура! Твій ІІ-бот запущений і слухає команди...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


