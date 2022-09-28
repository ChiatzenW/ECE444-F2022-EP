# Education_Pathways

This is a modified version of the previous Assignment1-template.

Hardcodings are removed.


## How to run it locally

+ Enter the repo directory
+ Create a virtual environment and activate it: https://flask.palletsprojects.com/en/2.2.x/installation/
```
# Windows
py -3 -m venv venv
venv\Scripts\activate
```
+ Install dependencies
```
pip install -r requirements.txt
```
+ Enter the Education_Pathways/ directory, run the backend
```
flask --app index --debug run
```
+ Enter the frontend/ directory
+ Change the BaseURL to `localhost:5000`
```
# Education_Pathways/frontend/src/api.js
export default axios.create({
//  baseURL: "https://a1-docker.herokuapp.com/" -- baseURL for deployment
   baseURL: "http://localhost:5000/"
});
```
+ Build and run the frontend:
```
npm run build
npm start
```
+ Then you will see the application at `localhost:3000`


## How to deploy

TBA