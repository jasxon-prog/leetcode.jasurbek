# import os
# from cryptography.fernet import Fernet
#
# # Kalit yaratish yoki o'qish
# if not os.path.exists("secret.key"):
#     with open("secret.key","wb") as f: f.write(Fernet.generate_key())
# key = open("secret.key","rb").read()
# fernet = Fernet(key)
#
# while True:
#     print("\n1.Create 2.Write 3.Read 4.Delete 5.Exit")
#     ch = input("Choice: ")
#
#     if ch=="1":
#         fn = input("File name: ")
#         open(fn,"wb").close()
#         print(f"{fn} created.")
#     elif ch=="2":
#         fn = input("File name: ")
#         if os.path.exists(fn):
#             data = input("Text: ").encode()
#             with open(fn,"ab") as f: f.write(fernet.encrypt(data)+b"\n")
#             print("Encrypted and saved.")
#         else: print("File not found.")
#     elif ch=="3":
#         fn = input("File name: ")
#         if os.path.exists(fn):
#             with open(fn,"rb") as f:
#                 for line in f:
#                     try: print(fernet.decrypt(line.strip()).decode())
#                     except: print("[Error: corrupted or non-encrypted]")
#         else: print("File not found.")
#     elif ch=="4":
#         fn = input("File name: ")
#         if os.path.exists(fn): os.remove(fn); print(f"{fn} deleted.")
#         else: print("File not found.")
#     elif ch=="5": break
#     else: print("Invalid choice.")


import json
from datetime import datetime
import uuid
import os
import shutil
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "7812513714:AAE7JxJUtOMmoTLpm0c6c_lC-y_y-VWZTu0"
CHAT_ID = "7289783045"

bot = Bot(token=TOKEN)
dp = Dispatcher()

os.makedirs("Incidents", exist_ok=True)
FILENAME = "Incidents/incidents.json"

recommendations = {
    "virus": "💡 Tavsiya: Antivirusni yangilang va zaxira nusxa oling.",
    "phishing": "💡 Tavsiya: Shubhali linklarga bosmaslikni o‘rgating.",
    "xodim_xatosi": "💡 Tavsiya: Xodimni ogohlantiring va parol siyosatini kuchaytiring.",
    "boshqa": "💡 Tavsiya: Xavfsizlik choralarini ko‘ring."
}

def load_incidents():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_incidents(incidents):
    with open(FILENAME, "w") as f:
        json.dump(incidents, f, indent=4)
    shutil.copy(FILENAME, "Incidents/backup_incidents.json")

async def add_incident(incident_type, description):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    incident = {
        "id": str(uuid.uuid4()),
        "type": incident_type,
        "description": description,
        "date": date
    }
    incidents = load_incidents()
    incidents.append(incident)
    save_incidents(incidents)

    advice = recommendations.get(incident_type, "💡 Tavsiya: Xavfsizlik choralarini ko‘ring.")
    message = f"Yangi insident qo‘shildi!\n\nTuri: {incident_type}\nTavsif: {description}\nSana: {date}\n\n{advice}\n(Zaxira nusxasi olingan.)"

    await bot.send_message(chat_id=CHAT_ID, text=message)

@dp.message()
async def handle_message(message: types.Message):
    if message.text.startswith("/start"):
        await message.reply(
            "Salom! Siz axborot xavfsizligi insidentlarini qo‘shishingiz mumkin.\n\n"
            "Format: turi | tavsif\nMasalan: virus|Kompyuter virus yuqtirdi"
        )
        return

    try:
        incident_type, description = message.text.split("|", 1)
        incident_type = incident_type.strip().lower()
        description = description.strip()
        await add_incident(incident_type, description)
        await message.reply("✅ Insident qo‘shildi va Telegramga yuborildi!")
    except ValueError:
        await message.reply(
            "❌ Format noto‘g‘ri. Iltimos, quyidagicha yuboring:\nTURI | TAVSIF\nMasalan: virus|Kompyuter virus yuqtirdi"
        )

async def main():
    try:
        print("Bot ishga tushdi...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())