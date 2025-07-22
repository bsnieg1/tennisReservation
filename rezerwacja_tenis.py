import requests
import time
from datetime import datetime, timedelta

ACCESS_TOKEN = "YOUR TOKEN HERE"

TARGET_HOUR = 0
TARGET_MINUTE = 0
reservationDate = datetime.now()+timedelta(days=5)
year = str(reservationDate.year)
month = str(reservationDate.month)
day = str(reservationDate.day)
hourStart = input("Podaj godzinę (6-20): ")
hourEnd = str(int(hourStart)+1)
if len(month) == 1:
    month = "0" + str(month)
if len(str(hourStart)) == 1:
    hourStart = "0" + str(hourStart)
if len(str(hourEnd)) == 1:
    hourEnd = "0" + str(hourEnd)
print(f"Rezerwacja na {year}-{month}-{day} od {hourStart}:00 do {hourEnd}:00")
payload = {
    "starts_at": f"{year}-{month}-{day}T{hourStart}:00:00.000Z",
    "ends_at": f"{year}-{month}-{day}T{hourEnd}:00:00.000Z",
    "station_id": 24,
    "payment_method": "ONLINE",
    "tariff_id": 12,
    "multisport_cards": 0,
    "medicover_cards": 0,
    "lightning": False,
    "message": "",
    "przelewy24_return_url": "https://app.tenis4u.pl/#/court/3?p24success=true"
}

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-Tenis-User-Agent": "tenis4u-web-frontoffice/3.4.0"
}
 
def wait_until_target_time(hour, minute):
    now = datetime.now()
    target_time = now.replace(hour=hour, minute=minute, second=1, microsecond=0)
    if target_time < now:
        target_time += timedelta(days=1) 

    seconds_to_wait = (target_time - now).total_seconds()
    print(f"Czekam do godziny {target_time.strftime('%H:%M:%S')} ({int(seconds_to_wait)} sekundy)...")
    time.sleep(seconds_to_wait)

def send_reservation():
    print("Wysyłam żądanie rezerwacji...")
    response = requests.post("https://api.tenis4u.pl/reservation", json=payload, headers=headers)
    print("Status:", response.status_code)
    print("Odpowiedź:")
    print(response.text)

if __name__ == "__main__":
    wait_until_target_time(TARGET_HOUR, TARGET_MINUTE)
    send_reservation()
    print("Rezerwacja została wysłana.")
