FROM node:18
WORKDIR /app/frontend

COPY package.json package-lock.json ./
RUN npm install 
RUN npm install react-scripts -g
COPY . ./
EXPOSE 3000