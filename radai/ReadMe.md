# Pig Latin Translator

## Backend 
- Using fastapi framework for python
- Docker for deployment (included DockerFile)
### Instructions
- Build the docker image
```
docker build -t <image-name>:latest .
```
- Run the docker image
```
docker run -d -p 8000:8000 <image-name>:latest
```

## Frontend
- Using ReactJS
- Using Material-UI for asthetics
### Instructions
- install dependencies
```
npm install
```
- run the app
```
npm start
```
- if you want to run the app in production mode or build the app for production
```
npm run build
```
