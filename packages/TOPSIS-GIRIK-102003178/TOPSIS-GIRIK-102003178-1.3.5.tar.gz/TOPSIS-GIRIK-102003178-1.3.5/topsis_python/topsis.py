#IMPORTING ESSENTIAL LIBRARIES
from os import path
from tabulate import tabulate
import pandas as pd
import sys
import math as m
import csv
def topsis(file, wt, imp, resFile):
    # LOADING DATASET
    df = pd.read_csv(file)

    # DROPPING EMPTY CELLS IF ANY
    df.dropna(inplace = True)

    # ONLY TAKING NUMERICAL VALUES
    d = df.iloc[0:,1:].values

    # CONVERTING INTO MATRIX
    matrix = pd.DataFrame(d)

    # CALCULATING SUM OF SQUARES
    sumSquares = []
    for col in range(0, len(matrix.columns)):
        X = matrix.iloc[0:,[col]].values
        sum = 0
        for value in X:
            sum = sum + m.pow(value, 2)
        sumSquares.append(m.sqrt(sum))
    # print(sumSquares)

    # DIVIDING ALL THE VALUES BY SUM OF SQUARES
    j = 0
    while(j < len(matrix.columns)):
        for i in range(0, len(matrix)):
            matrix[j][i] = matrix[j][i]/sumSquares[j] 
        j = j+1

    # MULTIPLYING BY WEIGHTS
    # wt = [0.25, 0.25, 0.25, 0.25]
    k = 0
    while(k < len(matrix.columns)):
        for i in range(0, len(matrix)):
            matrix[k][i] = matrix[k][i]*wt[k] 
        k = k+1

    # CALCULATING IDEAL BEST AND IDEAL WORST
    # imp = ['+', '+', '-', '+']
    bestVal = []
    worstVal = []

    for col in range(0, len(matrix.columns)):
        Y = matrix.iloc[0:,[col]].values
        
        if imp[col] == "-" :
            maxValue = max(Y)
            minValue = min(Y)
            bestVal.append(minValue[0])
            worstVal.append(maxValue[0])
        if imp[col] == "+" :
            maxValue = max(Y)
            minValue = min(Y)
            bestVal.append(maxValue[0])
            worstVal.append(minValue[0])

    # CALCULATING Si+ & Si-
    SiPlus = []
    SiMinus = []

    for row in range(0, len(matrix)):
        temp = 0
        temp2 = 0
        wholeRow = matrix.iloc[row, 0:].values
        for value in range(0, len(wholeRow)):
            temp = temp + (m.pow(wholeRow[value] - bestVal[value], 2))
            temp2 = temp2 + (m.pow(wholeRow[value] - worstVal[value], 2))
        SiPlus.append(m.sqrt(temp))
        SiMinus.append(m.sqrt(temp2))

    # CALCULATING PERFORMANCE SCORE Pi
    Pi = []

    for row in range(0, len(matrix)):
        Pi.append(SiMinus[row]/(SiPlus[row] + SiMinus[row]))

    # CALCULATING RANK
    Rank = []
    sortedPi = sorted(Pi, reverse = True)

    for row in range(0, len(matrix)):
        for i in range(0, len(sortedPi)):
            if Pi[row] == sortedPi[i]:
                Rank.append(i+1)

    # INSERTING THE NEWLY CALCULATED COLUMNS INTO THE MATRIX
    col1 = df.iloc[:,[0]].values
    matrix.insert(0, df.columns[0], col1)
    matrix['Topsis Score'] = Pi
    matrix['Rank'] = Rank

    # RENAMING ALL THE COLUMNS
    newColNames = []
    for name in df.columns:
        newColNames.append(name)
    newColNames.append('Topsis Score')
    newColNames.append('Rank')
    matrix.columns = newColNames

    # SAVING THE MATRIX INTO A CSV FILE
    matrix.to_csv(resFile)

    # PRINTING TO THE CONSOLE USING TABULATE PACKAGE
    print(tabulate(matrix, headers = matrix.columns))

def main() :
    if len(sys.argv) == 5 :
        # file
        file = sys.argv[1].lower()
        # wt
        wt = sys.argv[2].split(",")
        for i in range(0, len(wt)):
            wt[i] = int(wt[i])
        # imp
        imp = sys.argv[3].split(",")
        for impact in imp:
            if impact != "+" and impact != "-":
                print ("Impact must have only + or - values")
                return 
        # resFile
        resFile = sys.argv[-1].lower()
        if ".csv" not in resFile:
            print("RESULT FILENAME SHOULD CONTAIN '.csv'")
            return
        if path.exists(file) :
            if len(wt) != len(imp) :
                print("INPUT ERROR, NUMBER OF WEIGHTS AND IMPACTS SHOULD BE EQUAL")
                return
        else :
            print("INPUT FILE DOES NOT EXISTS ! CHECK YOUR INPUT")
            return
        with open(file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            if len(header) < 3:
                print("Error: Input file must contain at least three columns.")
                return
            else:
                for row in reader:
                    numeric_columns=len(row)-1
                    for i in range(1, len(row)):
                        try:
                            float(row[i])
                        except ValueError:
                            print("Error: All columns from 2nd column onwards must be numeric in nature ")
                            return
                if (numeric_columns!=len(wt) or numeric_columns!=len(imp)):
                    print ("The size of weight array, impact array and number of numeric coluns must all be same ")
                    return 
    else :
        print("REQUIRED NUMBER OF ARGUMENTS ARE NOT PROVIDED !")
        print("SAMPLE INPUT : python <script_name> <input_data_file_name> <wt> <imp> <result_file_name>")
        return
    topsis(file, wt, imp, resFile)

# MAIN FUNCTION
# if everything is fine, it will call the topsis() function,
# otherwise will display appropriate error

if __name__=='__main__':
    main()