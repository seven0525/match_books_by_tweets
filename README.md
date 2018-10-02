# match_books_by_tweets

ユーザーの過去のツイートからその人の性格にあった本を自動でサジェストしてくれるツール

アイデア主、責任者：渡辺大智（seven0525）

共同開発者：@Mocchaso

## 動かし方

1. `git clone https://github.com/seven0525/match_books_by_tweets.git`

1. クローンしてきたリポジトリ内で、`python app.py`

1. ローカルホストでアプリが起動される

## 必要なツール

### API

以下のAPIのトークンを取得すると、このアプリを実行できます。
    
* Twitter API

* IBM Watson Personality Insights API

### ライブラリ

* watson_developer_cloud (PersonalityInsightsV3)

* flask (Flask, render_template, redirect, request)

* requests_oauthlib (OAuth1Session)

* twitter (Twitter, OAuth)