# pull official base image
FROM node:13.12.0-alpine

EXPOSE 3000
# set working directory
WORKDIR /usr/webapp

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./

# add app
COPY . ./

RUN yarn

# start app
CMD ["npm", "start"]
