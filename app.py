import requests
import schedule
import time

# Credenciales de la API de WhatsApp
API_URL = "https://graph.facebook.com/v15.0/<YourPhoneNumberID>/messages"
ACCESS_TOKEN = "<YourAccessToken>"

# Números de WhatsApp a los que se enviará el mensaje
recipients = [
    "521XXXXXXXXXX",  # Número 1
    "521XXXXXXXXXX",  # Número 2
    "521XXXXXXXXXX",  # Número 3
    "521XXXXXXXXXX",  # Número 4
    "521XXXXXXXXXX"   # Número 5
]

# Función para enviar mensajes
def send_reminder():
    for recipient in recipients:
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": recipient,
            "type": "template",
            "template": {
                "name": "reservation_reminder",  # Cambia al nombre de tu plantilla aprobada
                "language": {"code": "es"}
            }
        }
        response = requests.post(API_URL, headers=headers, json=data)
        print(f"Mensaje enviado a {recipient}: {response.status_code} - {response.json()}")

# Programar los recordatorios a las 8:00 AM y 10:00 AM todos los días
schedule.every().day.at("08:00").do(send_reminder)
schedule.every().day.at("10:00").do(send_reminder)

# Ejecutar el cron job
if __name__ == "__main__":
    print("Servicio de recordatorios iniciado...")
    while True:
        schedule.run_pending()
        time.sleep(1)
