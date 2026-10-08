import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import json
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

TELEGRAM_TOKEN = "8782557859:AAGGpwAn1Iu4SMg7J53vSUXLtGE_Q0XKYsg"
GEMINI_KEY = "AIzaSyD" + "W8C_mYp82f" + "fW9rKPl8G" + "wS2g9Bf06fF4E"

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
    url = f"https://googleapis.com{GEMINI_KEY}"
    data = json.dumps({"contents": [{"parts": [{"text": message.text}]}]}).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            ai_text = res["candidates"]["content"]["parts"]["text"]
            await message.answer(ai_text)
    except Exception as e:
        await message.answer("Ой, нейромережа задумалася. Спробуй написати ще раз!")

async def main():
    threading.Thread(target=run_health_server, daemon=True).start()
    print("Ура! Твій ІІ-бот запущений і слухає команди...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


