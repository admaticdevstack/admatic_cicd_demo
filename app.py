from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='admaticredis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello RoboChef Admatic World Again! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

