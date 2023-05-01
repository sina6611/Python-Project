#command
#import numpy as np
#import pandas as pd
# pd.DataFrame(randn(n,m),[Xlable],[Ylable])
# df['A']
#df.drop['A',axis=0,inplace=True]
#df.shape
#df.loc['B'] row selection
# df.loc['A','C']
# df.iloc[[1,2],[2,4]]
#df.loc[['C','G'],['B','G']]
#df[(df['1']>0) & (df['2']<0)]
#df.reset_index()
#state='NR BD VG JH LK IJ ZG RT ZT FD'
#state_lis=state.split()
#df['States']=state_lis
# a=[1,121,13]  b=[14,4,5]  hier_index=list(zip(a,b))
#df.set_index('States')
#hier_index=pd.MultiIndex.from_tuples(hier_index)  multi level data frame
#d={'A':[1,2,np.nan],'B':[54,25,63],'C':[np.nan,25,89]}
#df=pd.DataFrame(d)
#df.dropna(thresh=1)
#df.fillna('Fill value')
#group=df.groupby('Company')
#group.mean()
#df.describe()
#df.describe().transpose()
#pd.concat([df1,df2],axis=1)
#pd.merge(df1,df2,on='Key') 
# right=pd.DataFrame({'A':'C0 C1 C2'.split(), 'B': 'D0 D1 D2'.split()}, index='K1 K2 K3'.split())
# left=pd.DataFrame({'C':'C0 C1 C2'.split(), 'D': 'D0 D1 D2'.split()}, index='K1 K2 K3'.split())
# left.join(right) 
# right['A'].nunique()
# df1['Key'].value_counts()
# df3=pd.DataFrame({'A':[1, 2, 3, 4, 5, 6, 7 ,8 ,9],'B':[9, 8, 7, 6 ,5 ,4, 3, 2, 1]})
# b=df3['B']
# b.sum()
# pip install lxml
