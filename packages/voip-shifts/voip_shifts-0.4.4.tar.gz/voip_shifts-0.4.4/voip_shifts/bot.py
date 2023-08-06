import requests as r
from voip_shifts.config import Config
import logging


log = logging.getLogger(__name__)
users = {
    "uQvek": "240641855",
}
class Bot():

    def check(self):
        resp = self.session.get(f"{self.baseUrl}/getMe")
        if not resp.json()['ok']:
            print(resp.text)
        else:
            print("OK")
            return True

    def __init__(self):
        self.session = r.Session()
        self.baseUrl = "https://api.telegram.org/bot" + Config.BOT_KEY
        self.check()

    def send_message(self, dst, msg):
        params = {"chat_id": dst, "text": msg, "parse_mode": "html"}
        resp = self.session.get(f"{self.baseUrl}/sendMessage", params=params)
        print(resp.json())
    
    def send_messages(self, msg):
        for user, user_id in users.items():
            log.info(f"Sending message to {user}")
            self.send_message(user_id, msg)


bot = Bot()
