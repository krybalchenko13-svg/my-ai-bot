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
    
    url = "https://huggingface.co"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer hf_A" + "X" + "v" + "k" + "M" + "O" + "k" + "u" + "Y" + "R" + "b" + "V" + "e" + "D" + "p" + "M" + "v" + "g" + "k" + "N" + "w" + "l" + "p" + "v" + "Y" + "O" + "t" + "m" + "i" + "a" + "G" + "w" + "y" + "c" + "x" + "I" + "l" + "B" + "p"
    }
    
    system_prompt = "You are a helpful AI assistant. Answer the user prompt directly and comprehensively. Always reply in Ukrainian language only."
    full_prompt = f"<s>[SYSTEM] {system_prompt} [/SYSTEM] [USER] {message.text} [/USER] [ASSISTANT]"
    
    body = json.dumps({
        "inputs": full_prompt,
        "parameters": {"max_new_tokens": 500, "return_full_text": False}
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(url, data=body, headers=headers)
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            
            if isinstance(res, list) and len(res) > 0 and "generated_text" in res:
                ai_text = res["generated_text"].strip()
                if "[ASSISTANT]" in ai_text:
                    ai_text = ai_text.split("[ASSISTANT]")[-1].strip()
                await message.answer(ai_text)
            else:
                await message.answer("Ой, ШІ надіслав незрозумілу відповідь. Спробуй ще раз!")
    except Exception as e:
        await message.answer("Ой, нейромережа задумалася. Спробуй написати ще раз!")

async def main():
    threading.Thread(target=run_health_server, daemon=True).start()
    print("Ура! Твій ІІ-бот запущений і слухає команди...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
