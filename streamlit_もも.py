import linecache
import time
from altair import AreaConfig
import numpy as np
import streamlit as st

st.title('よろしくね💩')
st.write('これから作品を作っていきます')

text = st.text_input('あなたの名前をおしえてくだささい')
st.write('あなたのお名前は'+text+'です')

condition = st.slider('あなたの今の調子は?',0, 100, 50)#最小値,最大値,スタート位置
'コンディション:',condition

text = st.text_input(text+'ちゃんのすきなたべものなに？')
option = st.selectbox('好きな数字を教えてください',list(['1番','2番','3番','4番']))
'あなたが選択したのは,',option,'だね'
option = st.selectbox('好きなごはんをえらんでね。',list(['おにぎり','塩おにぎり','梅おにぎり','北海道こんぶおにぎり']))
'あなたがおえらびになったのは,',option,'だね'

st.sidebar.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i +1)
    time.sleep(0.1)
'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

from PIL import Image
img = Image.open('IMG_0776.JPG')
st.image(img,caption='生活場面',use_column_width=True)

import pandas as pd
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)

import numpy as np
df = pd.DataFrame(
    np.random.rand(20,3), #20行3列
columns = ['a','b','c']
)
st.table(df.style.highlight_max(axis=0))

st.bar_chart(df)