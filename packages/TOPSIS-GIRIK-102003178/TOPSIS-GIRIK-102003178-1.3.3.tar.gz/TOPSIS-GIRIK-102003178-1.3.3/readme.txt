Topsis Value Calculator

TopsisCalc is a Python package implementing Topsis method, used for multi-criteria decision analysis.

TOPSIS stands for Technique for Order of Preference by Similarity to Ideal Solution

Just provide the input attributes and it will gives the results 


## Installation

$ pip install TOPSIS-GIRIK-102003178==1.3.3

In the commandline, you can write as -
    topsis <path to input_data_file_name> <weights as strings> <impacts as strings> <result_file_name>

E.g for input data file as data.csv, command will be like
     topsis data.csv "1,1,1,1" "+,+,-,+" output.csv

This will print all the output attribute values along with the Rank column, in a tabular format, and output the resultant table into output.csv file

License -> MIT