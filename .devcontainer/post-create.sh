#!/usr/bin/bash

cp -r /mnt/config/.gitconfig ~/.gitconfig
cp -r /mnt/config/.ssh ~/

uv sync --dev
