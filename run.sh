#!/bin/sh
gunicorn -w 2 -b 0.0.0.0:2083 --certfile /etc/cloudflare/cert.pem --keyfile /etc/cloudflare/key.pem rest_api_server_flask:app
