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
    6.1) Enter some dummy data in the database in line 38 and 42 of create_db.py file.
    6.2) Paste "python create_db.py" and run it. 
    The database with two tables, i.e. User and Newsletter, is created.
7) Enter your email and password in the main.py file line 10 and 11.
8) Run "python main.py".

# Project Description


# Future Improvements
1) A landing page can be added for users to subscribe to the mailing list.
2) Another page to handle all the mails, instead of making changes in the code everytime.
3) CRUD operations for message contents.
4) Unsubscribe option for the users.

# References:
1) https://www.geeksforgeeks.org/how-to-send-automated-email-messages-in-python/
2) https://pynative.com/python-sqlite/