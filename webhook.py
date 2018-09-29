from flask import Flask, request, abort
import os, datetime, requests, json, traceback
from InstagramAPI import InstagramAPI

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_quotes_from_api():
    return requests.get("http://gsx2json.com/api?id=13U7aLuYgzzrf-RoJOP3lQseo7ZFCV4mGCzDi14fFrBs")


@app.route('/daily_post', methods=['GET'])
def webhook():
    try:
        instagram = InstagramAPI(os.environ['username'], os.environ['password'])
        instagram.login()  # login

        quotes_json = get_quotes_from_api().text
        quotes_parsed = json.loads(quotes_json)

        day_number = datetime.date.today().strftime("%B %d, %Y")
        photo_path = dir_path + '/onion.jpg'
        caption = "There's no quote for the onion today, enjoy!"
        for i in quotes_parsed['rows']:
            if i['scheduledpostingdate'] == day_number:
                caption = i['title']

        instagram.uploadPhoto(photo_path, caption=caption)
        return 'Sucessfully posted.'

    except Exception:
        payload = {
            "app_key": "P7JRBmU9awdQTEMvG2hC",
            "app_secret": "OZQcniD4lcPJajoJYzEJUjfz3pazmK8o58CtqZ7i6fRle73YULy4TcWm8m7Fkg40",
            "target_type": "channel",
            "target_alias": "IwA4Rw",
            "content": "Critical Onion failure: failed to post daily onion!!"
        }

        r = requests.post("https://api.pushed.co/1/push", data=payload)
        print(r.text)
        # traceback.print_exc()
        return 'Not worked.'


@app.route("/", methods=['GET'])
def index():
    return '<a href="/daily_post"> Daily post - click here </a>'


if __name__ == '__main__':
    app.run()
