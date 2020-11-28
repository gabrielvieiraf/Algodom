#!/bin/sh
gunicorn rest_api_server_flask:app -b :5002
