# AirBnB clone - Web framewor

### Install Flask

![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png)

* * * * *

Tasks
-----

 Done?\
Help

#### 0\. Hello Flask! mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display "Hello HBNB!"
-   You must use the option `strict_slashes=False` in your route definition

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `0-hello_route.py, __init__.py`

Check your code?Get a container

 Done!\
Help

#### 1\. HBNB mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display "Hello HBNB!"
    -   `/hbnb`: display "HBNB"
-   You must use the option `strict_slashes=False` in your route definition

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `1-hbnb_route.py`

Check your code?Get a container

 Done!\
Help

#### 2\. C is fun! mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display "Hello HBNB!"
    -   `/hbnb`: display "HBNB"
    -   `/c/<text>`: display "C " followed by the value of the `text` variable (replace underscore `_`symbols with a space )
-   You must use the option `strict_slashes=False` in your route definition

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `2-c_route.py`

Check your code?Get a container

 Done!\
Help

#### 3\. Python is cool! mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display "Hello HBNB!"
    -   `/hbnb`: display "HBNB"
    -   `/c/<text>`: display "C ", followed by the value of the `text` variable (replace underscore `_`symbols with a space )
    -   `/python/(<text>)`: display "Python ", followed by the value of the `text` variable (replace underscore `_` symbols with a space )
        -   The default value of `text` is "is cool"
-   You must use the option `strict_slashes=False` in your route definition

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `3-python_route.py`

Check your code?Get a container

 Done!\
Help

#### 4\. Is it a number? mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display "Hello HBNB!"
    -   `/hbnb`: display "HBNB"
    -   `/c/<text>`: display "C ", followed by the value of the `text` variable (replace underscore `_`symbols with a space )
    -   `/python/(<text>)`: display "Python ", followed by the value of the `text` variable (replace underscore `_` symbols with a space )
        -   The default value of `text` is "is cool"
    -   `/number/<n>`: display "`n` is a number" **only** if `n` is an integer
-   You must use the option `strict_slashes=False` in your route definition

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `4-number_route.py`

Check your code?Get a container

 Done!\
Help

#### 5\. Number template mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display "Hello HBNB!"
    -   `/hbnb`: display "HBNB"
    -   `/c/<text>`: display "C ", followed by the value of the `text` variable (replace underscore `_`symbols with a space )
    -   `/python/(<text>)`: display "Python ", followed by the value of the `text` variable (replace underscore `_` symbols with a space )
        -   The default value of `text` is "is cool"
    -   `/number/<n>`: display "`n` is a number" **only** if `n` is an integer
    -   `/number_template/<n>`: display a HTML page **only** if `n` is an integer: 
        -   `H1` tag: "Number: `n`" inside the tag `BODY`
-   You must use the option `strict_slashes=False` in your route definition

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `5-number_template.py, templates/5-number.html`

Check your code?Get a container

 Done!\
Help

#### 6\. Odd or even? mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display "Hello HBNB!"
    -   `/hbnb`: display "HBNB"
    -   `/c/<text>`: display "C ", followed by the value of the `text` variable (replace underscore `_`symbols with a space )
    -   `/python/(<text>)`: display "Python ", followed by the value of the `text` variable (replace underscore `_` symbols with a space )
        -   The default value of `text` is "is cool"
    -   `/number/<n>`: display "`n` is a number" **only** if `n` is an integer
    -   `/number_template/<n>`: display a HTML page **only** if `n` is an integer: 
        -   `H1` tag: "Number: `n`" inside the tag `BODY`
    -   `/number_odd_or_even/<n>`: display a HTML page **only** if `n` is an integer: 
        -   `H1` tag: "Number: `n` is `even|odd`" inside the tag `BODY`
-   You must use the option `strict_slashes=False` in your route definition

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `6-number_odd_or_even.py, templates/6-number_odd_or_even.html`

Check your code?Get a container

 Done?\
Help

#### 7\. Improve engines mandatory

Before using Flask to display our HBNB data, you will need to update some part of our engine:

Update `FileStorage`: (`models/engine/file_storage.py`)

-   Add a public method `def close(self):`: call `reload()` method for deserializing the JSON file to objects

Update `DBStorage`: (`models/engine/db_storage.py`)

-   Add a public method `def close(self):`: call `remove()` method on the private session attribute (`self.__session`) [tips](https://intranet.hbtn.io/rltoken/O2mDvznV40mXE9dvTT3LJw "tips") or `close()` on the class `Session` [tips](https://intranet.hbtn.io/rltoken/Vdh9u26tfc9fObUOb9NFzw "tips")

Update `State`: (`models/state.py`) - If it's not already present

-   If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City`objects from `storage` linked to the current `State`

At this moment, in another tab:

And let's go back the Python console:

And for the getter `cities` in the `State` model:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `models/engine/file_storage.py, models/engine/db_storage.py, models/state.py`

Check your code?

 Done?\
Help

#### 8\. List of states mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage`or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/states_list`: display a HTML page: (inside the tag `BODY`)
        -   `H1` tag: "States"
        -   `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://intranet.hbtn.io/rltoken/fid5cMJKYMaRJqL60PlUew "tip")
            -   `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
-   Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump") to have some data
-   You must use the option `strict_slashes=False` in your route definition

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/HnqtubVouQ7WVUhJ5rTMLQ "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/7-states_list.py, web_flask/templates/7-states_list.html`

Check your code?Get a container

 Done?\
Help

#### 9\. Cities by states mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage`or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   To load all cities of a `State`:
    -   If your storage engine is `DBStorage`, you must use `cities` relationship
    -   Otherwise, use the public getter method `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/cities_by_states`: display a HTML page: (inside the tag `BODY`)
        -   `H1` tag: "States"
        -   `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://intranet.hbtn.io/rltoken/fid5cMJKYMaRJqL60PlUew "tip")
            -   `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>` + `UL`tag: with the list of `City` objects linked to the `State` **sorted by `name`** (A->Z)
                -   `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
-   Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump") to have some data
-   You must use the option `strict_slashes=False` in your route definition

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/HnqtubVouQ7WVUhJ5rTMLQ "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

In another tab:

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/8-cities_by_states_screenshot.jpg)

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html`

Check your code?Get a container

 Done?\
Help

#### 10\. States and State mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage`or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   To load all cities of a `State`:
    -   If your storage engine is `DBStorage`, you must use `cities` relationship
    -   Otherwise, use the public getter method `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/states`: display a HTML page: (inside the tag `BODY`)
        -   `H1` tag: "States"
        -   `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://intranet.hbtn.io/rltoken/fid5cMJKYMaRJqL60PlUew "tip")
            -   `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
    -   `/states/<id>`: display a HTML page: (inside the tag `BODY`)
        -   If a `State` object is found with this `id`:
            -   `H1` tag: "State: "
            -   `H3` tag: "Cities:"
            -   `UL` tag: with the list of `City` objects linked to the `State` **sorted by `name`** (A->Z)
                -   `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
        -   Otherwise: 
            -   `H1` tag: "Not found!"
-   You must use the option `strict_slashes=False` in your route definition
-   Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump") to have some data

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/HnqtubVouQ7WVUhJ5rTMLQ "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

In another tab:

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/9-states.py, web_flask/templates/9-states.html`

Check your code?Get a container

 Done?\
Help

#### 11\. HBNB filters mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage`or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   To load all cities of a `State`:
    -   If your storage engine is `DBStorage`, you must use `cities` relationship
    -   Otherwise, use the public getter method `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/hbnb_filters`: display a HTML page like `6-index.html`, which was done during the project [0x01. AirBnB clone - Web static](https://intranet.hbtn.io/rltoken/QU3Og2v6Xr_z4qqWen8vcg "0x01. AirBnB clone - Web static")
        -   Copy files `3-footer.css`, `3-header.css`, `4-common.css` and `6-filters.css` from `web_static/styles/` to the folder `web_flask/static/styles`
        -   Copy files `icon.png` and `logo.png` from `web_static/images/` to the folder `web_flask/static/images`
        -   Update `.popover` class in `6-filters.css` to allow scrolling in the popover and a max height of 300 pixels.
        -   Use `6-index.html` content as source code for the template `10-hbnb_filters.html`:
            -   Replace the content of the `H4` tag under each filter title (`H3` States and `H3`Amenities) by `&nbsp;`
        -   `State`, `City` and `Amenity` objects must be loaded from `DBStorage` and **sorted by name** (A->Z)
-   You must use the option `strict_slashes=False` in your route definition
-   Import this [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql "10-dump") to have some data

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/HnqtubVouQ7WVUhJ5rTMLQ "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

In the browser:

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters_0.jpg)![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters_1.jpg)![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters_2.jpg)![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters_3.jpg)

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/`

 Done?\
Help

#### 12\. HBNB is alive! #advanced

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage`or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   To load all cities of a `State`:
    -   If your storage engine is `DBStorage`, you must use `cities` relationship
    -   Otherwise, use the public getter method `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/hbnb`: display a HTML page like `8-index.html`, done during the [0x01. AirBnB clone - Web static](https://intranet.hbtn.io/rltoken/QU3Og2v6Xr_z4qqWen8vcg "0x01. AirBnB clone - Web static") project
        -   Copy files `3-footer.css`, `3-header.css`, `4-common.css`, `6-filters.css` and `8-places.css` from `web_static/styles/` to the folder `web_flask/static/styles`
        -   Copy all files from `web_static/images/` to the folder `web_flask/static/images`
        -   Update `.popover` class in `6-filters.css` to enable scrolling in the popover and set max height to 300 pixels.
        -   Update `8-places.css` to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)
        -   Use `8-index.html` content as source code for the template `100-hbnb.html`:
            -   Replace the content of the `H4` tag under each filter title (`H3` States and `H3`Amenities) by `&nbsp;`
            -   Make sure all HTML tags from objects are correctly used (example: `<BR />` must generate a new line)
        -   `State`, `City`, `Amenity` and `Place` objects must be loaded from `DBStorage` and **sorted by name** (A->Z)
-   You must use the option `strict_slashes=False` in your route definition
-   Import this [100-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql "100-dump") to have some data

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/HnqtubVouQ7WVUhJ5rTMLQ "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

In the browser:

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb_0.jpg)![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb_1.jpg)![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb_2.jpg)![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb_3.jpg)![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb_4.jpg)

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/100-hbnb.py, web_flask/templates/100-hbnb.html, web_flask/static/`
