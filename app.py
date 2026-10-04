import streamlit as st
import pandas as pd
import plotly.express as px

# Настройка страницы
st.set_page_config(
    page_title="Titanic Analysis",
    page_icon="🚢",
    layout="wide"
)

# Заголовок
st.title("🚢 Titanic — анализ пассажиров")
st.write("Интерактивный анализ данных пассажиров Титаника.")

# Загружаем данные
df = pd.read_csv("train.csv")

# -----------------------------
# Основная статистика
# -----------------------------

st.header("📊 Основная статистика")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Всего пассажиров", len(df))

with col2:
    st.metric("Выжили", int(df["Survived"].sum()))

with col3:
    st.metric("Мужчины", int((df["Sex"] == "male").sum()))

with col4:
    st.metric("Женщины", int((df["Sex"] == "female").sum()))

# -----------------------------
# Фильтры
# -----------------------------

st.header("🔎 Фильтры")

sex_filter = st.selectbox(
    "Выберите пол:",
    ["Все", "male", "female"]
)

class_filter = st.selectbox(
    "Выберите класс:",
    ["Все", 1, 2, 3]
)

filtered_df = df.copy()

if sex_filter != "Все":
    filtered_df = filtered_df[filtered_df["Sex"] == sex_filter]

if class_filter != "Все":
    filtered_df = filtered_df[filtered_df["Pclass"] == class_filter]

# -----------------------------
# График выживаемости
# -----------------------------
st.header("💡 Основные выводы")

survival_rate = df["Survived"].mean() * 100

st.write(
    f"Общий процент выживших пассажиров: {survival_rate:.1f}%"
)

female_survival = df[df["Sex"] == "female"]["Survived"].mean() * 100
male_survival = df[df["Sex"] == "male"]["Survived"].mean() * 100

st.write(
    f"Выживаемость женщин: {female_survival:.1f}%"
)

st.write(
    f"Выживаемость мужчин: {male_survival:.1f}%"
)
st.header("🛟 Выживаемость")

survival_data = (
    filtered_df["Survived"]
    .value_counts()
    .rename(index={0: "Погибли", 1: "Выжили"})
    .reset_index()
)

survival_data.columns = ["Результат", "Количество"]

fig = px.bar(
    survival_data,
    x="Результат",
    y="Количество",
    title="Количество выживших и погибших"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Выживаемость мужчин и женщин
# -----------------------------

st.header("👨‍🦱👩 Выживаемость по полу")

sex_data = (
    filtered_df.groupby("Sex")["Survived"]
    .mean()
    .reset_index()
)

sex_data["Survived"] = sex_data["Survived"] * 100

fig2 = px.bar(
    sex_data,
    x="Sex",
    y="Survived",
    title="Процент выживших по полу",
    labels={
        "Sex": "Пол",
        "Survived": "Выживаемость (%)"
    }
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Таблица
# -----------------------------

st.header("📋 Данные пассажиров")

st.dataframe(
    filtered_df,
    use_container_width=True
)
