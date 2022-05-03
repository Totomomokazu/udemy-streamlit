import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("たまちゃん♡ともちゃん")
st.write("Dataframe")

df = pd.DataFrame({
    "1列目":[1, 2, 3, 4],
    "2列目":[10, 20, 30, 40]
})

st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=300,height=200)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


df1 = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
st.dataframe(df1.style.highlight_max(axis=0),width=500,height=200)
st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=["lat","lon"]
)
st.dataframe(df2.style.highlight_max(axis=0),width=500,height=200)
st.map(df2)

img = Image.open("bankcy.jpg")
st.image(img,caption="bankcyyyyyy",use_column_width=True)

if st.checkbox("Show Image"):
    img = Image.open("bankcy2.jpg")
    st.image(img,caption="bankcyyyyyy2",use_column_width=True)

option=st.selectbox(
    "好きな数字を教えて",
    list(range(1,11))
)

"あなたの好きな数字は",option,"です"


text=st.text_input("あなたの趣味を教えてください")
"あなたの趣味は",text,"です。"
condition=st.slider("あなたの今の調子は？",0,100,50)
"コンディション",condition


