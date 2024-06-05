FROM alpine:3.15

RUN apk add --no-cache nodejs npm python3 python3-pip

WORKDIR /app

COPY . app

RUN npm install

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "allLinks.service.py"]
