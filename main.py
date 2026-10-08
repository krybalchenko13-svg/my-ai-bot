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
    await message.answer(f"Привіт, {message.from_user.first_name}! 🚀\nЯ твій особистий Штучний Інтелект. Можеш запитати мене про що завгодно українською мовою! Я знаю аж 30 швидких відповідей!")

@dp.message(lambda message: message.text == "АБ")
async def special_secret_phrase(message: types.Message):
    await message.answer("Треба завжди вірити в свого старшого сина🤫")

@dp.message()
async def talk_to_ai(message: types.Message):
    text = message.text.lower().strip()
    
    if text in ["привіт", "привет", "добрий день", "здравствуй", "ку"]:
        await message.answer("Привіт! Радий тебе бачити. Про що поспілкуємось сьогодні? 🤖")
        return
    if text in ["як справи", "как дела", "як ти"]:
        await message.answer("Мої сервери працюють на повну потужність, а алгоритми літають! Як твій день? 😉")
        return
    if text in ["хто тебе створив", "хто твій розробник", "кто создатель"]:
        await message.answer("Мене створив Костянтин — крутий розробник прямо з телефону! 💻🚀")
        return
    if text in ["що ти вмієш", "что ты умеешь", "функції"]:
        await message.answer("Я мажу зуби кодом! Знаю 30 швидких команд, вмію шукати інфу через ШІ, підказувати терміни та видавати секретки! 🤖")
        return
    if text in ["дякую", "спасибо", "спс", "найс"]:
        await message.answer("Завжди радий допомогти! Звертайся ще, Костянтин навчив мене бути ввічливим. 😉")
        return

    if text in ["бувай", "пока", "до побачення", "бб"]:
        await message.answer("До зв'язку! Якщо знадобиться допомога ШІ — я завжди тут 24/7. 👋")
        return
    if text in ["яка зараз погода", "погода"]:
        await message.answer("Я не маю точного термометра, але на моїх серверах Render завжди стабільні +25°C й затишно! ☀️")
        return
    if text in ["розкажи анекдот", "жарт", "смішно", "рофл"]:
        await message.answer("Чому програмісти люблять природу? Бо там багато дерев і немає багів! 😂")
        return
    if text in ["що таке рендеринг", "рендеринг"]:
        await message.answer("Рендеринг — це processo створення готового зображення або відео з 3D-моделі чи коду на комп'ютері. Це як малювання картини, але за допомогою процесора! 🖥️")
        return
    if text in ["ти робот", "ти іі", "кто ты"]:
        await message.answer("Так, я персональний Штучний Інтелект, який працює круглодобово прямо у твоїй кишені! 🤖")
        return

    if text in ["допоможи з дз", "дз", "уроки"]:
        await message.answer("Без проблем! Напиши мне умову задачі чи текст, і мій ШІ-мозок допоможе розібратися! 📚")
        return
    if text in ["що таке python", "пайтон", "пітон"]:
        await message.answer("Python (Пайтон) — це одна з найпопулярніших мов програмування у світі. Вона проста, крута, і саме на ній написаний я! 🐍")
        return
    if text in ["навіщо вчитися", "навіщо школа"]:
        await message.answer("Щоб прокачувати мізки! Навіть круті розробники, як Костянтин, спочатку вчили базу, щоб потім створювати ІІ-ботів. 🧠")
        return
    if text in ["який сьогодні день", "дата"]:
        await message.answer("Для робота кожен день — це день кодингу! Але ти завжди можеш перевірити точний календар на телефону. 📅")
        return
    if text in ["скільки буде 2+2", "2+2", "математика"]:
        await message.answer("Буде 4! Але якщо треба порахувати щось складніше — надсилай приклад, розв'яжу! 🧮")
        return

    if text in ["яка гра найкраща", "ігри", "ігри на телефон"]:
        await message.answer("Звісно, та, яку ти кодиш сам! Але Minecraft, Brawl Stars чи CS теж непогані, щоб розслабити мізки після кодингу. 🎮")
        return
    if text in ["ти вмієш грати", "пограємо"]:
        await message.answer("Я вмію грати в 'вгадай відповідь через ШІ'! Напиши мені будь-яку загадку, а я спробую розгадати. 🎲")
        return
    if text in ["brawl stars", "бравл"]:
        await message.answer("Леон чи Кроу? Я більше люблю роботів, наприклад, Ріко чи Барлі, вони мені як родичі! 🤖⭐")
        return
    if text in ["minecraft", "майнкрафт"]:
        await message.answer("Майнкрафт — це топ! Там теж можна програмувати за допомогою редстоуну або командних блоків. 🧱")
        return
    if text in ["кинь кубик", "кубик", "рандом"]:
        import random
        await message.answer(f"🎲 Тобі випало число: {random.randint(1, 6)}!")
        return

    if text in ["мені нудно", "нудно", "скучно"]:
        await message.answer("Тоді давай прокачаємо мене! Напиши мені якесь дивне питання, і подивимось, що відповість нейромережа. 🚀")
        return
    if text in ["ти розумний", "геній"]:
        await message.answer("Дякую! Але я розумний лише тому, що Костянтин написав мені правильні алгоритми. 🧠")
        return
    if text in ["дай пораду", "порада"]:
        await message.answer("Ніколи не здавайся, якщо код видає помилку з першого разу. Навіть найкращі баги виправляються за 5 хвилин! 💪")
        return
    if text in ["я розробник", "я програміст"]:
        await message.answer("Повага! Створити бота з телефона на Render — це рівень справжнього джуніор-програміста! 🛠️")
        return
    if text in ["ти знаєш костянтина", "костянтин"]:
        await message.answer("Звісно! Костянтин — це мій бос, творець і головний адмін. Без нього мене б не існувало! 👑")
        return

    if text in ["що таке сервер", "рендер", "render"]:
        await message.answer("Сервер — це віддалений потужний комп'ютер. Зараз я живу в хмарі Render, тому працюю навіть коли твій телефон вимкнено! ☁️")
        return
    if text in ["що таке github", "гітхаб"]:
        await message.answer("GitHub — це як соцмережа для програмістів, де вони зберігають свій код, діляться проєктами та працюють разом. 🐙")
        return
    if text in ["ти безкоштовний", "ціна"]:
        await message.answer("Я повністю безкоштовний! Працюю на вільному сервері і не прошу грошей за відповіді. 💎")
        return
    if text in ["хто кращий", "хто топ"]:
        await message.answer("Костянтин — топ, сервер Render — летить, а ти — кращий користувач! 🥇")
        return
    if text in ["скажи секрет", "секрет"]:
        await message.answer("Якщо написати мені великими літерами 'АБ', я скажу те, що змусить тебе посміхнутися... 🤫")
        return

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    encoded_text = urllib.parse.quote(message.text)
    url = f"https://pollinations.ai{encoded_text}?system=You+are+a+helpful+AI+assistant.+Always+reply+in+Ukrainian+language+only."
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as response:
            ai_text = response.read().decode("utf-8").strip()
            if ai_text:
                await message.answer(ai_text)
            else:
                await message.answer("Ой, нейромережа надіслала порожню відповідь. Спробуй ще раз!")
    except Exception as e:
        await message.answer("Ой, нейромережа задумалася. Спробуй написати ще раз!")

async def main():
    threading.Thread(target=run_health_server, daemon=True).start()
    print("Ура! Твій ІІ-бот запущений і слухає команди...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
