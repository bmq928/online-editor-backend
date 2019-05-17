FROM revotech2017/wi-python-node:latest

ENV PATH /usr/local/bin:$PATH

RUN pip install requests

COPY ./wilibs /root/.local/lib/python3.6/site-packages/wilibs
COPY ./sitecustomize.py /usr/lib/python3.6/

#######################################
# app

WORKDIR /app
ENV NODE_ENV production
ENV PYTHON_PROJECT_STORAGE /storage
ENV PYTHON_LOG_PATH ./logs
ENV PYTHON_PORT 3000
ENV PYTHON_CLIENT_DOMAIN localhost:8080
ENV PROJECT_RELATED_ROOT_URL https://api-1.i2g.cloud
ENV USER_RELATED_ROOT_URL https://users.i2g.cloud

COPY . .
RUN npm i --only=prod &&\
  mkdir /storage &&\
  mkdir logs &&\
  touch logs/activities.log &&\
  touch logs/errors.log &&\
  touch logs/request.log

CMD ["npm", "start"]
