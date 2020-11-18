# ecu-seng-6245-investment-tracker
Note: This repository contains two implementations of an investment tracker. One is a pure Python implementation of essential classes with associated unit tests.

The other is an implementatio in Python and the Django Web Framework. This will eventually have unit tests once the translation of the Python implementation into the form needed for models and views in Django is complete.

Both were created for SENG 6245 course at East Carolina University.
## Development Environment
1. Create a new `conda`environment: `conda create -n SENG6245 python=3.8`
2. Activate the environment: `conda activate SENG6245`
3. Install Django 2.2 using `pip`: pip install Django==2.2`
4. Install `coverage` using `conda`: `conda install coverage`

## Running the Django site
1. Navigate to /investmentracker/
2. Run `python manage.py runserver`
3. Navigate to [localhost on port 8000](http://127.0.0.1:8000) to view the landing page.
4. Access the Django [admin page](http://127.0.0.1:8000/admin)

## Running tests:

`python run -m unittest -v Test*.py`

`coverage run -m unittest -v Test*.py`

## Running Django tests:
`python manage.py  test -v 3 investmentservices`
