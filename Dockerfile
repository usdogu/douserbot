FROM python:3
COPY . /douserbot
WORKDIR /douserbot
RUN pip3 install -r requirements.txt
CMD [ "python3", "main.py"]