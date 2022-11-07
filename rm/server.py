import imp
import sys, os, csv, time
import pandas as pd

if not __name__ == '__main__':
    from . import HomeTk

def trash(name=None, tel=None, unix_time=None):
    dataPath = os.getcwd() + os.sep + 'rm' + os.sep + 'rmDatabase.csv'
    with open(dataPath, encoding='shift-jis') as f:           #scan to method_index
        csvreader = csv.reader(f)
        rmDatabase = [row for row in csvreader]
    for i in range(len(rmDatabase)):
        if rmDatabase[i][0] == name and rmDatabase[i][1] == tel\
            and rmDatabase[i][2] == unix_time:
            new_rmDatabase = rmDatabase[0:i]
            for j in range(i+1, len(rmDatabase)):
                new_rmDatabase.append(rmDatabase[j])
            break
    df = pd.DataFrame(new_rmDatabase)
    df.to_csv(dataPath, encoding='shift-jis', header=False, index=False)


if __name__ == '__main__':
    import HomeTk