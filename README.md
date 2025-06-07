# Diary Plus

Django を学んだ証として GitHub に置く用のサンプルプロジェクトです。
機能: Markdown 日記、画像、タグ、全文検索、HTMX いいね、REST API。

## セットアップ
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Docker Compose での実行

Docker と Docker Compose がインストールされている環境で以下を実行します。

```bash
docker compose up --build
```
