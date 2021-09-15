#!/usr/bin/env bash

sudo apt-get update

sudo apt install -y software-properties-common

sudo apt install -y default-jre
sudo apt install -y default-jdk

# install python
sudo apt-get install python3-dev python3-pip -q -y
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

sudo apt install -y python3.8-venv
sudo apt install -y python3-venv

