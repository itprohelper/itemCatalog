# Item Catalog
Project for the Udacity course
# I did not use Vagrant for this project. I used a Digital Ocean droplet and using docker on top. DO NOT use Vangrant to follow my example.

**Note: It is recommended to use a Linux/Mac with Python 2.7 and sqlite installed**

### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).  
(On Mac or Linux systems you can use the regular terminal program.)

## Fetch the Source Code and VM Configuration

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.  
**Other systems:** Use your favorite terminal program.

From the terminal, run:

    git clone https://github.com/udacity/OAuth2.0 oauth

This will give you a directory named **itemcatalog** complete with the source code for the flask application, a vagrantfile, and a bootstrap.sh file for installing all of the necessary tools.

## Run the code!

Using the terminal, change directory to itemcatalog (**cd itemcatalog**):


Type **ls** to ensure that you are inside the directory that contains application.py, database_setup.py, and two directories named 'templates' and 'static'

Now type **python database_setup.py** to initialize the database.

Type **python populateit.py** to populate the database with restaurants and menu items. (Optional)

Type **python application.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the Catalog app.  You should be able to view, add, edit, and delete menu items and categories.
