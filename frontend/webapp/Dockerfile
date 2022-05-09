FROM node:18.1.0

WORKDIR /usr/frontend/webapp

# ENV COPIED FROM https://gitlab.unimelb.edu.au/resplat-cloud/uom-cloud-docs/blob/c59fcf93639f6121d12de3fd2d9786b73b3a47a7/docs/guides/using_uom_internal_network.md
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy="localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.unimelb.edu.au,.cloud.unimelb.edu.au"
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/

EXPOSE 3000

COPY package.json ./
COPY package-lock.json ./
RUN yarn

COPY . ./

CMD ["npm", "start"]