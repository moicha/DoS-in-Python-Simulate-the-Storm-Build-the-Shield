# DDoS-in-Python-Simulate-the-Storm-Build-the-Shield
Scripts to explore both sides of cybersecurity using Python coding.


Flask app runs on localhost (127.0.0.1), and only a local machine can reach it. Hence too simulate requests from the "outside world" (e.g., for testing DDoS attack scenario), ngrok gives creates a public URL that tunnels into the local Flask app.
_________________________________________________________________________________________________________________________________________
Prerequisites:
1. Create login to Ngrok (or similar): This will help to craete a dummy web app server that we will launch DDoS on.

2. pip install flask flask-limiter pyngrok

- flask: A lightweight web framework for building web applications and APIs in Python.
- flask-limiter: A Flask extension for rate limiting incoming requests to your app.
- pyngrok: Python wrapper for ngrok, which exposes local servers to the public internet through secure tunnels

3. ngrok config add-authtoken #YOUR_TOKEN
- ngrok will associate tunnels with individual accountand provide access to features like more connections, and rate limits.



