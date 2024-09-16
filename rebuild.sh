#!/bin/bash
echo "start"
docker stop chat_gpt_proxy_dc
docker rm chat_gpt_proxy_dc
docker rmi chat_gpt_proxy_dc
docker build -t chat_gpt_proxy_dc .
docker run -d --restart=always -e ACCESS_KEY='123456' -p 9081:9081 --name=chat_gpt_proxy_dc chat_gpt_proxy_dc
# docker run -e ACCESS_KEY='123456' -e VERBOSE='1' -p 9081:9081 -it --name=chat_gpt_proxy_dc chat_gpt_proxy_dc
echo "finished - run container chat_gpt_proxy_dc"