import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import random

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
    await message.answer(f"Привіт, {message.from_user.first_name}! 🚀\nЯ твій персональний розумний ШІ-співрозмовник. Напиши мені щось!")

@dp.message()
async def talk_to_ai(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(1)
    
    text = message.text.lower()
    
    answers_hello = [
        "Привіт! Радий тебе чути. Про що будемо кодити сьогодні? 💻",
        "Привіт! Як твої справи? Я готовий до роботи! 🚀",
        "О, привіт! Якраз оновлював свої алгоритми. Що цікавого розкажеш? 🤖"
    ]
    
    answers_how_are_you = [
        "Мої плати працюють на повну потужність! 🔋 Як твій день минає?",
        "Все супер, сервер летить! Думаю, як стати ще розумнішим. А ти як? 😉",
        "Я ж робот, у мене завжди все стабільно 101010. Як сам?"
    ]
    
    answers_what_doing = [
        "Аналізую гігабайти інформації та чекаю на твої повідомлення! 🧐",
        "Працюю 24/7 на сервері Render без відпочинку, щоб писати тобі! 🖥️",
        "Вивчаю мову Python, вона дуже крута. А ти чим займаєшся?"
    ]
    
    answers_default = [
        f"Ти написав: \"{message.text}\". Це дуже цікава думка! Розкажи про це детальніше 🤔",
        f"Хм, твій запит \"{message.text}\" прийнято в мій віртуальний мозок! Давай розвивати цю тему 🚀",
        f"Я зафіксував твої слова. Ти правий! Що ще додаси до цього? 🤖"
    ]
    
    if any(word in text for word in ["привет", "привіт", "дарова", "hello"]):
        reply = random.choice(answers_hello)
    elif any(word in text for word in ["дела", "справи", "як ти"]):
        reply = random.choice(answers_how_are_you)
    elif any(word in text for word in ["делаешь", "робиш", "зайнятий"]):
        reply = random.choice(answers_what_doing)
    else:
        reply = random.choice(answers_default)
        
    await message.answer(reply)

async def main():
    threading.Thread(target=run_health_server, daemon=True).start()
    print("Ура! Твій ІІ-бот запущений і слухає команди...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


