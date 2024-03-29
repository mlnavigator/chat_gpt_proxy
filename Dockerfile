FROM ubuntu:22.04
LABEL authors="mlnavigator"

RUN apt update
RUN apt install -y nano && apt install -y python3.10 && apt install -y python3-venv && apt install -y python3-pip

ADD . /chat_gpt_proxy

RUN python3.10 -m pip install -r /chat_gpt_proxy/requirements.txt
EXPOSE 9081

ENTRYPOINT ["/bin/bash", "/chat_gpt_proxy/run.sh"]