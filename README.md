# Software Services CRUD Application

This is a simple Python application that connects to a MongoDB database to manage software services. It provides a command-line interface (CLI) for performing CRUD (Create, Read, Update, Delete) operations on a database of software services.

## Features

- **Create**: Add new software services with details like name, 2-year support availability, estimated hours of work, and cost.
- **Read**: Display all available software services stored in the database.
- **Update**: Modify existing software services by updating any of the fields.
- **Delete**: Remove a software service from the database.
- **Exit**: Safely exit the application.

## Prerequisites

- **Python 3.x**: Ensure that Python is installed on your system.
- **MongoDB**: Install and run MongoDB on your local machine.
- **Python Packages**:
  - `pymongo`: The Python MongoDB driver.

Install the required package using pip:

```bash
pip install pymongo
```
## Getting Started

1. **Clone the Repository**:

```bash
git clone https://github.com/spowers0409/pythonCRUD.git
cd pythonCRUD
```
2. **Set Up MongoDB**

```bash
mongod
```
- By default, the application connects to a MongoDB instance running locally at `mongodb://localhost:27017/`

3. **Run the Application**
```bash
python softwareServices.py
```
4. **Using the Application**
- Follow the on-screen prompts to create, read, update, or delete software services.

## Code Overview
- **serviceID()**: Determines the next available ID for a new service by checking the current highest ID in the database.
- **createService()**: Prompts the user to input details for a new software service and adds it to the database.
- **readServices()**: Fetches and displays all software services from the database, including their custom ID, name, support availability, estimated hours, and cost.
- **updateService()**: Allows the user to update an existing software service by specifying the ID and the field to be updated.
- **deleteService()**: Deletes a software service from the database by its ID.
- **main()**: The main loop that provides the user with options to perform CRUD operations or exit the application.

## Example
```bash
Options:
C. Create Software Service
R. Read (Display) Software Services
U. Update Software Service
D. Delete Software Service
E. Exit

Enter your CRUDE option: C

Enter a Software Service name: Web Development
Is 2 Year Support available? (True/False): True
Enter the Estimated Hours of Work: 150
Enter the Cost: 5000

Service created with ID: 1
You have added: Web Development to the database
```



































