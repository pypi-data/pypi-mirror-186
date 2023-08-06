import argparse
import sys
import os
import numpy as np
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype


def topsis():
  n = len(sys.argv)
  if n != 5:
        print("Error: Provide correct input format <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        quit()
  if not sys.argv[1].lower().endswith('.csv') or not sys.argv[4].lower().endswith('.csv'):
        print("Error: input and output file format should be .csv")
        quit()
  if(len(sys.argv[2]) != len(sys.argv[3])):
        print("Error: Number of weights and number of impacts passed dont match")
        quit()
  i=0
  while i<len(sys.argv[3]):
        if sys.argv[3][i] not in ["+","-"]:
            print("Error: The impacts should be either '+'/'-'")
            quit()
        i+=2
  try:
        df = pd.read_csv(sys.argv[1])
  except:
        print("Error: Cannot find the file")
        quit()
  if(df.shape[1] <3):
        print("Error: Number of columns should be >= 3")
        quit()
  if(df.shape[1]-1 != len(sys.argv[2])//2+1 or df.shape[1]-1 != len(sys.argv[3])//2+1):
        print("Error: Number of columns of df and number of weights/impacts passed dont match")
        quit()

  df = pd.read_csv(sys.argv[1])
  print(df)
  result=df.copy()
  ncol=len(df.columns)
  weights=sys.argv[2]
  impact=sys.argv[3]
  resultname=sys.argv[4]
  weights=weights.split(',')
  impact=impact.split(',')
  
  curr=[]
  for i in df.columns:
      curr.append(i)

  curr.pop(0)
  for i in curr:
      if df[i].dtype!=np.int64 and df[i].dtype != np.float64:
        print("There is atleast one column with non-numeric data type.")
        quit()

  
  for i in range(1,ncol):
      temp=0
    
      for j in range(len(df)):
        
        temp=float(temp)+float(df.iloc[j,i])**2
      
      temp=temp**0.5
      

      for k in range(len(df)):
         
         df.iat[k,i]=(float(df.iloc[k,i])/float(temp))*float(weights[i-1])
         

  
  p_val=(df.max().values)[1:]
  n_val=(df.min().values)[1:]
  
  for i in range(1,ncol):
      if impact[i-1]=='-':
          p_val[i-1],n_val[i-1]=n_val[i-1],p_val[i-1]

      

  
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
      

  
  final=[]
  for i in range(len(df)):
       d=(float(S_n[i]))/(float(S_p[i])+float(S_n[i]))
       final.append(d)

  

  result['Topsis score']=final
  result['Rank']=result['Topsis score'].rank(ascending=False).astype(int)
     
  result.to_csv(resultname,index=False)
  sys.stdout.write("Result csv has been created in the Users/pc")





if __name__ == '__main__':
  topsis()
    

    
    
    

