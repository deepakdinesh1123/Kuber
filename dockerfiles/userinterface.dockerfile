FROM node:current-alpine

COPY userinterface /usr/src/app
WORKDIR /usr/src/app
RUN npm install
RUN npm run build
EXPOSE 4000
CMD ["npm", "start"]
