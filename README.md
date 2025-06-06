# DoS-in-Python-Simulate-the-Storm-Build-the-Shield

Workshop proposal: GHC2025-Workshop Proposal.pdf

Google Doc link: https://docs.google.com/document/d/1rECbX_KT-Lfkcume07x8s4zDjgEL3EmPJy3kbc8FBXU/edit?usp=sharing

_________________________________________________________________________________________________________________________________________
Flask app runs on localhost (127.0.0.1), and only a local machine can reach it. Hence to simulate requests from the "outside world" (e.g., for testing DoS attack scenario), ngrok creates a public URL that tunnels into the local Flask app.
_________________________________________________________________________________________________________________________________________
Prerequisites:
1. Create login to Ngrok (or similar): This will help to craete a dummy web app server that we will launch DDoS on.

2. pip install flask flask-limiter pyngrok

- flask: A lightweight web framework for building web applications and APIs in Python.
- flask-limiter: A Flask extension for rate limiting incoming requests to your app.
- pyngrok: Python wrapper for ngrok, which exposes local servers to the public internet through secure tunnels

3. ngrok config add-authtoken #YOUR_TOKEN
- ngrok will associate tunnels with individual account and provide access to features like more connections, and rate limits.


_________________________________________________________________________________________________________________________________________
Scripts execution order: 

1. FlaskWebServer.py
  - Runs a Flask web app locally.
  - Limits traffic to 5 requests per minute per IP.
  - Opens a public link (via ngrok) so the app is reachable from the internet.
  - Access the web app without deploying it and testing rate-limiting.
    
2. DoS_Sim.py
- Send high number of HTTP requests to a ngrok URL using multithreading.
- Prints the HTTP status code.
  
3. RateLimit.py
 - Flask web server that includes basic DoS protection using request rate limiting via the flask-limiter library.
