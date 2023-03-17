# Dart App Report

## FrontEnd
1. Implemented the frontend using React please find it in ./dart_frontend/
2. Implemented the refresh button along with time elasped since last update and the in-page editing of the title field 
3. Implemented the individual task page
4. Restyled the project using TailwindCSS to some extent

## BackEnd
1. Implemented the /api/tasks/edit endpoint to allow editing of the title field
2. Added status field to the task model and make the migration
3. Added the extra_tasks.csv to the database using the load_scipts.py script integrated with django-extensions
4. Dockerized the application along with docker-compose.yml. Please find it in the root folder. 
5. All dependencies are installed using pip. Please find the requirements.txt in the ./dart_takehome folder.

## Running the app
Please run the following command in the root folder of the project
docker-compose up