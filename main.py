import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import json
import urllib.request
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
    await message.answer(f"Привіт, {message.from_user.first_name}! 🚀\nЯ твій особистий Штучний Інтелект. Запитай мене про що завгодно українською мовою!")

@dp.message()
async def talk_to_ai(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    url = "https://openrouter.ai"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    body = json.dumps({
        "model": "google/gemini-2.5-flash:free",
        "messages": [{"role": "user", "content": message.text}]
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(url, data=body, headers=headers)
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            ai_text = res["choices"][0]["message"]["content"]
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
