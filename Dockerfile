FROM python:3.8

#establce un directorio dentro del contenedor
WORKDIR /usr/src/app


COPY requirements.txt .
RUN pip install -r requirements.txt


 

#Copia todos los archivos de la carpeta app al directorio de trabajo 
#COPY app/* .
COPY app/ /usr/src/app/

RUN pip list

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]
#ENTRYPOINT ./run.sh
