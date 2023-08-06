#!/bin/bash

# Check if x11vnc is installed
if [ ! -x "$(command -v x11vnc)" ]; then
  # Install x11vnc if it is not installed
  echo "x11vnc is not installed. Installing it now..."
  # Use your system's package manager to install x11vnc
  # For example, on Ubuntu/Debian systems:
  sudo apt-get install x11vnc -y
  # Check if x11vnc was successfully installed
  if [ -x "$(command -v x11vnc)" ]; then
    echo "x11vnc was successfully installed."
    # Send a notification to the user
    notify-send "x11vnc installed" "x11vnc was successfully installed on your system."
  else
    echo "Failed to install x11vnc. Please try again."
    # Send a notification to the user
    notify-send "x11vnc installation failed" "Failed to install x11vnc on your system. Please try again."
  fi
else
  echo "x11vnc is already installed."
  # Send a notification to the user
fi
nohup x11vnc -display $DISPLAY -autoport 5905 &
IP_ADDR=$(ip addr | grep 'inet' | grep -v 'inet6' | grep -v '127.0.0.1' | head -n 1 | awk '{print $2}' | cut -d '/' -f 1)
noVNCurl=$1

vnc="cd $noVNCurl/sh/VNC/noVNC-1.3.0"
$vnc
sudo chmod 777 utils/novnc_proxy
utils/novnc_proxy --vnc $IP_ADDR:5905
