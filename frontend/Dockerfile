FROM node:18-alpine
WORKDIR /usr/src/app
COPY ./app/package.json .
RUN npm i
COPY ./app .
CMD ["npm", "run", "dev"]