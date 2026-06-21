FIFA国際試合の歴史的データと機械学習アルゴリズム（LightGBM）を用いた、2026年W杯本大会の勝敗確率予測システムです。
本リポジトリでは、予測ロジックによって出力されたデータをもとに、直感的に勝率を確認できるStreamlit Webアプリのフロントエンドソースコードを公開しています。

※本プロジェクトのメインである「特徴量エンジニアリングおよびモデル学習用ノートブック」は、W杯全日程終了後に本リポジトリにて追加公開を予定しています。

---

## 📊 データ出典・ソース (Data Sources)
本プロジェクトの予測モデル構築にあたり、客観的な分析の基盤として以下の3つのデータセットおよびAPIを利用しています。

1. **International football results from 1872 to 2026**
   - 1872年から現在に至るまでの、約5万試合におよぶ国際Aマッチの全試合結果データ（スコア、対戦国、開催地等）です。モデルのベースライン学習に使用しています。
2. **FIFA World Ranking Dataset (1990-2024)**
   - 過去30年以上の時系列FIFAランキングおよびポイントのデータセットです。試合開催日時点の正確なレーティング差を算出するための特徴量として、時系列結合（`merge_asof`）を行っています。
3. **API-Sports (Football API)**
   - 2026年W杯本大会の最新の試合スケジュール、対戦カード、およびリアルタイムな試合ステータスを動的に取得するために活用しています。

---

## 🛠️ 技術スタック (Technology Stack)
- **Language:** Python
- **Machine Learning API/Backend:** LightGBM, Pandas, Scikit-learn (※Jupyter Notebook環境で構築)
- **Frontend / UI:** Streamlit Cloud
- **Environment Management:** Python-dotenv, OS Environment Variables

---

## 🚀 アプリケーションの概要
Streamlit Community Cloud上で展開されたWebアプリでは、ユーザーがプルダウンから対戦カードを選択するだけで、AIモデルが弾き出した「ホーム勝ち」「引き分け」「アウェイ勝ち」の確率を、`st.metric` および積み上げ横棒グラフによって直感的に比較・検証することが可能で
