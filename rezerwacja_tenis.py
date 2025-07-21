import requests
import time
from datetime import datetime, timedelta

ACCESS_TOKEN = "b0051da2-262d-47b3-8eba-4f9f39a994bd"

TARGET_HOUR = 0
TARGET_MINUTE = 0

payload = {
    "starts_at": "2025-07-21T17:00:00.000Z",
    "ends_at": "2025-07-21T18:00:00.000Z",
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
    target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
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
