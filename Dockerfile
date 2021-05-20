FROM python:3.8

RUN apt-get update && apt-get install -y \
libbluetooth-dev \
libcap2-bin \
bluetooth \
bluez \
bluez-tools \
blueman

RUN mkdir /app
ADD requirements.txt /app
WORKDIR /app

ENV PYTHONPATH $PYTHONPATH:/app

RUN pip install -r requirements.txt

ADD . /app

STOPSIGNAL SIGHUP

RUN setcap 'cap_net_raw,cap_net_admin+eip' "$(readlink -f "$(which python3)")"

CMD ["python", "main.py"]
