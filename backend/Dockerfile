FROM python:3.11.3-alpine
WORKDIR /usr/src/backend

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
#RUN ./app/checkenv.sh

# Establecer la orden de ejecución predeterminada
#ENTRYPOINT ["./app/checkenv.sh"]
CMD ["uvicorn", "app.main:app", "--reload","--host", "0.0.0.0", "--port", "8080"]