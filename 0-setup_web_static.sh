#!/usr/bin/env bash
# Configuration

dpkg -s nginx &> /dev/null  && sudo apt-get update && sudo apt-get -y install nginx for success 
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Testing Nginx" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "45i \\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart