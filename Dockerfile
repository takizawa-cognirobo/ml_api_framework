FROM tensorflow/tensorflow:latest-gpu-py3

WORKDIR /tmp
RUN apt-get update
RUN apt-get install python3 python3-pip -y

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt

RUN mkdir /tmp/.jupyter
COPY jupyter_notebook_config.py /tmp/.jupyter/

WORKDIR /home