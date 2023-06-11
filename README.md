Project Name: Building a CRUD REST API with MySQL, Testing, and XML/JSON Output

Description:

The Building a CRUD REST API with MySQL, Testing, and XML/JSON Output project is aimed at developing a robust and scalable RESTful API that performs CRUD (Create, Read, Update, Delete) operations on a MySQL database. The API provides endpoints to interact with the database, allowing users to create, retrieve, update, and delete data through HTTP requests. Additionally, the project includes testing functionality to ensure the API's reliability and accuracy. The API supports both XML and JSON formats for input and output data, providing flexibility for clients to choose their preferred format.l.

Example Usage:

1. Creating a new record: The client sends an HTTP POST request to the API's create endpoint, providing the data for the new record in either XML or JSON format. The API validates and inserts the record into the MySQL database.

2. Retrieving data: The client sends an HTTP GET request to the API's read endpoint, specifying the desired record's identifier. The API queries the MySQL database and returns the requested data in the specified XML or JSON format.

3. Updating an existing record: The client sends an HTTP PUT request to the API's update endpoint, providing the updated data for a specific record. The API validates and modifies the corresponding record in the MySQL database.

4. Deleting a record: The client sends an HTTP DELETE request to the API's delete endpoint, specifying the identifier of the record to be deleted. The API removes the record from the MySQL database.

5. Testing the API: The project includes a suite of tests to ensure the API's functionality and reliability. Tests are executed to validate the create, read, update, and delete operations, as well as handling of invalid requests and edge cases.

installation: 

1. create repository in github with readme file
2. create folder in desktop
3. cd foldername
4. git init .
5. git clone https://github.com/username/nameofrepository.git
6. cd nameofrepository 
7. create virtual env = python -m venv .
8. activate scripts = Scripts/activate
8. create .gitignore = type in cmd: notepad .gitignore 
9. write:
Lib/
Scripts/
pyvenv.cfg
.gitignore
10. git status then check if there is untracked file
11. create api.py = notepad api.py leave empty, then type in cmd: git add . tapos git commit -m "comment mo"
12. type in cmd: git push origin master, pag napush na code na

