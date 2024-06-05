# Stage 1: Install dependencies
FROM python:3.12-alpine3.19 AS builder

RUN apk add --no-cache nodejs npm

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Stage 2: Copy application and reduce image size
FROM alpine:latest

WORKDIR /app

COPY --from=builder . .

RUN npm install

CMD ["python3", "/allLinks.service.py"]