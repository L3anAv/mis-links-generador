FROM alpine:3.15

RUN apk add --no-cache nodejs npm python3 py3-pip

COPY . /

RUN npm install

RUN pip install -r requirements.txt

CMD ["python", "/allLinks.service.py"]