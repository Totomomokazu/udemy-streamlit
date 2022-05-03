import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("Streamlit")
st.write("Dataframe")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)  
    time.sleep(0.01)
    
"Done"



st.sidebar.write("Interactive Widgets")
text2=st.sidebar.text_input("あなたの趣味を教えてください")
condition2=st.sidebar.slider("あなたの今の調子は？",0,100,50)
"あなたの趣味:",text2
"コンディション",condition2


left_column,right_column=st.columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_column.write("表示されました")

expander1=st.expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2=st.expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3=st.expander("問い合わせ3")
expander3.write("問い合わせ3の回答")

