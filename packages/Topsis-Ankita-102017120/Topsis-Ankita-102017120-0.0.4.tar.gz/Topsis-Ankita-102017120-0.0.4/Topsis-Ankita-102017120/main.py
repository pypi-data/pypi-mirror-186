import argparse
import sys
import os
import numpy as np
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype


def topsis_score(args):
    df = pd.read_csv(args.df);

    weights= args.weights.split(',')

    impact=args.impact.split(',')
    resultname=args.resultname

    result=df.copy()
    ncol=len(df.columns)
    if(ncol<=3):
      sys.stdout.write("Number of columns less than 3 .It must be greater than 3")
      sys.exit(0)
    curr=[]
    for i in df.columns:
      curr.append(i)

    curr.pop(0)
    for i in curr:
      if df[i].dtype!=np.int64 and df[i].dtype != np.float64:
        sys.stdout.write("There is atleast one column with non-numeric data type.")
        sys.exit(0)

    if(len(weights)!=(ncol-1)):
      sys.stdout.write("Number of weights not equal to number of features")
      sys.exit(0)

    if(len(impact)!=(ncol-1)):
      sys.stdout.write("Number of impacts not equal to number of features")
      sys.exit(0)

    for i in impact:
      if i!="+" and i!="-":
        
        sys.stdout.write("Impact must be + or -")
        sys.exit(0)

    def normalize(df,ncol,weights):
      for i in range(1,ncol):
       temp=0
    
       for j in range(len(df)):
        
        temp=float(temp)+float(df.iloc[j,i])**2
      
       temp=temp**0.5

       for k in range(len(df)):
         df.iat[k,i]=(float(df.iloc[k,i])/float(temp))*float(weights[i-1])

    def cal_values(df,ncol,impact):
      p_val=(df.max().values)[1:]
      n_val=(df.min().values)[1:]
  
      for i in range(1,ncol):
        if impact[i-1]=='-':
          p_val[i-1],n_val[i-1]=n_val[i-1],p_val[i-1]

      return p_val,n_val

    def diff(df,ncol,p_val,n_val):
      S_p=[]
      S_n=[]
      for i in range(len(df)):
        temp=0
        temp1=0
        for j in range(1,ncol):
          temp=temp+(float(df.iloc[i,j])-float(p_val[j-1]))**2
          temp1=temp1+(float(df.iloc[i,j])-float(n_val[j-1]))**2

        temp=temp**0.5
        temp1=temp1**0.5
        S_p.append(temp)
        S_n.append(temp1)
      return S_p,S_n

    def performance(df,S_p,S_n):
     final=[]
     for i in range(len(df)):
       d=(float(S_n[i]))/(float(S_p[i])+float(S_n[i]))
       final.append(d)

     return final


    def create(df,final,result):

     result['Topsis score']=final
     result['Rank']=result['Topsis score'].rank(ascending=False).astype(int)
     
     result.to_csv(resultname,index=False)

    normalize(df,ncol,weights)
    p_val,n_val=cal_values(df,ncol,impact)
    S_p,S_n=diff(df,ncol,p_val,n_val)
    final=performance(df,S_p,S_n)
    create(df,final,result)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('df',
                        help="Enter the name of your csv file: ")

    parser.add_argument( 'weights',
                        help="Enter weights: ")

    parser.add_argument('impact' ,
                        help="Enter impacts: ")

    parser.add_argument('resultname', 
                        help="Enter output file name: ")

    if(len(sys.argv)<4):
      sys.stdout.write("Input missing")
      sys.exit(0)

    

    args = parser.parse_args()

    if os.path.exists(args.df):
      topsis_score(args)

    else:
      sys.stdout.write("Input file does not exist")
      sys.exit(0)
    
    
    sys.stdout.write("Result csv has been created in the same folder as the input csv")


