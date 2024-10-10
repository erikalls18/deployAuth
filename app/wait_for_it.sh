#!/bin/bash

python3 /usr/src/app/db/models/user.py
uvicorn main:app --reload --host 0.0.0.0
