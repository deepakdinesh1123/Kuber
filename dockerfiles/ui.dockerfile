FROM node:current-alpine


COPY ui /usr/src/app
WORKDIR /usr/src/app
RUN npm install
ENTRYPOINT [ "npm", "run", "dev" ]
