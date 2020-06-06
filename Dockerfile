FROM python:2.7
WORKDIR /opt
COPY requirements.txt /opt 
RUN pip install -r requirements.txt
COPY *.ini /opt/
COPY *.py /opt/
