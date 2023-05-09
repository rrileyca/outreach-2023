#!/bin/bash
openssl req -x509 -nodes -days 365 -subj "/C=CA/ST=QC/O=Company, Inc./CN=mydomain.com" -addext "subjectAltName=DNS:localhost" -newkey rsa:2048 -keyout ./nginx-selfsigned.key -out ./nginx-selfsigned.crt