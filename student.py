import streamlit as st
import pandas as pd

# 1. 데이터 불러오기
df = pd.read_csv('study.csv')

st.title("공부 습관 대시보드 📊")

# 2. 핵심 지표 한 줄에 보여주기 (컬럼 3개로 나누기)
col1, col2, col3 = st.columns(3)
col1.metric("학생 수", len(df))
col2.metric("평균 점수", int(df['점수'].mean()))
col3.metric("평균 공부시간", int(df['공부시간'].mean()))

# 3. 슬라이더로 최소 공부시간 선택하기
# 0부터 데이터의 최대 공부시간까지 선택할 수 있게 만듭니다.
max_time = int(df['공부시간'].max())
min_study_time = st.slider('최소 공부시간', 0, max_time, 0)

# 4. 슬라이더에서 고른 시간 이상 공부한 학생만 거르기
filtered_df = df[df['공부시간'] >= min_study_time]

# 5. 차트 그리기 (기본 내장 함수 사용)
st.write("📈 공부시간과 점수의 관계 (산점도)")
st.scatter_chart(data=filtered_df, x='공부시간', y='점수')

st.write("📊 학생별 점수 (막대그래프)")
st.bar_chart(data=filtered_df, x='학생ID', y='점수')
