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

Details of the video games are displayed in tabular form.
By clicking onto particular video game name, year, platform, genre, or publisher, details page of the selected parameter will be displayed.

Filtering function is implemented in two parts of the web application with different criteria.
- Video games list
  - Platform
  - Year
  - Genre
  - Publisher
- Comparison
  - Video Game rank

Data visual components are implemented in the web application.
- Dashboard pie graph for showing the proportion of registered account types
- Dashboard bar graph for showing the number of orders made by each customer
- Comparison bar graph for comparing sales of two video games

Authentication system is implemented in the web application.
- Login and registration system
- Customer accounts, staff accounts, admin accounts

A horizontal navigation bar is shown in the top of every web page allowing users to navigate to the respective pages.
Links are embedded into the data shown in the table columns.

For the e-commerce part, users can add the video games into the cart and can only purchase the video games after logged into the system.
Users can register if they do not have an account previously.

Using customer accounts, customers can only add video games into the cart and purchase them.

Using staff and admin accounts, staffs and admin can view all e-commerce related web pages including dashboard, customer related and order related pages other than the normal purchase pages.

Django administration system is activated so users using staff and admin accounts can login.
Staff account users are only allowed to view in the administration website.
Admin account users can perform every actions with all permissions in the administration website.

## Templates in the website
There are total twenty three templates in this web application.
These 23 templates can be grouped in two major parts which are video games related models and e-commerce related models.

### Video games related
First, there are twelve templates which are video games related.

These templates are located in:
~~~
 cs551q_solo/games/templates/games/base
~~~
All pages have respective web links linked to the corresponding web pages.

- Main Pages
  - Video Games list (index.html)
    - This is a base page for the following 2 html for showing the video game list.
    - Showing full list of video games with 3000 entries (game_full_list.html)
    - Showing filtered list of video games with users' inputted parameters (game_filter_list.html)
  - Year (year.html)
    - This is a page for showing the list of years that the video games are released in.
  - Genre (genre.html)
    - This is a page for showing the list of genres with their descriptions for the video games.
  - Platform (platform.html)
    - This is a page for showing the list of platforms with the respective images for the video games to be published on.
  - Publisher (publisher.html)
    - This is a page for showing the list of publishers publishing the video games.
  - Comparison Page (compare.html)
    - This is a page for users to compare between 2 video games of their choice in form of tabular data and bar graph for showing sales data.

- Detail pages
  - Video Game detail page (game_detail.html)
    - This is a page for showing the details of the chosen video games. There is also an add to cart link at the bottom of the page.
  - Year Game page (year_game.html)
    - This is a page for showing the list of video games with the selected year of release.
  - Genre Game page (genre_game.html)
    - This is a page for showing the list of video games with the selected genre with the description.
  - Platform Game page (platform_game.html)
    - This is a page for showing the list of video games with the selected platform with the platform image.
  - Publisher Game page (publisher_game.html)
    - This is a page for showing the list of video games with the selected publisher.

### E-commerce related
Second, there are ten templates which are e-commerce related.

There are three sub-parts for the e-commerce templates which are stored in two separate folders.

For base part and e-commerce part, the templates are located in:
~~~
cs551q_solo/games/templates/games/shop
~~~

For registration part, the templates are located in:
~~~
cs551q_solo/games/templates/registration
~~~
#### Base part
There is one template in the base part.
- Base header, navigation bar for e-commerce related templates (base.html)
  - This is a base page for all e-commerce related templates. The showing of web page is related to the account permissions. Customer accounts can only see the basket page where staff accounts and admin accounts can see all web pages including basket, dashboard, customer pages and orders pages.

#### E-commerce part
There are eight templates in the e-commerce part.

These two templates are accessible to everyone using the web application including users who are not logged into the system:
- Basket (basket.html)
  - This is a basket page for all users of that session showing the video games added into their basket.
- Register page (signup.html)
  - This is a registration page for all users to register a new account if they do not have one.

All remaining templates access in e-commerce part require account login.
The number of pages accessible depend on the type of accounts the user is using.

This template is accessible to all logged-in users
- Purchase (purchase.html)
  - This is a purchase page for logged-in users to input their card details in to do the payment action for the video games added in the cart in that session.

Following templates are only accessible to staff accounts and admin accounts:
- Dashboard (dashboard.html)
  - This is a dashboard page showing the graph displaying the proportion of registered account types.
- Customer list (customer_list.html)
  - This is a customer list page showing all users who have an account in the web application including staff accounts and admin accounts holders.
- Customer detail (customer_detail.html)
  - This is a customer detail page showing all details of the chosen user and displaying the order IDs which has been purchased by this user. By clicking into this page, the current user account will be switch to the viewing customer's account.
- Order list (order_list.html)
  - This is a order list page showing all orders made by all users according to time sequence.
- Order detail (order_detail.html)
  - This is a order detail page showing all video games with the respective quantity in the chosen order. By clicking into this page, the current user account will be switch to the viewing customer's account.

#### Registration part
There are one template in the registration part.
- Login (login.html)
  - This is the login page for the users to input their username and password to login. If the user does not have an account, a new account can be registered using the Register link.

## Models in the web application
There are total nine models in this web application.
These 9 models can be grouped in two major parts which are video games related models and e-commerce related models.

### Video games related
First, there are five class objects which are video games related.

- Year
  - This table refers to the years where the video games are released.
  - According to the database obtained, this table consist from 1980 to 2020 with some N/A which do not have any data
  - column name: year_no

- Genre
  - This table refers to the genres and the respective genre descriptions where the video games belong to.
  - column name: genre_name, genre_description

- Platform
  - This table refers to the platform with the respective platform image url where the video games have been published onto.
  - column names: platform_name, url

- Publisher
  - This table refers to the publisher of each video game.
  - column name: publisher_name

- Game
  - This table refers to the video games with top 3000 sales with the sales data from different parts of the world.
  - This table is linked to the other tables in this video games related part using primary and foreign key pair.
  - For the columns meaning in this table:
    - rank - Ranking of overall sales from 1 to 3001 where 654th data is lost
    - name - Name of video game
    - platform - Platform of the video game release (i.e. PC, PS4, etc.)
    - year - Year of the video game's release
    - genre - Genre of the video game
    - publisher - Publisher of the video game
    - na_sales - Sales in North America (in millions)
    - eu_sales - Sales in Europe (in millions)
    - jp_sales - Sales in Japan (in millions)
    - other_sales - Sales in the rest of the world (in millions)
    - global_sales - Total worldwide sales (in millions)
    - price - Randomly generated price of the video game
  - column names:rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales, price

### E-commerce related
Second, there are four class objects which are e-commerce related.

- Cart
  - This table refers to the added items in cart for the customer of current session.
  - This table is linked to Game table with primary and foreign key pair.
  - column names: game, quantity, created_date

- Customer
  - This table refers to the users saved as customer for easy usage of Django components.
  - All users' information will be saved in this table, including admin accounts, staff accounts and customer accounts.
  - column names: user, user_type, address, created_date

- LineItem
  - This table refers to the different video games added into the cart.
  - This table is linked to Game table, Cart table and Order tables with primary and foreign key pair.
  - column names: quantity, game, cart, order, created_date

- Order
  - This table refers to the time when customers place the order.
  - This table is linked to Customer table with primary and foreign key pair.
  - column names: customer, created_date

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
In the shop-related data generated, Faker and Random are used to create customers, carts, orders and lineitems.
In this web application, admin and staff accounts can also order and purchase video games through the web application.
So all registered users using any account types can place random numbers of orders  and purchase random number of video games.

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
Other details for the Admin account such as first name and last name, especially user_type can later be added using the administration dashboard.

For the web application pages,

Other than normal video games purchasing, 
Admin account can also view the dashboard page, basket page, customers page with details of each customer, orders page with details of each order.

#### Staff account

For Staff account, it is an account with staff status and inside a staff group.
The staff status is a Admin-given permission allowing the user to login to the administration website.

For the administration website,

The staff group is a group of chosen viewing permissions given by the Admin.
So staff account users can view all logs, groups, permissions, users, content types, models, sessions using administration dashboard.
The staff account status and staff group are manually added in the administration website by an admin user.

For the web application pages,

Other than normal video games purchasing, 
Staff account can also view the dashboard page, basket page, customers page with details of each customer, orders page with details of each order.

#### Customer account

For Customer account, it is an account without any special permission.

Customer account cannot login to the administration website.

For the web application pages,

Customer account can only perform video games purchasing and view basket page.

### Sample accounts created
These sample accounts are manually created and are not generated by running the shop_data.py
Permissions settings is done manually and have been set for all of the following accounts.

All manual changes will be removed once the shop_data.py is run.

- Admin account
  - username: admin
  - password: 1234
  - first name: Afirst
  - last name: Alast
  - email: a@b.com


- Staff account
  - username: staff
  - password: 5678
  - first name: Sfirst
  - last name: Slast
  - email: s@b.com


- Customer account
  - username: customer
  - password: 7890
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
Django tests for filter function, graph, HTML pages, views, login, model setup and data input are implemented.

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