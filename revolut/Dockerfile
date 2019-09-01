FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG FLASK_APP=server/app.py

COPY . .

CMD [ "python", "-m", "flask", "run" ]
