import streamlit as st
import yt_dlp
import os

st.title("YouTube to MP3 Converter ナリ！")

# YouTubeのURLを入力するテキストボックス
url = st.text_input("YouTube URLを入力するナリ")

if st.button("MP3に変換するナリ"):
    if url:
        try:
            # yt-dlpのオプション設定
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': 'downloads/%(title)s.%(ext)s',
            }
            
            # ダウンロードディレクトリの作成
            os.makedirs('downloads', exist_ok=True)
            
            # ダウンロードと変換の実行
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                st.info("ダウンロード中ナリ...")
                info = ydl.extract_info(url, download=True)
                title = info['title']
                
            st.success(f"'{title}' のダウンロードが完了したナリ！")
            st.balloons()
            
        except Exception as e:
            st.error(f"エラーが発生したナリ: {str(e)}")
    else:
        st.warning("URLを入力するナリ！")
