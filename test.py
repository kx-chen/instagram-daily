#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("kaiusesthis", "password899")
InstagramAPI.login()  # login

photo_path = 'onion.jpg'
caption = "Staging!"
InstagramAPI.uploadPhoto(photo_path, caption=caption)