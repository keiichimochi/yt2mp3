import streamlit as st
import yt_dlp
import os
from pathlib import Path

st.title("YouTube to MP3/MP4 Converter ナリ！")

# ダウンロードフォルダの選択
if 'download_dir' not in st.session_state:
    st.session_state['download_dir'] = "downloads"

col1, col2 = st.columns([3, 1])
with col1:
    download_dir = st.text_input(
        "ダウンロード先のフォルダを指定するナリ（空欄の場合は'downloads'フォルダになるナリ）",
        value=st.session_state['download_dir']
    )

# ホームディレクトリのパスを取得
home = str(Path.home())
st.caption(f"💡 使えるフォルダの例（コピペしてナ）:")
st.caption(f"・ホームフォルダ: {home}")
st.caption(f"・デスクトップ: {os.path.join(home, 'Desktop')}")
st.caption(f"・ダウンロード: {os.path.join(home, 'Downloads')}")

if download_dir:
    try:
        # パスの正規化と存在確認
        download_dir = os.path.expanduser(download_dir)  # ~を展開
        if not os.path.exists(download_dir):
            os.makedirs(download_dir, exist_ok=True)
            st.success(f"フォルダを作成したナリ: {download_dir}")
        st.session_state['download_dir'] = download_dir
    except Exception as e:
        st.error(f"フォルダの作成に失敗したナリ: {str(e)}")
        download_dir = "downloads"
else:
    download_dir = "downloads"

# 最大5つまでのYouTube URLを入力
urls = []
for i in range(5):
    url = st.text_input(f"YouTube URL {i+1}を入力するナリ（任意）", key=f"url_{i}")
    if url:
        urls.append(url)

col1, col2 = st.columns(2)

with col1:
    if st.button("MP3に変換するナリ"):
        if urls:
            for url in urls:
                try:
                    # yt-dlpのオプション設定
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                        'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
                    }
                    
                    # ダウンロードと変換の実行
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        st.info(f"{url} をダウンロード中ナリ...")
                        info = ydl.extract_info(url, download=True)
                        title = info['title']
                        
                    st.success(f"'{title}' のダウンロードが完了したナリ！")
                    
                except Exception as e:
                    st.error(f"エラーが発生したナリ ({url}): {str(e)}")
            
            st.balloons()
        else:
            st.warning("URLを最低1つは入力するナリ！")

with col2:
    if st.button("MP4に変換するナリ"):
        if urls:
            for url in urls:
                try:
                    # yt-dlpのオプション設定
                    ydl_opts = {
                        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                        'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
                    }
                    
                    # ダウンロードと変換の実行
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        st.info(f"{url} をダウンロード中ナリ...")
                        info = ydl.extract_info(url, download=True)
                        title = info['title']
                        
                    st.success(f"'{title}' のダウンロードが完了したナリ！")
                    
                except Exception as e:
                    st.error(f"エラーが発生したナリ ({url}): {str(e)}")
            
            st.balloons()
        else:
            st.warning("URLを最低1つは入力するナリ！")
