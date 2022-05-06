# curelink_assignment 
Python application which sends email to a list of subscribers at a specified time. 
 
# Steps to set up and run the project on your local machine: 
1) Make a new folder. 
2) Initialize an empty git repository inside the folder by running the command "git init" in your terminal. 
3) Clone the repository using "git clone https://github.com/shanoorahmed/curelink_assignment.git". 
4) Move into the folder, set up a new virtual enviroment and activate it. 
    4.1) For making a new virtual enviroment, paste "python3 -m venv venv" and run it. 
    4.2) For activating it: 
        Windows: 
        i) Set-ExecutionPolicy Unrestricted -scope process 
        ii) .\venv\Scripts\activate 
        Mac OS/Linux: 
        i) source venv/bin/activate 
5) Install all the dependencies using "pip install -r requirements.txt". 
6) Setting up the database: 
    6.1) Paste "python create_db.py" and run it. 
    6.2) Run "python insert_data.py" and enter some rows into the tables. 
    The database with two tables, i.e. User and Newsletter, is created. 
7) Enter your email and password in the main.py file line 10 and 11. 
8) Run "python main.py". 
 
# Project Description 
1) create_db.py creates the database and with the two tables User and Newsletter. In the User table, we have the name and email of the user. And in the Newsletter table, we have the topic and message related to that topic. 
2) insert_data.py lets us insert data into the two tables. 
3) In main.py we have the code for sending mails at a specified time to all the users in the User table. 
4) Firstly, we have to enter the username and password for the login to be successful. Also turn on less secure app access for your gmail account. 
5) We can add or remove functions from line 67 according to the topics of the emails. 
6) Finally we can schedule specific timings for the mail to be sent from line 77. 
 
# Future Improvements 
1) A landing page can be added for users to subscribe to the mailing list. 
2) Another page to handle all the mails and timings, instead of making changes in the code everytime. 
3) CRUD operations for message contents. 
4) Unsubscribe option for the users. 
5) The application currently runs on our local machine only and changes need to be made for its deployment. 
 
# References: 
1) https://www.geeksforgeeks.org/how-to-send-automated-email-messages-in-python/ 
2) https://pynative.com/python-sqlite/ 