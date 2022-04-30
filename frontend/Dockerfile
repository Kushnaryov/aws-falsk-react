# syntax=docker/dockerfile:1
FROM node:18-alpine3.14
# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH
WORKDIR /frontend

COPY ./package.json .
COPY ./package-lock.json .

RUN npm install
RUN npm install react-scripts 

COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]