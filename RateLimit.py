# Flask Server with Limiter Defense
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Rate limiter configuration
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]  # Adjust as needed
)

@app.route('/')
def index():
    return "Hello! You're accessing a rate-limited server."

if __name__ == '__main__':
    app.run(debug=True)
