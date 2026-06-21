
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="W杯2026 勝敗予測システム", layout="centered")

st.title("🏆 W杯2026 勝敗予測アプリ")
st.caption("LightGBM 予測パイプライン・デモ画面")

@st.cache_data
def load_data():
    # Jupyter側で出力した予測結果を読み込む
    df = pd.read_csv("output_csv/df3_wcup_2026_predictions.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

try:
    df_pred = load_data()
    
    # プルダウン表示用のラベルを作成
    df_pred['match_label'] = df_pred['date'].dt.strftime('%Y-%m-%d') + " | " + df_pred['home_team'] + " vs " + df_pred['away_team']
    match_list = df_pred['match_label'].tolist()
    
    # UI: 試合選択
    selected_match = st.selectbox("🔮 予測を確認したい対戦カードを選択してください", match_list)
    
    # 選択された試合のデータを取得
    row = df_pred[df_pred['match_label'] == selected_match].iloc[0]
    
    home = row['home_team']
    away = row['away_team']
    h_prob = row['Home_Win_Prob']
    d_prob = row['Draw_Prob']
    a_prob = row['Away_Win_Prob']
    
    st.markdown("---")
    st.subheader("📊 勝敗予測確率")
    
    # 数値の強調表示
    col1, col2, col3 = st.columns(3)
    col1.metric(label=f"🏠 {home} 勝ち", value=f"{h_prob:.1%}")
    col2.metric(label="🤝 引き分け", value=f"{d_prob:.1%}")
    col3.metric(label=f"🚀 {away} 勝ち", value=f"{a_prob:.1%}")
    
    # 積み上げ横棒グラフ用のデータ成形
    chart_data = pd.DataFrame({
        f"{home} Win": [h_prob],
        "Draw": [d_prob],
        f"{away} Win": [a_prob]
    })
    
    # 確率を可視化する横棒グラフ
    st.bar_chart(chart_data, horizontal=True, color=["#1f77b4", "#aec7e8", "#ff7f0e"])
    
    # 参考データの表示
    st.markdown("---")
    st.markdown(f"**分析用スタッツ (当時のFIFAランク):**")
    st.write(f"・{home}: {row['home_rank']:.0f}位  /  ・{away}: {row['away_rank']:.0f}位")

except Exception as e:
    st.error("データの読み込みに失敗しました。ファイルの出力状況を確認してください。")
    st.caption(f"エラー詳細: {e}")


