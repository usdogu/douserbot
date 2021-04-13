FROM python:3
COPY . /douserbot
WORKDIR /douserbot
RUN pip3 install -r requirements.txt
ARG SESSION
ARG API_ID
ARG API_HASH
ENV STRING_SESSION=${SESSION}
ENV API_ID=${API_ID}
ENV API_HASH=${API_HASH}
CMD ["python3", "main.py"]
