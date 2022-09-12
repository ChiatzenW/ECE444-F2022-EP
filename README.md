# Assignment 1: Education Pathway

This repository host the source code for Education Pathway project. You can view the online deployed version [here](https://assignment-1-starter-template.herokuapp.com/). We are using this repo as a starting point for assignment 1.


This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app) for frontend, and [Flask-tdd](https://github.com/mjhea0/flaskr-tdd) for backend.


## 0. Before the project

Make you have all the prerequisites installed
* Git/GitHub Desktop
* Python (python-3.10.6)
* nodejs



## 1. Clone the repository to your local machine
```sh
$ git clone https://github.com/ECE444-2022Fall/Assignment_1_starter_template.git
```
## 2. To run the app in development

First, to install the nodejs modules needed, run
```sh
$ npm install
```
then to start the app in development mode
```sh
$ npm start
```
## 3. To build the app for production to the `build` folder.
```sh
$ npm run build
```
## 4. Deploy the project
   
We use Heroku to deploy the project online. To do this, first [sign up](https://signup.heroku.com/) for a Heroku account,  and then install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).


Next, install a production-grade WSGI web server called [Gunicorn](http://gunicorn.org/):

```sh
$ pip install gunicorn==20.0.4
```

Create a [Procfile](https://devcenter.heroku.com/articles/procfile) in the project root:

```sh
$ touch Procfile
```

And add the following code:

```sh
web: gunicorn project.app:app
```

Create a *requirements.txt* file to specify the external dependencies that need to be installed for the app to work:

```sh
$ touch requirements.txt
```

Add the requirements:

```
Flask==2.1.1
gunicorn==20.0.4
pytest==7.1.2
```

Create a *.gitignore* file in the project root:

```sh
$ touch .gitignore
```

And include the following files and folders (so they are not included in version control):

```sh
env
*.pyc
*.DS_Store
__pycache__
test.db
```

To specify the correct Python runtime, add a new file to the project root called *runtime.txt*:

```
python-3.10.4
```

Add a local Git repo:

```sh
$ git init
$ git add -A
$ git commit -m "initial"
```

Deploy to Heroku:

```sh
$ heroku create myapp-unique-name
$ git push heroku main
```
Then to view the deployed app online, run 

```sh
$ heroku open
```
or go to your Heroku account and check your the url of your deployed app. (`https://myapp-unique-name.herokuapp.com/`)