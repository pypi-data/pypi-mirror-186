import sys
import math
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def topsis(data,weight,impact) :
    cols = data.columns
    idealBest = []
    idealWorst = []

    ## normalizing the values
    for val in cols :
        sum = 0
        for i in data[val] :
            sum += i**2
        sum = math.sqrt(sum)
        for i in range(len(data)) :
            data.loc[i,val] = data.loc[i,val]/sum

    ## multiplying weights with respective columns
    for val,w in zip(cols,weight) :
        for i in range(len(data)) :
            data.loc[i,val] = data.loc[i,val]*w
    
    ## finding ideal best and ideal worst values
    for val,i in zip(cols,impact) :
        arr = list(data[val])
        if i == '+' :
            arr.sort()
        else :
            arr.sort(reverse=True)
        idealBest.append(arr[len(arr)-1])
        idealWorst.append(arr[0])

    ## finding euclidean distance from ideal best and ideal worst values
    sp = []
    sn = []
    p = []

    for i in range(len(data)) :
        sumPos = 0
        sumNeg = 0
        for j in range(len(cols)) :
            sumPos += (idealBest[j] - data.loc[i,cols[j]])**2
            sumNeg += (idealWorst[j] - data.loc[i,cols[j]])**2
        sp.append(math.sqrt(sumPos))
        sn.append(math.sqrt(sumNeg))

    ## finding perfromance score
    for i in range(len(sp)) :
        p.append(sn[i]/(sn[i]+sp[i])) 
   
    ## finding rank
    rank = [None] * len(p)
    dict = {}
    for i in range(len(p)) :
        dict[i] = p[i]
    dict = sorted(dict.items(), key=lambda x:x[1],reverse=True)
    r = 1
    for pos in dict :
        rank[pos[0]] = r
        r += 1

    return pd.DataFrame({'Topsis score' : p,'Rank':rank})

def main() :
    ## taking input
    if len(sys.argv) != 5 :
        sys.exit('Wrong number of arguments')

    inputFile = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    outputFile = sys.argv[4]

    ## reading input file
    try :
        data = pd.read_csv(inputFile)
    except :
        sys.exit('File not found')

    ## creating list of weights and impacts
    weights = weights.split(',')
    impacts = impacts.split(',')

    nrow = data.shape[0]
    ncol = data.shape[1]

    if ncol < 3 :
        sys.exit('Not enough columns in input file')


    ## checking if number of weights and impacts are same as columns
    if (ncol-1) != len(weights) :
        sys.exit('Incorrect number of Weights')

    if (ncol-1) != len(impacts) :
        sys.exit('Incorrect number of impacts')


    ## converting weights into float and checking if values inside weights are correct
    try :
        for i in range(len(weights)) :
            weights[i] = float(weights[i])
    except :
        print('Incorrect data in weights')

    ## checking if values inside impact are correct
    for val in impacts :
        if val != '+' and val != '-' :
            sys.exit('Incorrect data in impact')

    ## implementing topsis model

    try :
        ans = topsis(data[data.columns[1:]],weights,impacts)
    except :
        sys.exit('Non numeric values in file')

    data = pd.concat([data,ans],axis=1,join='inner')

    data.to_csv(outputFile,index=False)

if __name__ == '__main__' :
    main()