from flask import Flask, request, jsonify
import os, datetime, requests, json, traceback
from InstagramAPI import InstagramAPI

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_quotes_from_api():
    return requests.get("http://gsx2json.com/api?id=13U7aLuYgzzrf-RoJOP3lQseo7ZFCV4mGCzDi14fFrBs")


def send_error_pushed_notification():
    payload = {
        "app_key": "P7JRBmU9awdQTEMvG2hC",
        "app_secret": "OZQcniD4lcPJajoJYzEJUjfz3pazmK8o58CtqZ7i6fRle73YULy4TcWm8m7Fkg40",
        "target_type": "channel",
        "target_alias": "IwA4Rw",
        "content": "Critical Onion failure: failed to post daily onion!!"
    }

    r = requests.post("https://api.pushed.co/1/push", data=payload)



    print(r.text)
@app.route("/", methods=['GET'])
def index():
    return '<a href="/daily_post"> Daily post - click here </a>'


@app.route('/daily_post', methods=['GET'])
def webhook():
    if request.args.get('password') != os.environ['posting_password']:
        response = jsonify({'status': '401', 'error': 'Unauthorized'})
        send_error_pushed_notification()
        return response, 401

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
        response = jsonify({'status': '200', 'message': 'Posted.'})
        return response, 200

    except Exception:
        # traceback.print_exc()
        send_error_pushed_notification()
        return 'Not worked.'


if __name__ == '__main__':
    app.run()
