FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip3 install --upgrade pip \
    -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["neura_app.py"]