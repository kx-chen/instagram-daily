from flask import Flask, request
import os
from posttoinstagram import post_to_instagram

app = Flask(__name__)


def posting_password_is_correct(password):
    # TODO: add as decorator or before_request
    return password == os.environ['posting_password']


@app.route("/", methods=['GET'])
def index():
    return '<h1> Instagram Daily Poster </h1> <p> Created by <a href="github.com/kx-chen"> Kai Chen.</a>'


@app.route('/daily_post/onion', methods=['GET'])
def post_daily_onion():
    if posting_password_is_correct(request.args.get('posting_password')):
        return post_to_instagram(os.environ['onion_username'],
                                 os.environ['onion_password'],
                                 'onion.jpg',
                                 os.environ['onion_spreadsheet_id'])

    return 'Unauthorized', 403


@app.route('/daily_post/krabs', methods=['GET'])
def post_daily_krabs():
    if posting_password_is_correct(request.args.get('posting_password')):
        return post_to_instagram(os.environ['krabs_username'],
                                 os.environ['krabs_password'],
                                 'krabs.jpg',
                                 os.environ['krabs_spreadsheet_id'])
    return 'Unauthorized', 403


if __name__ == '__main__':
    app.run()
