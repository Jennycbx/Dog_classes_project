Welcome to my Dog Training Classes app!
In order to run the app, first create the database:

<!-- createdb booking_manager -->

Then we need to run our psql command to access our sql file and create the tables:

<!-- psql -d booking_manager -f db/booking_manager.sql -->

Finally we need to run the console in order to input our data:

<!-- python3 console.py -->

To access the website, quit out of python in the terminal and run flask:

<!-- flask run -->

Cmd + click on the link provided.

The brief I was given was to build a piece of software to help a gym to manage memberships, and register members for classes. I decided to base mine on a dog training company instead of a gym. The app should allow the company to:

Create and edit Members.
Create and edit Classes.
Book members on specific classes.
Show a list of all upcoming classes.
Show all members that are booked in for a particular class.
Show a list of classes that members are booked in for.

In order to create this app I used Visual Studio Code to write my code.
I used flask to display my code and add interaction in the browser.
I used draw.io to plan my app.
I used SQL to create a database in order to save interactions with my app.

