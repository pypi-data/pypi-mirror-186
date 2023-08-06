#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:59:20 2023

@author: akshay
"""

import subprocess
#subprocess.run(["python","--version"])

def launch(port="localhost:8000",workers="4"):
    subprocess.run(["gunicorn","main:server","-b",port,"-w",workers])

#launch()