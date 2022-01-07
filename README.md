### Flask webapp for training purpose  
Swagger docs for the APIs and MVC pattern for API development
![Screenshot from 2022-01-07 18-29-43](https://user-images.githubusercontent.com/96610585/148547614-f6793bc7-33b0-41e1-9f1b-9617f55dd66b.png)  

### Steps to setup project
    git clone <https://github.com/DhruvikJeavio/pythonflask.git>
    cd pythonflask
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
Further steps:-
    cd src
    export FLASK_APP=server
    flask run

Create your database in PostgreSQL and update the config file for it. Run the migrations
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
