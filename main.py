
import streamlit as st
from PIL import Image
import time



st.title('streamlit 超入門') #タイトルの追加

st.write('progress bar') #テキストの追加

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'DONE!!'
left_column,right_column = st.columns(2)
button = left_column.button("右カラムにボタンを表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ1")
expander.write("問い合わせ内容1を表示")
expander = st.expander("問い合わせ2")
expander.write("問い合わせ内容2を表示")
expander = st.expander("問い合わせ3")
expander.write("問い合わせ内容3を表示")
#text = st.text_input('あなたの趣味を教えてください')
#condition = st.slider('あなたの今の体調は',0,100,50)

#'あなたの趣味は',text
#'あなたの体調は',condition


#if st.checkbox('Show Image'):
#    img = Image.open('sample1.jpg')
#    st.image(img,caption='Homura Title',use_column_width=True)

#option = st.selectbox(
#    'あなたが好きな数字は？',list(range(1,11)))
#
#'あなたが好きな数字は',option,'です'

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns=['lat','lon']
#)
#st.map(df)

#表の挿入

#"""
# 章
## 節
### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
#グラフ表示

