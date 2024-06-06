# Stage 1: Install dependencies
FROM python:3.12-alpine3.19 AS builder

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install gunicorn

RUN pip install -r requirements.txt

# Stage 2: Copy application and reduce image size
FROM alpine:latest

WORKDIR /app

COPY --from=builder . .

COPY . .

RUN apk add --no-cache nodejs npm

RUN npm install

CMD [ "gunicorn", "-b", "0.0.0.0:$PORT", "allLinks.service:app"]