import linecache
import time
from altair import AreaConfig
import numpy as np
import streamlit as st



# 文字の色を変えるには、styleメソッドを使用します
st.markdown('<style>h1 { color: #999900; }</style>', unsafe_allow_html=True)




import streamlit as st

from PIL import Image
img = Image.open('3人のこびと.jpg')
st.image(img,caption='　',use_column_width=True)


# Google FontsからRobotoを読み込むCSSコード
font_css = """
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
body {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
}
"""

# CSSコードをMarkdownとして表示
st.markdown(f"<style>{font_css}</style>", unsafe_allow_html=True)

import streamlit as st

# HTMLを使用してフォントを指定
import streamlit as st


# HTMLを使用してフォントを指定し、中央揃えにして大きさを調整
st.markdown(
    f'<h1 style="font-family: \'Darumadrop One\', sans-serif; text-align: center; font-size: 80px;">お つ か れ さ ま</h1>',
    unsafe_allow_html=True
)

st.markdown(
    f'<h1 style="font-family: \'Darumadrop One\', sans-serif; text-align: center; font-size: 40px;">いつもがんばっているきみへ</h1>',
    unsafe_allow_html=True
)

st.write('　')
st.write('　')
st.write('　')
st.write('　')
st.write('　')
st.write('　')

custom_style = """
    <style>
        /* 文字のスタイルを指定 */
        .custom-text {
            font-family: 'Darumadrop One', sans-serif;
            font-size: 25px;
            color: #996600; /* 好みの文字色に変更 */
            text-align: center;
        }
    </style>
"""

# StreamlitアプリにカスタムCSSを適用
st.markdown(custom_style, unsafe_allow_html=True)

# テキストを表示
st.write('<div class="custom-text">きみのおなまえをおしえてね。</div>', unsafe_allow_html=True)

text = st.text_input('　')

# 入力がある場合は次の文章を表示
if text:
    styled_text = f'<div class="custom-text">{text}ちゃん、こんにちは。</div>'
    st.markdown(styled_text, unsafe_allow_html=True)
    styled_text = f'<div class="custom-text">このページをみつけてくれて、ありがとう。</div>'
    st.markdown(styled_text, unsafe_allow_html=True)
    st.write('　')
    st.write('　')   
    img = Image.open('ありがとう.png') 
    st.image(img,caption='　',use_column_width=True)
    
else:
    img = Image.open('月.png')
    st.image(img,caption='　',use_column_width=True)



st.write('　')
st.write('　')
st.write('　')
st.write('　')

custom_style = """
    <style>
        /* 文字のスタイルを指定 */
        .custom-text {
            font-family: 'Darumadrop One', sans-serif;
            font-size: 25px;
            color: #996600; /* 好みの文字色に変更 */
            text-align: center;
        }
    </style>
"""

# StreamlitアプリにカスタムCSSを適用
st.markdown(custom_style, unsafe_allow_html=True)

# テキストを表示
st.write('<div class="custom-text">いまのきみはどんなきぶん?</div>', unsafe_allow_html=True)

import streamlit as st
import streamlit as st
import pandas as pd
import plotly.express as px




# ユーザーに気分を選択させるセレクトボックス
mood = st.selectbox("　", ["しあわせ～", "少しかなしいことがあったよ。", "たのしみなことがあるよ！", "すこしおこだよ。"])

# 選択された気分に基づいて異なる文章を表示
if mood == "しあわせ～":
    st.write('<div class="custom-text">へ~。なにかいいことあったんか?<br>そんなきみには、こんなえいががおすすめ!<br><br></div>', unsafe_allow_html=True)
    from PIL import Image
    img = Image.open('ひみつ道具博物館.jpg')
    st.image(img, caption='　', use_column_width=True)

    st.write('　')
    img = Image.open('ゆめみーる.jpg')
    st.image(img, caption='　', use_column_width=True)

elif mood == "少しかなしいことがあったよ。":
    st.write('<div class="custom-text">どうしたの?<br>わたしでよかったらおしえてね。</div>', unsafe_allow_html=True)
    text = st.text_input('　　')
    if text:

        st.write('<div class="custom-text">そうだったんだね。<br>かなしいときはじんないとものりのネタみると、すこしげんきでるよ。<br>したをクリックしてみてね。<br><br></div>', unsafe_allow_html=True)

elif mood == "たのしみなことがあるよ！":
    st.write('<div class="custom-text"><br>なになに? わてにもおしえて~!<br><br>やっぱき~かない!</div>', unsafe_allow_html=True)

elif mood == "すこしおこだよ。":
    st.write('<div class="custom-text">いらいらすることあるよね。<br>まわりのともだちにもいえないときだってあるよね。<br></div>', unsafe_allow_html=True)
    st.write('<div class="custom-text">したのところにらくがきしちゃお。<br>そんなときはじんないとものりのネタをみると、わらえてくるよ。</div>', unsafe_allow_html=True)
    import pandas as pd
    from PIL import Image
    import streamlit as st
    from streamlit_drawable_canvas import st_canvas

    # Specify canvas parameters in application
    drawing_mode = st.sidebar.selectbox(
        "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
    )

    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("Stroke color hex: ")
    bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
    bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

    realtime_update = st.sidebar.checkbox("Update in realtime", True)

    

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=Image.open(bg_image) if bg_image else None,
        update_streamlit=realtime_update,
        height=150,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
        key="canvas",
    )

    # Do something interesting with the image data and paths
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data)
    if canvas_result.json_data is not None:
        objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
        for col in objects.select_dtypes(include=['object']).columns:
            objects[col] = objects[col].astype("str")
        st.dataframe(objects)

# 他にも気分に応じて異なる処理や文章を表示することができます




custom_style = """
    <style>
        /* 文字のスタイルを指定 */
        .custom-text {
            font-family: 'Darumadrop One', sans-serif;
            font-size: 25px;
            color: #CC9900; /* 好みの文字色に変更 */
            text-align: center;
        }
    </style>
"""

# StreamlitアプリにカスタムCSSを適用
st.markdown(custom_style, unsafe_allow_html=True)




import streamlit as st


# Google FontsからDarumadrop OneのWebフォントを追加
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Darumadrop+One&display=swap');
        .custom-text {
            font-family: 'Darumadrop One', sans-serif;
            font-size: 24px;
            color: #CC9900;  /* 好みの色に変更（例: 黒色） */
        }
    </style>
""", unsafe_allow_html=True)

import streamlit as st
import random

# 名言のリスト
quotes = [
    "<br>きっとなにもかもうまくいくわ。<br>　<br>白雪姫『白雪姫』<br><br>",
    "<br>今はどんなに悲しくても、信じ続けてさえいればいつか必ず夢は叶う<br>　<br>シンデレラ『シンデレラ』<br><br>",
    "<br>いつも笑顔でいればいつかきっと素敵な恋に巡り合う<br>- Always remember to be happy because you never know who’s falling in love with your smile. -<br>　<br>白雪姫『白雪姫』<br><br>",
    "<br>焦らずに自分を信じていればチャンスは必ずやってくるのだ。<br>- Even miracles take a little time. -<br>　<br>フェアリーゴッドマザー『シンデレラ』<br><br>",
    "<br>僕を信じて。<br>- Do you trust me? -<br>　<br>アラジン『アラジン』",
    "<br>みんな違って、みんないい。<br>-　What makes someone special? I suppose it all depends. It’s what’s unique in each of us.　-<br>　<br>アリエル『リトルマーメイド』<br><br>"
    "<br>のび太くんをばかにするということは、ぼくをばかにすることだ。<br>ゆるせぬ！<br><br>ドラえもん『ドラえもん』"
]




st.markdown(
    f'<h1 style="font-family: \'Darumadrop One\', sans-serif; text-align: center; font-size: 40px;">すこしげんきがないきみへ</h1>',
    unsafe_allow_html=True
)




# YouTubeのリンク
youtube_link = "https://youtu.be/WxAZT-cgLg8?feature=shared"

import streamlit as st

# Hina Mincho フォントのリンク
font_link = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hina+Mincho&display=swap">'
st.markdown(font_link, unsafe_allow_html=True)
font_style = "font-family: 'Hina Mincho', sans-serif; font-size: 20px; color: #999966; text-align: center;"





# ボタンが押されたらランダムな名言を表示
if st.button("🌟"):
    selected_quote = random.choice(quotes)
    st.markdown(f'<div style="{font_style}">{selected_quote}</div>', unsafe_allow_html=True)
    unsafe_allow_html=True
    unsafe_allow_html=True
    img = Image.open('ハートもってる.png')
    st.image(img,caption='　',use_column_width=True)  
    link_style = 'font-family: Darumadrop One, sans-serif; font-size: 20px; color: #999966; text-decoration: none; text-align: center;'
    st.markdown(f'<div style="{link_style}"><a href="{youtube_link}" target="_blank">じんないとものりYouTube</a></div>', unsafe_allow_html=True)
    youtube_links = [
        "https://www.youtube.com/embed/CG65xSRE6Wg",
        "https://www.youtube.com/embed/y41AUYWfG0A",
        "https://www.youtube.com/embed/swN5jiGSNF8",
        "https://www.youtube.com/embed/WxAZT-cgLg8"
    ]

    # リンクスタイル
    link_style = 'font-family: Darumadrop One, sans-serif; font-size: 20px; color: #999966; text-decoration: none; text-align: center;'

# 各動画をリンクとして表示
    for youtube_link in youtube_links:
        st.markdown(f'<div style="{link_style}"><a href="{youtube_link}" target="_blank">じんないとものりYouTube</a></div>', unsafe_allow_html=True)



button_style = """
    <style>
        div.stButton > button {
            display: block;
            margin: 0 auto;
        }
    </style>
"""

# スタイルを適用
st.markdown(button_style, unsafe_allow_html=True)

import streamlit as st

# YouTube動画の埋め込みリンク


import streamlit as st
import requests
from datetime import datetime, timedelta

