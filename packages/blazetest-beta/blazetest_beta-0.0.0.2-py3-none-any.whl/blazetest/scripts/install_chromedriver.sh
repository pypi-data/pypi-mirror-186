#!/bin/bash

mkdir -p /usr/bin

# Download and unzip chromedriver
curl -SL https://chromedriver.storage.googleapis.com/`curl -Ls https://chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip > /tmp/chromedriver.zip
unzip /tmp/chromedriver.zip -d /usr/bin
rm /tmp/chromedriver.zip
chown root:root /usr/bin/chromedriver
chmod 0755 /usr/bin/chromedriver
