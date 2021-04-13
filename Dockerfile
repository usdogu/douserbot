FROM python:3
COPY . /douserbot
WORKDIR /douserbot
RUN pip3 install -r requirements.txt
ARG SESSION
ENV STRING_SESSION=$SESSION
CMD [ "python3", "main.py"]
