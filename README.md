# iRobot
## iRobot Cloud SW Team Take Home Assignment
The application is built using flask restX framework and is using MongoDb as a Database.

### Now to install Mongo(Mac), it requires to install some dependencies such as -:

    Open Terminal
    Execute Following Commands-:
        1. xcode-select --install
        2. brew help -:
            if it gives error execute following command to install it -:
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        3. brew help
        4. brew tap mongodb/brew
        5. brew tap | grep mongodb
        6. brew install mongodb-community@4.4

By executing above commands Mongo should be installed on the system.

### Next, we have to run MongoDb on the system by executing following commands in Terminal-:
    1. brew services start mongodb-community@4.4

    if there is mongo service already running you can stop it by following command and re-run it by executing step above

    1. brew services stop mongodb-community@4.4

Just for reference if the following commands are not working in any order, please refer the following documentation-:
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/



### Now the application has to be setup on the machine by following steps-:
1. Clone the Project from Git Repository -:
    git clone https://github.com/Jashan-Goku/iRobot.git
2. pip3 install virtualenv (This Installs the virtual env package)
3. python3 -m venv venv (This Installs the virtual env for the project with Active Python3 in it)
4. source venv/bin/activate (Activates the Virtual Environment)
5. pip install -r requirements.txt
6. Now run the Command_line.py file and follow the prompt's on the command line-:
     1. Please enter the Ingredients -: Type any ingredient from the above list
     2. Do you like this recipe -: if you like it type y or Y else press enter
     3. It will keep showing you the recipes unless you like a recipe and then finally it will add to the bag
        and show you the Shopping Bag
7. In Order to check the rest API's on swagger -:
    1. Run the app.py and launch http://127.0.0.1:5000 on your browser

### NOTE-: Please insert your own API Key in .env file for successful execution of the application.

## Future Work-:
### There can be various modifications done to the application such as -:
Shopping Bag can be designed in various ways such as a List of Common Ingredients, aisles and the average price is calculated on the basis of ingredient used in the recipe to the price per amount(gram/ounce/spoon etc).



