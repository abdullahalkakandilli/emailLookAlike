import streamlit as st
import pandas as pd
from abydos.phonetic import RussellIndex

df = pd.read_csv(r'C:\Users\alka\Masaüstü\testDatasets\emailLookaLikeTest.csv')
encode_list = []
re = RussellIndex()
for index, rows in df.iterrows():

    encode_ = re.encode(rows['Email'])
    encode_list.append(encode_)


df['Encode-scores'] = encode_list
duplicates = df[df.duplicated(subset=['Encode-scores'], keep = False)]
print(duplicates)