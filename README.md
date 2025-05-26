# DDoS-in-Python-Simulate-the-Storm-Build-the-Shield
Scripts to explore both sides of cybersecurity using Python coding.

Prerequisites:

Create login to Ngrok (or similar): This will help to craete a dummy web app server that we will launch DDoS on.

!pip install flask flask-limiter pyngrok

- flask: A lightweight web framework for building web applications and APIs in Python.
- flask-limiter: A Flask extension for rate limiting incoming requests to your app.
- pyngrok: Python wrapper for ngrok, which exposes local servers to the public internet through secure tunnels

!ngrok config add-authtoken #YOUR_TOKEN
- ngrok will associate tunnels with individual accountand provide access to features like more connections, and rate limits.
