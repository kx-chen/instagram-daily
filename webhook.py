# instapy -u kaiusesthis -p password899 -f https://instagram.fcxh3-1.fna.fbcdn.net/vp/c5ef6cab120b908d85657dfca4966d25/5B6DBF75/t51.2885-15/e35/30605196_182396209053880_8553512260012605440_n.jpg?ig_cache_key=MTc1NzU0MjM5MjkwMTQ1NDIxOQ%3D%3D.2  -t 'staging account'

from flask import Flask, request, abort
import os 
import pynstagram

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))

@app.route('/webhook', methods=['GET'])
def webhook():
    os.system("""instapy -u kaiusesthis -p password899 -f https://instagram.fcxh3-1.fna.fbcdn.net/vp/c5ef6cab120b908d85657dfca4966d25/5B6DBF75/t51.2885-15/e35/30605196_182396209053880_8553512260012605440_n.jpg?ig_cache_key=MTc1NzU0MjM5MjkwMTQ1NDIxOQ%3D%3D.2  -t 'staging account' """)
    return 'success'

if __name__ == '__main__':
    app.run()