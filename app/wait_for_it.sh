#!/bin/bash




#python3 /usr/src/app/create_data.py
python3 /usr/src/app/db/models/user.py
uvicorn main:app --reload --host 0.0.0.0
#echo 'Hello World!'


# TO IMPLMENT !
#https://docs.docker.com/compose/how-tos/startup-order/
#https://medium.com/@arturocuicas/fastapi-with-postgresql-part-1-70a3960fb6ee
#https://medium.com/@kevinkoech265/a-guide-to-connecting-postgresql-and-pythons-fast-api-from-installation-to-integration-825f875f9f7d
#https://www.timescale.com/blog/when-and-how-to-use-psycopg2/
#https://www.youtube.com/watch?v=gQTRsZpR7Gw
#https://www.descope.com/learn/post/jwt