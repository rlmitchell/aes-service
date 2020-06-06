FROM python:2.7
WORKDIR /opt
COPY requirements.txt /opt 
RUN pip install -r requirements.txt
