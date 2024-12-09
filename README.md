# YouTube to MP3/MP4 Converter ナリ！

YouTubeの動画をMP3やMP4形式でダウンロードできるStreamlitアプリケーションナリ！

## 特徴

- 最大5つまでの動画を一度にダウンロード可能
- MP3（音声のみ）とMP4（動画）の両方に対応
- ダウンロード先フォルダを自由に指定可能
- シンプルで使いやすいUI

## インストール方法

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/yt2mp3.git
cd yt2mp3

# 必要なパッケージをインストール
pip install -r requirements.txt
```

## 使い方

1. Streamlitアプリを起動:
```bash
streamlit run yt2mp3.py
```

2. ブラウザで開いたアプリで以下の操作を行う:
   - ダウンロード先フォルダを指定（任意）
   - YouTubeのURLを入力（最大5つまで）
   - 「MP3に変換するナリ」または「MP4に変換するナリ」ボタンをクリック

## 注意事項

- YouTubeの利用規約に従ってご利用ください
- 著作権を遵守してください
- 個人使用目的でのみご利用ください

## 必要なもの

- Python 3.6以上
- FFmpeg（動画/音声変換に必要） 