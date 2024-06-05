FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip nodejs npm

COPY . /

RUN npm install

RUN pip install -r requirements.txt

CMD ["python", "/allLinks.service.py"]