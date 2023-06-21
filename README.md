# Nearby Shops Management

This project is a web application for managing nearby shops. It allows users to create, read, and update shop information based on their current location and distance preferences. The project is built using the Django web framework with PostgreSQL and GeoDjango for spatial data management.


## Table of Contents



* [Overview]
* [Installation]
* [Usage]
* [Testing]
* [Technologies Used]
* [Contributing]


## Overview

The Nearby Shops Management project provides the following features:



* Shop Creation: Users can create new shop entries by providing shop details such as name, address, and coordinates (latitude and longitude).
* Shop Listing: The application displays a list of all nearby shops based on the user's current location and distance preferences.
* Shop Update: Users can update the details of existing shops, including name, address, and coordinates.
* Geographic Search: The application uses GeoDjango to perform spatial queries and retrieve shops within a specified distance from the user's location.
### DEMO is Deployed with Railway App at https://nearbyshops.up.railway.app/

## Installation

To set up and run the Nearby Shops Management project, you have two options: running it directly or using Docker. Choose the option that suits your preference.


### Option 1: Running Without Docker



1. Clone the repository:
```bash
git clone https://github.com/mayankWIZ/nearbyshops.git
```

2. Navigate to the project directory:
```bash
cd nearbyshops
```
3. Set up a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```
Also install all your OS supported relevant packages from system_packages.txt

5. Set up the PostgreSQL database:
    * Create a new PostgreSQL database and note down the database credentials.
    * Update the database settings in the settings.py file with your database credentials.
6. Apply database migrations:
```bash
python manage.py makemigration
python manage.py migrate
```

7. Start the development server:
```bash
python manage.py runserver
```
#### The application should now be running locally at http://localhost:8000.



### Option 2: Running with Docker

1. Clone the repository:
```bash
git clone https://github.com/mayankWIZ/nearbyshops.git
```
2. Navigate to the project directory:
```bash
cd nearbyshops
```
3. Build the Docker image:
```bash
docker build -t nearbyshops .
````
4. Run the Docker container:
```bash
docker run -p 8000:8000 nearbyshops
```
#### The application should now be running inside a Docker container at http://localhost:8000.

## Usage
1. Access the application in your web browser at http://localhost:8000.
2. To create a new shop, click on the "Create Shop" button and fill in the required details.
3. To view the list of nearby shops, click on the "View Nearby Shops" button and enter your current location (latitude and longitude) and the desired distance in kilometers.
4. The application will display the shops within the specified distance from your location.
5. To update a shop's details, click on the "Edit" button next to the shop you wish to update and make the necessary changes.
6. You can also delete a shop by clicking on the "Delete" button.


## Testing

To run the tests for the Nearby Shops Management project, follow these steps:

1. Make sure the project dependencies are installed (refer to the[ Installation] section).
2. Run the following command:

python manage.py test

5. This will execute the test cases and display the test results.


## Technologies Used

The Nearby Shops Management project utilizes the following technologies:



* Django: A high-level Python web framework for rapid development.
* PostgreSQL: A powerful open-source relational database management system.
* GeoDjango: A Django library for working with spatial data and geographic models.
* Docker: A platform for containerization to ensure consistent development and deployment environments.
* Other Python libraries: Refer to requirements.txt for the full list of dependencies.


## Contributing

Contributions to the Nearby Shops Management project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

To contribute code:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your fork.
4. Submit a pull request to the main repository.
