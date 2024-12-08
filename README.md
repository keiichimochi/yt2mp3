# YouTube to MP3 Converter ナリ！

YouTubeの動画をMP3形式に変換するWebアプリケーションナリ！

## インストール方法

```bash
# リポジトリをクローン
git clone https://github.com/keiichimochi/yt2mp3.git
cd yt2mp3

# 仮想環境を作成して有効化
uv venv venv
.\venv\Scripts\activate

# 依存関係をインストール
uv pip install -r requirements.txt
```

## 使い方

1. 以下のコマンドでアプリを起動するナリ：

```bash
streamlit run yt2mp3.py
```

2. ブラウザが開いたらYouTubeのURLを入力して「MP3に変換するナリ」ボタンを押すナリ！
3. 変換されたMP3ファイルは`downloads`フォルダに保存されるナリ！

## 注意事項

- このアプリは個人使用目的のみで使用するナリ！
- 著作権を尊重するナリ！ 