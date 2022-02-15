# shopping-cart-exercise

## Program Usage

To use this program, the store clerk or other user will be asked to input a series of product identifiers that coorelate with a pre-existing list of products.  At present, the list of available products includes 20 items with identifiers ranging 1-20.

When the program is initialized, the message "Please input a product identifier or 'DONE':" will appear.  The user should input the identifier or identifiers of the products that are being purchased.  Right now, this should be an integer between  1 and 20, though this could be changed if different products are loaded into the program.  Punctuation should not be used.  After each number is typed, the user should press enter to record the product.  The program will ask for another identifier until the user enters the key word "DONE".  It is important that "DONE" be typed in capital letters and contains no punctuation.  

When the user enters "DONE", the program will compile a list of the products purchased and their prices.  The subtotal, tax, and total will be calculated and displayed along with the name of the supermarket and the date and time of the transaction.  

## Setting Up and Running the Program

You should create a virtual environment to run the program in on your computer.

Enter the following from the command line to create the environment:

``` sh
conda create -n shopping-env python-3.8
```

Once you have created the environment, activate it as follows:

```sh
conda activate shopping-env
```

Navigate to the location of the program using the following commands:

```sh
cd ~/
```
After the slash, type the file path of where the program is saved.


Once within the virtual environment and using the directory of the program, use the following command to run the program.

```sh
python shopping-cart.py
```
