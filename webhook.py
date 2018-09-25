from flask import Flask, request, abort
import os, datetime
from InstagramAPI import InstagramAPI

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
quotes = [
    "An onion can make people cry but there's never been a vegetable that can make people laugh.",

    "All we have to do is to peel the shrines like an onion, and we will be with the king himself.",

    "If you dig deep and keep peeling the onion, artists and freelance writers are the leaders in society - the "
    "people who start to get new ideas out.",

    "Good intentions are not enough. They've never put an onion in the soup yet.",

    "Life is like an onion. You peel it off one layer at a time, and sometimes you weep.",

    "It doesn't matter how precisely the onion is cut as long as the person chewing it is happy.",

    "The real secret to guacamole is that you use exactly the elements that you need, which is cilantro, onion, "
    "tomato, and jalapenos. And, of course, avocado.",

    " 'I will not move my army without onions!' -Ulysses S. Grant",

    "'The onion and its satin wrappings is among the most beautiful of vegetables and is the only one that represents "
    "the essence of things. It can be said to have a soul.' -My Summer in a Garden by Charles Dudley Warner",

    " 'It is hard to imagine civilization without onions.' -Julia Child",

    """ "Onion skins very thin,
    Mild winter coming in.
    Onion skins very tough,
    Coming winter very rough."
    -old English rhyme """,

    """ "If you hear an onion ring, answer it." -Anonymous """,

    " 'It's probably illegal to make soups, stews and casseroles without plenty of onions.' "
    "-Maggie Waldron, American author and editor ",

    " 'Onions can make even heirs and widows weep.' -Benjamin Franklin",

    "'Life is like an onion; you peel off layer after layer and then you find there is nothing in it.' -James Gibbons "
    "Huneker, American musician, critic",

    """ "For this is every cook's opinion,
    No savoury dish without an onion;
    But lest your kissing should be spoiled,
    Your onions should be thoroughly boiled."
    -Jonathon Swift, Irish satirist """,

    " \"Take care to chop the onion fine.\" -Opening line of Like Water for Chocolate by Laura Esquivel",

    """ "Why is it that the poet tells
    So little of the sense of smell?
    These are the odors I love well:
    The smell of coffee freshly ground;
    Or rich plum pudding, holly crowned;
    Or onions fried and deeply browned…"
    -Christopher Morley, poet """,

    " \"It was for bringing the cook tulip-roots instead of onions.\" "
    "-The reason the Queen of Hearts wants to behead the Seven-of-Spades in "
    "Alice's Adventures in Wonderland by Lewis Carroll",

    " \"Mine eyes smell onions: I shall weep anon.\" -All's Well that Ends Well by William Shakespeare ",

    " \"The onion tribe is prophylactic and highly invigorating, and even more necessary to "
    "cookery than parsley itself.\" "
    "-George Ellwanger, British food writer ",

    " \"Banish (the onion) from the kitchen and the pleasure flies with it. Its presence lends color and enchantment to the most modest dish; its absence reduces the rarest delicacy to hopeless insipidity, and dinner to despair.\"  "
    "-Elizabeth Robbins Pennell, American columnist",

    " The term 'personal ambition' immediately puts me off. "
    "It feels like finding a sliver of onion in my ice cream. "
    "There's nothing wrong with a sliver of onion, but I don't want it in my ice cream.",

    "Onion rings in the car cushions do not improve with time. - Erma Bombeck",

    "It doesn't matter how precisely the onion is cut as long as the person chewing it is happy. -Padma Lakshmi",

    "Good intentions are not enough. They've never put an onion in the soup yet. -Sonya Levien",

    "It is hard to imagine civilization without onions. -Julia Child",

    "I will not move my army without onions! -Ulysses S. Grant",

    "If you hear an onion ring, answer it. -Anonymous",

    "[on the BMW X3] If you are clinically insane, by which I mean you wake up in the morning and think you are an "
    "onion, here's your car -Jeremy Clarkson",

    "The onion and its satin wrappings is among the most beautiful of vegetables and is the only one that represents "
    "the essence of things. It can be said to have a soul. -My Summer in a Garden by Charles Dudley Warner "
]


@app.route('/daily_post', methods=['GET'])
def webhook():
    instagram = InstagramAPI(os.environ['username'], os.environ['password'])
    instagram.login()  # login

    day_number = datetime.date.today().strftime("%d")
    photo_path = dir_path + '/onion.jpg'
    caption = quotes[int(day_number) - 1] + " #dailyonion"
    instagram.uploadPhoto(photo_path, caption=caption)
    return 'Sucessfully posted.'


@app.route("/", methods=['GET'])
def index():
    return '<a href="/daily_post"> Daily post - click here </a>'


if __name__ == '__main__':
    app.run()
