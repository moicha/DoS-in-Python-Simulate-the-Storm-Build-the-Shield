#Imports

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from pyngrok import ngrok


# Initialize Flask App
app = Flask(__name__)

# Add rate limiting
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])


# Define the homepage (/) of the web app and show a sample welcome message
@app.route("/")
def home():
    return "Welcome to the rate-limited Flask server!"

# Open a tunnel on port 5000
public_url = ngrok.connect(5000)
print("Public URL:", public_url)

# Run the app
app.run(port=5000)
