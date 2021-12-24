import os
import time
import uuid

try:
    from discord_webhook import DiscordWebhook
except:
    print("installing discord-webhook")
    os.system("pip install discord-webhook")
try:
    from colorama import Fore
except:
    print("installing colorama")
    os.system("pip install colorama")

os.system('cls')
InfoPrefix = Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "INFO" + Fore.WHITE + "] "
ErrorPrefix = Fore.WHITE + "[" + Fore.RED + "ERROR" + Fore.WHITE + "] "


def main():
    webhookurl: str = input(InfoPrefix + "Enter the WebhookURL: ")
    if len(webhookurl) == 0:
        os.system("cls")
        print(ErrorPrefix + "The WebhookURL can't be None")
        main()
    message: str = input(InfoPrefix + "Enter the message to send: ")
    if len(message) == 0:
        message = f"Webhook Spammer by 04mansur11#5858 "
    delay: int = input(InfoPrefix + "Enter the delay: ")
    if len(delay) == 0:
        delay = 0.42069
    try:
        delay + 1
    except Exception:
        delay = 0.42069

    try:
        while True:
            webhook = DiscordWebhook(url=webhookurl, content=f"{message} | {str(uuid.uuid4())[:4]}")
            webhook.execute()
            print(InfoPrefix + f"Message sent: {message}")
            time.sleep(delay)
    except Exception:
        os.system('cls')
        print(ErrorPrefix + "Invalid webhook")
        main()


if __name__ == '__main__':
    main()
