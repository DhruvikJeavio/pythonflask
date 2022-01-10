### Flask webapp for training purpose  
Swagger docs for the APIs and MVC pattern for API development
![Screenshot from 2022-01-10 10-23](https://user-images.githubusercontent.com/96610585/148719984-cbc18c13-3de3-4966-9310-981c8472d214.png)

### Steps to setup project
    git clone <https://github.com/DhruvikJeavio/pythonflask.git>
    cd pythonflask
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
### Create your database in PostgreSQL and update the config file for it. Run the migrations:-  
    cd src  
    export FLASK_APP=server
    flask run
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
