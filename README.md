# Top 3000 Video Games

Top 3000 Video Games is a web application providing details for top 3000 video games locating in the sales rank as listed in the database.
There is also an e-commerce part in the web application allowing the customers to purchase the listed video games after registered an account in the web application.
This project is developed with Python-based web framework, Django and deployed in Render.

Data shown in the web application is extracted from https://www.kaggle.com/datasets/gregorut/videogamesales produced by GregorySmith by listing out a list of video games with sales in different parts of the world.
This dataset contains a list of video games with sales greater than 100,000 copies. This dataset was generated by a scrape of vgchartz.com.

## Where to view
Web application deployed on Render: https://cs551q-games.onrender.com/
Web application deployed on Codio virtual environment: https://wheelpioneer-bananashock-8000.codio-box.uk/

## Main features
There are two major parts in this web application where one of them is the base part for displaying pages related to the video games and the other part is for e-commerce part allowing customers to purchase the listed video games where authorization and authentication are added.

## Templates in the website
## Models in the web application


top 3000 video games sales
from 1980-2020 with some N/A

Fields include

    Rank - Ranking of overall sales

    Name - The games name

    Platform - Platform of the games release (i.e. PC,PS4, etc.)

    Year - Year of the game's release

    Genre - Genre of the game

    Publisher - Publisher of the game

    NA_Sales - Sales in North America (in millions)

    EU_Sales - Sales in Europe (in millions)

    JP_Sales - Sales in Japan (in millions)

    Other_Sales - Sales in the rest of the world (in millions)

    Global_Sales - Total worldwide sales.


## Basic setup of the virtual environment
A virtual environment with Python version 3.10.7 is created. 
Run the following code in the terminal inside the project folder to setup the required virtual environment.
~~~
pyenv update
pyenv install 3.10.7
pyenv local 3.10.7
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install django
pip install whitenoise
pip install behave
pip install selenium
~~~

For later times for open the previously created virtual environment, run the following code in the project folder.
~~~
source .venv/bin/activate
~~~

## Database resetting
For database regeneration, use the following command after deleting the file db.sqlite3
~~~
python3 manage.py migrate
~~~

To generate migration folder and files, use the following command:
~~~
python3 manage.py makemigrations games
~~~

To run the generated migration, use the following command:
~~~
python3 manage.py migrate games
~~~

## Data parsing
To parse video games-related data rows from csv files in data folder into the database, run the following command:
~~~
python3 manage.py parse_csv
~~~

To create shop-related data with Faker into the database, run the following command:
~~~
python3 manage.py shop_data
~~~

## Starting the server
For starting the server in local machine, run the following command in terminal:
~~~
python3 manage.py runserver
~~~

For starting the server in Codio, run the following command in Codio terminal:
~~~
python3 manage.py runserver 0.0.0.0:8000
~~~

## E-commerce administration
Administration website on Render: https://cs551q-games.onrender.com/admin/
Administration website on Codio virtual environment: https://wheelpioneer-bananashock-8000.codio-box.uk/admin/

### E-commerce accounts
There are three types of accounts in the e-commerce part of the web application: Admin account, Staff account and Customer account.

There are different permissions given to each type of accounts.

#### Admin account

For Admin account, as it is a superuser, all pages are available for the admin users to view and edit.

For the administration website,

Admin account has full access to all views to models or pages using the administration dashboard.
Admin account can add, edit and delete details and permissions for users of the web application such as giving staff status and putting users into staff group using the administration dashboard.
Admin account can also add, edit and delete any instances using the administration dashboard.
Command for creating a superuser:
~~~
python3 manage.py createsuperuser
~~~
Credentials of the Admin account are then asked, which are username, email and password.
Other details for the Admin account such as first name and last name can later be added using the administration dashboard.

For the web application pages,

Other than normal video games purchasing, 
Admin account can also view the dashboard page, basket page, customers page with details of each customer, orders page with details of each order.

#### Staff account

For Staff account, it is an account with staff status and inside a staff group.
The staff status is a Admin-given permission allowing the user to login to the administration website.

For the administration website,

The staff group is a group of chosen viewing permissions given by the Admin.
So staff account users can view all logs, groups, permissions, users, content types, models, sessions using administration dashboard.

For the web application pages,

Other than normal video games purchasing, 
Staff account can also view the dashboard page, basket page, customers page with details of each customer, orders page with details of each order.

#### Customer account

For Customer account, it is an account without any special permission.

Customer account cannot login to the administration website.

For the web application pages,

Customer account can only perform video games purchasing and view basket page.

### Sample accounts created

- Admin account
  - username: admin
  - password: 1234
  - first name: Afirst
  - last name: Alast
  - email: a@b.com


- Staff account
  - username: staff
  - password: 5678abcd
  - first name: Sfirst
  - last name: Slast
  - email: s@b.com


- Customer account
  - username: customer
  - password: 7890efgh
  - first name: Cfirst
  - last name: Clast
  - email: c@b.com

## Maintenance
Latest code commit is automatically pulled from GitHub for Render deployment.
At most two websites can be opened at once from the Render deployed link.
The number of rows of data in the data CSV files can be increased to include more video games in the lower part of the sales rank.
However, the server ability on Render should also be considered when doing such decision.

Generate git log using the following command:
~~~
git log --pretty=format:"%h - %an, %ad : %s" --graph > documents/git-log.txt
~~~
## Testing
PyTest is used for Unit testing and Behave is used for Behavioral-based development (BDD) tests.

### Unit Testing
Django tests for filter function, graph, HTML pages, views, model setup and data input are implemented.

If you change anything in the static folder, please run this command before running the next command:
~~~
python3 manage.py collectstatic
~~~
For running tests, run the following command in the terminal:
~~~
python3 manage.py test games/tests
~~~
### Behave Testing
BDD tests with Given When Then pattern is used for testing the user stories in form of features and scenarios.
All BDD testing related files are placed in features folder.

For running behave, run the following command in the terminal:
~~~
behave
~~~
## Documents
Git-log: documents/git-log.txt

One page design and development report: documents/Ho Pok Nga-CS551Q solo one-page report.pdf
## License
MIT License

Copyright (c) 2023 Cloudy030

## Dependencies
To extract the dependencies of the web application, run the following command:
~~~
pip freeze > requirements.txt
~~~

Due to Render deployment limitation, version numebr of Django and python-dotenv need to be manually changed:
~~~
Django==3.2.18
python-dotenv==0.21.1
~~~

Full dependency list:
~~~
asgiref==3.6.0
async-generator==1.10
attrs==23.1.0
beautifulsoup4==4.12.2
behave==1.2.6
behave-django==1.4.0
certifi==2022.12.7
charset-normalizer==3.1.0
Django==3.2.18
exceptiongroup==1.1.1
Faker==18.4.0
gunicorn==20.1.0
h11==0.14.0
idna==3.4
outcome==1.2.0
packaging==23.1
parse==1.19.0
parse-type==0.6.0
PySocks==1.7.1
python-dateutil==2.8.2
python-dotenv==0.21.1
requests==2.28.2
selenium==4.9.0
six==1.16.0
sniffio==1.3.0
sortedcontainers==2.4.0
soupsieve==2.4.1
sqlparse==0.4.3
tqdm==4.65.0
trio==0.22.0
trio-websocket==0.10.2
urllib3==1.26.15
webdriver-manager==3.8.6
whitenoise==6.4.0
wsproto==1.2.0
~~~
## Documentation
Documentation is placed in the code's comments.
## Background
This is a solo assignment of course Enterprise Software Development (CS551Q) for Master of Information Technology (MScIT) from University of Aberdeen (UoA). It is required to develop a database-driven web application using Django without JavaScript (except graph part) and deploy the developed website with Render.

This is a production of Ho Pok Nga in April 2023.