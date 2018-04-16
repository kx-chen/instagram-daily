from flask import Flask, request, abort
import os, datetime
from InstagramAPI import InstagramAPI

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
quotes = [
	"An onion can make people cry but there's never been a vegetable that can make people laugh.",
	"All we have to do is to peel the shrines like an onion, and we will be with the king himself.",
	"If you dig deep and keep peeling the onion, artists and freelance writers are the leaders in society - the people who start to get new ideas out.",
	"Good intentions are not enough. They've never put an onion in the soup yet.",
	"Life is like an onion. You peel it off one layer at a time, and sometimes you weep.",
	"It doesn't matter how precisely the onion is cut as long as the person chewing it is happy.",
	"The real secret to guacamole is that you use exactly the elements that you need, which is cilantro, onion, tomato, and jalapenos. And, of course, avocado."
]

@app.route('/daily_post', methods=['GET'])
def webhook():
    Instagram = InstagramAPI(os.environ['username'], os.environ['password'])
    Instagram.login()  # login

    day_number = datetime.date.today().strftime("%w")
    photo_path = dir_path + '/onion.jpg'
    caption = quotes[int(day_number)] + " #dailyonion"
    Instagram.uploadPhoto(photo_path, caption=caption)
    return 'Sucessfully posted.'

@app.route("/", methods=['GET'])
def index():
    return '<a href="/daily_post"> daily post </a>'

if __name__ == '__main__':
    app.run()
