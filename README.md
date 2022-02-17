# shopping-cart-exercise

## Program Usage

To use this program, the store clerk or other user will be asked to input a series of product identifiers that coorelate with a pre-existing list of products.  At present, the list of available products includes 20 items with identifiers ranging 1-20.

The user will have the option at the beginning of the program every time it is run to update the products data.  The program will ask if the user would like to update the products list, and if the user indicates that they would, the program will enter an update mode.  In order for this element of the program to work, it is important that the user inputs the correct information.  The program will require the file path of the desired file to be typed so that it can be accessed.  The file additionally must be in a .csv format and contain the same keys as the default product list.  It must have a "id", "name", and "price" attribute that cooresponds with the barcode, name, and prices of the products.  Different attributes may not cause an error immediately, but may cause an error later on during usage.  If the user enters the path to a file that is not a .csv or a mistyped file path, the program will indicate an error and ask the user if they would like to try again.  The user may try again, or simply continue with the program with the default product set.

When the program is initialized, the message "Please input a product identifier or 'DONE':" will appear.  The user should input the identifier or identifiers of the products that are being purchased.  Right now, this should be an integer between  1 and 20, though this could be changed if different products are loaded into the program.  Punctuation should not be used.  After each number is typed, the user should press enter to record the product.  The program will ask for another identifier until the user enters the key word "DONE".  It is important that "DONE" be typed in capital letters and contains no punctuation.  

When the user enters "DONE", the program will compile a list of the products purchased and their prices.  The subtotal, tax, and total will be calculated and displayed along with the name of the supermarket and the date and time of the transaction.  

## Setting Up and Running the Program

You should create a virtual environment to run the program in on your computer.

Enter the following from the command line to create the environment:

``` sh
conda create -n shopping-env python=3.8
```

Once you have created the environment, activate it as follows:

```sh
conda activate shopping-env
```

Navigate to the location of the program using the following commands:

```sh
cd ~/myfilepath
```
After the slash, type the file path of where the program is saved.


There are some basic requirements of the program, primarily the pandas package.  Make sure these are installed in the virtual environment using the following command:

```sh
pip install -r requirements.txt
```

After the requirements have been installed, use the following command to run the program:
Note that the packages do not need to be installed multiple times so long as you are using the same virtual environment that they were initially installed in.

```sh
python shopping-cart.py
```

When you are finished using the program, deactivate the virtual environment using the following:

```sh
conda deactivate
```
