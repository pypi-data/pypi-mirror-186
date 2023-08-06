import sys
import pandas as pd
import time

def main():

    argumentList=sys.argv
    logFile=open('101903793-log.txt','w')
    logFile.flush()
    weights=''
    impacts=''
    rname=''
    if(len(argumentList)<2):
        logFile.write(str(time.asctime())+' Not enough arguments. Exiting program.')
        sys.exit(0)
    elif len(argumentList)<4:
        logFile.write(str(time.asctime())+' Not enough arguments. Assuming defaults.')
    else:
        weights=argumentList[2]+','
        impacts=argumentList[3]+','

    fname=argumentList[1]
    rname=argumentList[-1]
    if rname[-3:]!='csv':
        rname='101903793-result.csv'

    try:
        df=pd.read_csv(fname,index_col=0,na_values=['missing','Missing','NA','na','Na','N/A','n/a',' '])
    except:
        logFile.write(str(time.asctime())+' Error is reading dataframe from the file.')

    n=len(df.columns)
    if n<2:
        logFile.write(str(time.asctime())+' DataFrame has less than 3 columns. Exiting...')
        sys.exit(0)

    if not len(weights):
        for i in df.columns:
            weights=weights+'1,'
            impacts=impacts+'+,'

    df.fillna(0)

    if not min(df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all())):
        logFile.write(str(time.asctime())+' Non-numeric values in the dataFrame. Exiting...')
        sys.exit(0)

    squared=[pow(sum(df[col].apply(lambda x: pow(x,2))),0.5) for col in df]
    normalized=pd.DataFrame(columns=df.columns)
    for i in range(n):
        normalized[df.columns[i]]=df[df.columns[i]].apply(lambda x: x/squared[i])

    try:
        weights=weights.split(sep=',')[:-1]
    except:
        logFile.write(str(time.asctime())+' Weights given improperly. Exiting...')
        sys.exit(0) 
        
    if len(weights)!=n:
        logFile.write(str(time.asctime())+' Weights given improperly. Exiting...')
        sys.exit(0)

    weighted=pd.DataFrame(columns=df.columns)
    for i in range(n):
        weighted[df.columns[i]]=normalized[normalized.columns[i]].apply(lambda x: x*float(weights[i]))

    try:
        impacts=impacts.split(sep=',')[:-1]
    except:
        logFile.write(str(time.asctime())+' Impacts given improperly. Exiting...')
        sys.exit(0)   

    if len(impacts)!=n or len(set(impacts).difference({'+','-'})):
        logFile.write(str(time.asctime())+' Impacts given improperly. Exiting...')
        sys.exit(0)

    v_plus=[max(weighted.iloc[:,i]) if impacts[i]=='+' else min(weighted.iloc[:,i]) for i in range(n)]
    v_minus=[min(weighted.iloc[:,i]) if impacts[i]=='+' else max(weighted.iloc[:,i]) for i in range(n)]

    s_plus=[]
    s_minus=[]
    for i in range(len(df)):
        s_plus.append(pow(sum([pow(weighted.iloc[i,j]-v_plus[j],2) for j in range(n)]),0.5))
        s_minus.append(pow(sum([pow(weighted.iloc[i,j]-v_minus[j],2) for j in range(n)]),0.5))
        

    p=[s_minus[i]/(s_plus[i]+s_minus[i]) for i in range(len(df))]
    df['Topsis Score']=p
    df['Rank']=df['Topsis Score'].rank(ascending=0)

    df.to_csv(rname)


if __name__ == '__main__':
    main()