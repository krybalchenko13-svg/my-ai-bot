
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
    
    url = "https://aryahcr.cc"
    headers = {"Content-Type": "application/json"}
    body = json.dumps({
        "prompt": message.text,
        "model": "gpt-4"
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(url, data=body, headers=headers)
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            if "id" in res:
                # Если апи вернул сырой json с текстом
                url_get = f"https://aryahcr.cc/{res['id']}"
                req_get = urllib.request.Request(url_get)
                with urllib.request.urlopen(req_get) as res_get:
                    final_res = json.loads(res_get.read().decode("utf-8"))
                    ai_text = final_res.get("text", "Не вдалося отримати текст відповіді.")
            else:
                ai_text = res.get("text", "Ой, нейромережа задумалася. Спробуй ще раз!")
            await message.answer(ai_text)
    except Exception as e:
        # Резервный полностью открытый апи ИИ, если первый лагает
        try:
            url_backup = "https://lolhuman.xyz" + urllib.parse.quote(message.text)
            req_b = urllib.request.Request(url_backup, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_b) as response_b:
                res_b = json.loads(response_b.read().decode("utf-8"))
                await message.answer(res_b.get("result", "Повтори запит ще раз, будь ласка!"))
        except:
            await message.answer("Ой, нейромережа задумалася. Спробуй написати ще раз!")

async def main():
    threading.Thread(target=run_health_server, daemon=True).start()
    print("Ура! Твій ІІ-бот запущений і слухає команди...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
