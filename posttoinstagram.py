from InstagramAPI import InstagramAPI
from flask import jsonify, json
import datetime, os
import requests


dir_path = os.path.dirname(os.path.realpath(__file__))


def get_quotes_from_api(spreadsheet_id):
    return requests.get("http://gsx2json.com/api?id=" + spreadsheet_id)


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


def post_to_instagram(username, password, image, spreadsheet_id):
    try:
        instagram = InstagramAPI(username, password)
        instagram.login()  # login

        quotes_json = get_quotes_from_api(spreadsheet_id).text
        quotes_parsed = json.loads(quotes_json)

        day_number = datetime.date.today().strftime("%b %d, %Y").replace(" 0", " ")
        photo_path = dir_path + '/' + image
        caption = ""

        for i in quotes_parsed['rows']:
            if i['scheduledpostingdate'] == day_number:
                caption = i['caption']

        instagram.uploadPhoto(photo_path, caption=caption)
        response = jsonify({'status': '200', 'message': 'Posted.'})
        return response, 200

    except Exception:
        # traceback.print_exc()
        send_error_pushed_notification()
        return 'Not worked.'
