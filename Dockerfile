FROM alpine:3.15

RUN apk add --no-cache nodejs npm python3 py3-pip

COPY . /

RUN npm install -g

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/allLinks.service.py"]