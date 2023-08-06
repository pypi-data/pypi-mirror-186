Topsis Value Calculator

TopsisCalc is a Python package implementing Topsis method, used for multi-criteria decision analysis.

TOPSIS stands for Technique for Order of Preference by Similarity to Ideal Solution

Just provide the input attributes and it will gives the results 


## Installation

$ pip install TOPSIS-GIRIK-102003178==1.1.1

In the commandline, you can write as -
    $ python <package_name> <path to input_data_file_name> <weights as strings> <impacts as strings> <result_file_name>

E.g for input data file as data.csv, command will be like
    $ python TOPSIS-GIRIK-102003178 data.csv "1,1,1,1" "+,+,-,+" output.csv

This will print all the output attribute values along with the Rank column, in a tabular format

License -> MIT