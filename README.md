###########################################Resort Hub############################################

                                                 TEAM MEMBERS 
                                                 
                                                 Jayesh Ranjan
                                                 Feazan Yaseen
                                                   Fanny Dai
                                                   Lucy Yang

DESCRIPTION
-----------
A travel agency website was developed as part of Final Project for Databases course that supports searching for
accommodations, transportations that are available based on location. Ability to add/remove accommodation,
transportation, user registration system and customer support system and an administrator page.


IMPLEMENTATION DETAILS
----------------------
The following technologies were utilized
UI - HTML | CSS | Bootstrap
Front End - Javascript | JQuery | Ajax
Back End - Python
Back End Framework - Flask
Database - AWS (Amazon Web Services) RDBMS

FILES
-----
Routing and Backend Related:
main.py - Entry point to the program and contains all the routes (DO: "python3 main.py" to run the program) 
adminFunction.py - Admin page functions on the server side
homePageFunction.py - Heart of the program, this is where all functions related to search, checkout
                      and miscellaneous actions can be found here. 
loginPageFunctions.py - Account Registration and Login functions can be found here

Database Related:
dbConnect.py - Connection to Database
dbFunctions.py - All calls to DB is made from here

UI:
templates/ - Contains all the HTML Pages
static/css - All CSS files are stored here
static/images - All images are stored here
static/js - All javascript files are stored here


HOW TO RUN:
----------
1) Clone the Repository
2) cd Resort-Hub
3) python3 main.py (Make sure flask and other dependencies are installed)
