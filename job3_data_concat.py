import pandas as pd
import glob
import datetime
data_path=glob.glob('./crawling_data/*')
print(data_path)

df=pd.DataFrame()
for path in data_path[:-1]:
    df_temp=pd.read_csv(path)
    df=pd.concat([df, df_temp])
df.dropna(inplace=True)
df.reset_index(inplace=True, drop=True)
print(df.head())
print(df.tail())
print(df['category'].value_counts())
df.info()
df.to_csv('./crawling_data/naver_headline_news_titles_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)

#에러없을 때
#df=df.read_csv('/crawling_data/crawling_data/csv')
#df_headline=pd.read.csv('./crawling_data/naver_headline_news_20220525.csv')
#df_all=pd.concat([df_headline])