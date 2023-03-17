# Dart Takehome Project

Welcome to the Dart takehome project! Thanks for giving it a look. This is a chance for you to demonstrate your frontend, backend, or full stack coding skills in a practical context. It should take no longer than three hours, and you can do it whenever works for you--just submit it when you are done! We guarantee detailed feedback on your solution so hopefully it will be worth your time.


## Introduction

This project is a very scaled-down version of the actual Dart 🎯 application! It's quite a bit like what we work on all day, every day, on the Dart team. That means the work that you do on this project is pretty similar to real work you would do on Dart. That way you can get a sense for what the job might actually be like and we can get a sense for all of the great work that you can do.

The project consists of a functional backend and a static frontend; your goal will be to extend it in a few ways based on what kind of work you do.

At a high level, you should
1. Get the project running and understand what's happening
2. Add some improvements based on the backlog of ideas in this file
3. Submit the project according to the steps below

Please spend no more than three hours on the project overall. We know that there is a lot to understand here, and the project is inherently very open-ended, so we do not expect you to 'complete' it. In fact, there is no such thing as completing it. Just do your best work in the time that you have.

Feel very free to use any resources online or offline, including any packages or libraries, but excluding other people (i.e. do not get help from a friend). Additionally, please do not share or post either this source or your solution.

If any of this is confusing or you have any clarifying questions, reach out to zack@itsdart.com at any time.


## Setup

1. Make sure you have `python` and `pip` installed and working; [this guide might help](https://packaging.python.org/en/latest/tutorials/installing-packages/)
2. Consider also using a virtual environment for Python
3. Install the backend dependencies for this project with `pip install -r requirements.txt`


## Usage

1. Run the backend with `python manage.py runserver`
2. Check out the current static page at http://localhost:8000
3. Run the backend tests with `python manage.py test backend`


## Improvements

Now that you have the project running, time for the fun part! There are an lot of improvements possible but listed here are some of the specific things that would be best. We recognize this is very open-ended and that's intentional: this is almost like a backlog where you can pick the tasks that you will do, and it's a lot like what actually working at Dart will be like.

Again, remember that we don't expect you to do all of these--just pick a few that make sense and that you can accomplish well during the time you have.

#### Frontend
First and foremost, reimplement the static frontend page that exists currently by using Vue (ideally) or React (if you don't know Vue yet). You can GET the data needed for this page from `/api/tasks/list` as long as you are running the backend server.

Once that's done, you could
1. Enable editing the title field and post those edits to `/api/tasks/edit`, which isn't implemented yet
2. Add an in-page refresh button that also tells you how long it's been since the data were last loaded
3. Make a page specifically for an individual task that you can get to by clicking a row
4. Restyle the project a bit with TailwindCSS--don't worry about the design
5. Add some frontend tests using your framework of choice
6. Add documentation to your changes or to existing work
7. Fix any bugs you find

#### Backend
1. Write a Python script that reads the additional tasks from the `extra_tasks.csv` and puts them in the DB
2. Add a new enum field to the task model called 'status' and make sure it shows up on the frontend
3. Implement `/api/tasks/edit` in a reasonable way to allow editing, particularly of the title field
4. Dockerize the application so that it can be run anywhere
5. Deploy the app to the free tier of Heroku
6. Extend the existing tests to more fully test different behaviors of the server
7. Add documentation to your changes or to existing work
8. Fix any bugs you find

Feel free to be creative and add other features you think make sense!


## What we're looking for

1. Clarity: does your report clearly explain what you did and why
2. Correctness: does the code do what it's supposed to do
3. Quality: is the code written legibly, with tests and comments as appropriate
4. UX: is the user experience understandable (including on the backend, where the user might be a developer)
5. Technical: are the architecture and libraries appropriate


## Submission

1. Make sure that all of your work is in this folder
2. Record a summary of everything you've done in a top-level file called `report.md` (`.txt`, `.doc`, or other common file extension is also fine but definitely name the file `report`--you could even do a screen recording and submit `report.mp4` if you like)
    1. Be sure to explain all of your work so that we don't miss anything
    2. Give us very clear instructions on how to run your new code
    3. Please comment on what challenges you had and what you liked/didn't like about this project
3. Zip your project by running `zip [your_name]_dart_takehome_submission.zip -r dart_takehome` (or a similar command) in your workspace
4. Email the zip to zack@itsdart.com

We hope this was interesting for you, and maybe even fun!
