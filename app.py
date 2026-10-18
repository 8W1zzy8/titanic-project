
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Titanic Archive",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- ДАННЫЕ ----------
@st.cache_data
def load_data():
    return pd.read_csv("train.csv")


df = load_data()

# ---------- ПАЛИТРА ----------
INK = "#202A30"
GOLD = "#B18A4A"
CREAM = "#F6F3EC"
MUTED = "#7D827F"
TEAL = "#487C78"
RED = "#B65F51"

# ---------- ДИЗАЙН ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

.stApp {
    background: #F6F3EC;
    color: #202A30;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: #F6F3EC !important;
}

[data-testid="stMain"] {
    background: transparent !important;
}

[data-testid="stHeader"] {
    background: #F6F3EC !important;
}

[data-testid="stSidebar"] {
    background: #202A30 !important;
}

[data-testid="stSidebar"] * {
    color: #F6F3EC;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: #303B40;
    border-color: #59615F;
}

[data-testid="stSidebar"] input {
    color: #202A30 !important;
}

.block-container {
    max-width: 1500px;
    padding: 2.2rem 3rem 4rem 3rem;
}

h1, h2, h3 {
    font-family: 'Playfair Display', Georgia, serif !important;
    color: #202A30 !important;
    letter-spacing: -0.5px;
}

p, label {
    color: #555F60;
}

.archive-eyebrow {
    color: #A27A3C;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.archive-hero {
    background: #202A30;
    padding: 38px 42px;
    border-radius: 4px;
    margin: 8px 0 28px 0;
    color: #F6F3EC;
    border-bottom: 4px solid #B18A4A;
}

.archive-hero h1 {
    font-family: 'Playfair Display', Georgia, serif !important;
    color: #F6F3EC !important;
    font-size: clamp(34px, 5vw, 58px) !important;
    line-height: 1.12;
    margin: 12px 0;
}

.archive-hero p {
    color: #C8CBC5;
    font-size: 15px;
    max-width: 650px;
    line-height: 1.8;
}

.archive-label {
    color: #B18A4A;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 700;
}

.metric-card {
    background: #FFFFFF;
    border: 1px solid #E5E0D5;
    border-top: 3px solid #B18A4A;
    padding: 21px 22px;
    min-height: 125px;
}

.metric-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    color: #7D827F;
    margin-bottom: 12px;
}

.metric-value {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 34px;
    color: #202A30;
    line-height: 1.1;
}

.metric-note {
    font-size: 12px;
    color: #7D827F;
    margin-top: 9px;
}

.section-heading {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 27px;
    color: #202A30;
    margin: 28px 0 4px 0;
}

.section-subtitle {
    color: #7D827F;
    font-size: 13px;
    margin-bottom: 18px;
}

.insight-card {
    background: #EAE5D9;
    border-left: 3px solid #B18A4A;
    padding: 22px 24px;
    margin: 8px 0;
    color: #202A30;
    line-height: 1.7;
}

.profile-card {
    background: #202A30;
    color: #F6F3EC;
    padding: 30px;
    border-bottom: 4px solid #B18A4A;
}

.profile-card h2 {
    color: #F6F3EC !important;
    font-size: 30px;
}

.profile-kicker {
    color: #D3B77F;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.profile-number {
    color: #D3B77F;
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 26px;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E5E0D5;
    border-top: 3px solid #B18A4A;
    padding: 18px;
    border-radius: 2px;
}

div[data-testid="stMetricLabel"] {
    color: #7D827F !important;
}

div[data-testid="stMetricValue"] {
    color: #202A30 !important;
    font-family: 'Playfair Display', Georgia, serif;
}

.stButton button, .stDownloadButton button {
    background: #202A30;
    color: #F6F3EC;
    border: 1px solid #202A30;
    border-radius: 2px;
    padding: 10px 18px;
    font-weight: 600;
}

.stButton button:hover, .stDownloadButton button:hover {
    background: #B18A4A;
    border-color: #B18A4A;
    color: white;
}

[data-testid="stDataFrame"] {
    border: 1px solid #E5E0D5;
}

hr {
    border-color: #DDD6C8;
}

[data-baseweb="select"] > div,
[data-baseweb="input"] > div {
    border-radius: 2px;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 22px;
    border-bottom: 1px solid #DDD6C8;
}

.stTabs [data-baseweb="tab"] {
    color: #7D827F;
    padding: 12px 4px;
}

.stTabs [aria-selected="true"] {
    color: #202A30 !important;
    border-bottom-color: #B18A4A !important;
}

@media (max-width: 800px) {
    .block-container {
        padding: 1rem;
    }
    .archive-hero {
        padding: 25px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------- БОКОВАЯ ПАНЕЛЬ ----------
st.sidebar.markdown("""
<div style="padding: 16px 0 22px 0;">
    <div style="font-size:11px;letter-spacing:3px;color:#D3B77F;">
        HISTORICAL DATA PROJECT
    </div>
    <div style="font-family:Georgia;font-size:30px;
                color:#F6F3EC;margin-top:12px;">
        Titanic<br>Archive.
    </div>
    <div style="color:#AEB7B4;font-size:12px;margin-top:10px;">
        Пассажиры · 1912
    </div>
</div>
<hr style="border-color:#455052;">
""", unsafe_allow_html=True)

st.sidebar.markdown("### Параметры исследования")

sex_options = {
    "Все пассажиры": "Все",
    "Мужчины": "male",
    "Женщины": "female"
}

selected_sex_label = st.sidebar.selectbox(
    "Пол пассажира",
    list(sex_options.keys())
)
selected_sex = sex_options[selected_sex_label]

class_options = {
    "Все классы": "Все",
    "Первый класс": 1,
    "Второй класс": 2,
    "Третий класс": 3
}

selected_class_label = st.sidebar.selectbox(
    "Класс билета",
    list(class_options.keys())
)
selected_class = class_options[selected_class_label]

if "Age" in df.columns:
    age_range = st.sidebar.slider(
        "Возраст пассажиров",
        min_value=0,
        max_value=80,
        value=(0, 80)
    )
else:
    age_range = (0, 80)

search_name = st.sidebar.text_input(
    "Поиск по имени",
    placeholder="Например, John..."
)

st.sidebar.markdown("---")
st.sidebar.caption("Titanic Archive · Data & History")


# ---------- ФИЛЬТРАЦИЯ ----------
filtered = df.copy()

if selected_sex != "Все" and "Sex" in filtered.columns:
    filtered = filtered[filtered["Sex"] == selected_sex]

if selected_class != "Все" and "Pclass" in filtered.columns:
    filtered = filtered[filtered["Pclass"] == selected_class]

if "Age" in filtered.columns:
    filtered = filtered[
        filtered["Age"].isna()
        | filtered["Age"].between(age_range[0], age_range[1])
    ]

if search_name.strip() and "Name" in filtered.columns:
    filtered = filtered[
        filtered["Name"].str.contains(
            search_name.strip(), case=False, na=False
        )
    ]

# Статистика по всему исходному набору
total_passengers = len(df)
total_survived = int(df["Survived"].sum())
total_died = total_passengers - total_survived
overall_rate = (
    total_survived / total_passengers * 100
    if total_passengers else 0
)

# Статистика по текущему фильтру
n = len(filtered)
survived = int(filtered["Survived"].sum()) if n else 0
died = n - survived
survival_rate = survived / n * 100 if n else 0


# ---------- ГЛАВНЫЙ ЗАГОЛОВОК ----------
st.markdown(f"""
<div class="archive-eyebrow">THE HISTORICAL DATA COLLECTION · NO. 001</div>
<div class="archive-hero">
    <div class="archive-label">A STUDY OF THE RMS TITANIC</div>
    <h1>История, рассказанная<br>через данные.</h1>
    <p>
        Кто находился на борту «Титаника»? У кого было больше шансов
        выжить? Исследуем судьбы пассажиров через статистику,
        визуализации и реальные данные исторического архива.
    </p>
    <div style="font-size:11px;letter-spacing:2px;color:#D3B77F;margin-top:24px;">
        15 APRIL 1912 &nbsp; / &nbsp; PASSENGER RECORDS
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- КЛЮЧЕВЫЕ ПОКАЗАТЕЛИ ----------
st.markdown('<div class="archive-eyebrow">01 / THE BIG PICTURE</div>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">Пассажиры в цифрах</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Общая статистика набора данных и текущей выборки.</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">В наборе данных</div>
        <div class="metric-value">{total_passengers:,}</div>
        <div class="metric-note">Всего записей</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Выжившие</div>
        <div class="metric-value">{total_survived:,}</div>
        <div class="metric-note">Из исходного набора</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Погибшие</div>
        <div class="metric-value">{total_died:,}</div>
        <div class="metric-note">Из исходного набора</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Выживаемость</div>
        <div class="metric-value">{overall_rate:.1f}%</div>
        <div class="metric-note">Доля выживших</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")
st.markdown(
    f"**Текущая выборка:** {n:,} пассажиров · "
    f"**Выжили:** {survived:,} · "
    f"**Погибли:** {died:,} · "
    f"**Выживаемость:** {survival_rate:.1f}%"
)

st.markdown("---")


# ---------- ВКЛАДКИ ----------
overview_tab, passengers_tab, insights_tab = st.tabs([
    "01  Обзор",
    "02  Пассажиры",
    "03  Выводы"
])


# ---------- ОБЗОР ----------
with overview_tab:
    left, right = st.columns([1.05, 1])

    with left:
        st.markdown(
            '<div class="section-heading">Выживание и трагедия</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="section-subtitle">Соотношение исходов среди отобранных пассажиров.</div>',
            unsafe_allow_html=True
        )

        if n:
            outcome = pd.DataFrame({
                "Исход": ["Выжили", "Погибли"],
                "Количество": [survived, died]
            })
            fig = px.pie(
                outcome,
                names="Исход",
                values="Количество",
                hole=0.68,
                color="Исход",
                color_discrete_map={
                    "Выжили": TEAL,
                    "Погибли": RED
                }
            )
            fig.update_traces(
                textposition="outside",
                textinfo="label+percent",
                marker=dict(line=dict(color=CREAM, width=3))
            )
            fig.update_layout(
                showlegend=False,
                margin=dict(t=20, b=25, l=20, r=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="DM Sans", color=INK, size=12),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Нет пассажиров для отображения. Измени фильтры.")

    with right:
        st.markdown(
            '<div class="section-heading">Выживаемость по полу</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="section-subtitle">Сравнение доли выживших среди мужчин и женщин.</div>',
            unsafe_allow_html=True
        )

        if n and "Sex" in filtered.columns:
            sex_stats = (
                filtered.groupby("Sex", observed=True)["Survived"]
                .mean().mul(100).reset_index()
            )
            sex_stats["Пол"] = sex_stats["Sex"].map({
                "male": "Мужчины",
                "female": "Женщины"
            }).fillna(sex_stats["Sex"])

            fig = px.bar(
                sex_stats,
                x="Пол",
                y="Survived",
                color="Пол",
                text=sex_stats["Survived"].map(lambda x: f"{x:.1f}%"),
                color_discrete_map={
                    "Мужчины": INK,
                    "Женщины": GOLD
                }
            )
            fig.update_traces(
                textposition="outside",
                cliponaxis=False
            )
            fig.update_layout(
                showlegend=False,
                yaxis_title="Выживаемость, %",
                xaxis_title="",
                yaxis=dict(range=[0, 110], gridcolor="#E5E0D5"),
                margin=dict(t=25, b=20, l=10, r=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="DM Sans", color=INK),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Недостаточно данных для сравнения.")

    st.markdown("---")

    st.markdown(
        '<div class="section-heading">Класс билета и шансы на спасение</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">Как менялась доля выживших в зависимости от класса.</div>',
        unsafe_allow_html=True
    )

    if n and "Pclass" in filtered.columns:
        class_stats = (
            filtered.groupby("Pclass", observed=True)["Survived"]
            .mean().mul(100).reset_index()
        )
        class_stats["Класс"] = class_stats["Pclass"].map({
            1: "Первый класс",
            2: "Второй класс",
            3: "Третий класс"
        })

        fig = px.bar(
            class_stats,
            x="Класс",
            y="Survived",
            text=class_stats["Survived"].map(lambda x: f"{x:.1f}%"),
            color="Pclass",
            color_continuous_scale=["#D7C5A2", GOLD, INK]
        )
        fig.update_traces(textposition="outside", cliponaxis=False)
        fig.update_layout(
            showlegend=False,
            coloraxis_showscale=False,
            yaxis_title="Выживаемость, %",
            xaxis_title="",
            yaxis=dict(range=[0, 110], gridcolor="#E5E0D5"),
            margin=dict(t=30, b=20, l=10, r=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="DM Sans", color=INK),
            height=370
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Нет данных для сравнения классов.")

    if "Age" in filtered.columns and n:
        st.markdown("---")
        st.markdown(
            '<div class="section-heading">Возраст пассажиров</div>',
            unsafe_allow_html=True
        )
        age_data = filtered.dropna(subset=["Age"])
        if not age_data.empty:
            fig = px.histogram(
                age_data,
                x="Age",
                color="Survived",
                nbins=25,
                barmode="overlay",
                opacity=0.8,
                color_discrete_map={
                    0: RED,
                    1: TEAL
                },
                labels={
                    "Age": "Возраст",
                    "Survived": "Исход",
                    "count": "Количество"
                }
            )
            fig.update_layout(
                legend_title_text="Исход (0 — погиб, 1 — выжил)",
                yaxis_title="Количество пассажиров",
                xaxis_title="Возраст",
                margin=dict(t=20, b=20, l=10, r=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="DM Sans", color=INK),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)


# ---------- ПАССАЖИРЫ ----------
with passengers_tab:
    st.markdown(
        '<div class="section-heading">Архив пассажиров</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">Изучай записи, ищи имена и выгружай отфильтрованные данные.</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"**Найдено записей:** {len(filtered):,}")

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
        height=390
    )

    csv_data = filtered.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="↓  Скачать выбранные данные CSV",
        data=csv_data,
        file_name="titanic_filtered_data.csv",
        mime="text/csv"
    )

    st.markdown("---")
    st.markdown(
        '<div class="section-heading">Карточка пассажира</div>',
        unsafe_allow_html=True
    )

    if not filtered.empty and "Name" in filtered.columns:
        passenger_names = filtered["Name"].dropna().tolist()
        selected_name = st.selectbox(
            "Выбери пассажира для просмотра",
            passenger_names
        )

        passenger = filtered[filtered["Name"] == selected_name].iloc[0]

        passenger_class = passenger.get("Pclass", "—")
        age = passenger.get("Age", None)
        sex = passenger.get("Sex", "—")
        fare = passenger.get("Fare", None)
        ticket = passenger.get("Ticket", "—")
        survived_value = int(passenger.get("Survived", 0))

        age_text = f"{age:g}" if pd.notna(age) else "Не указан"
        fare_text = f"{fare:.2f}" if pd.notna(fare) else "Не указан"
        sex_text = {
            "male": "Мужчина",
            "female": "Женщина"
        }.get(sex, str(sex))
        class_text = {
            1: "Первый класс",
            2: "Второй класс",
            3: "Третий класс"
        }.get(passenger_class, str(passenger_class))

        status_text = (
            "Выжил"
            if survived_value == 1
            else "Погиб"
        )
        status_color = TEAL if survived_value == 1 else RED

        st.markdown(f"""
        <div class="profile-card">
            <div class="profile-kicker">PASSENGER RECORD</div>
            <h2>{selected_name}</h2>
            <div style="margin:16px 0;color:{status_color};font-weight:700;">
                ● {status_text}
            </div>
            <div style="display:flex;flex-wrap:wrap;gap:38px;margin-top:25px;">
                <div>
                    <div class="profile-kicker">Возраст</div>
                    <div class="profile-number">{age_text}</div>
                </div>
                <div>
                    <div class="profile-kicker">Пол</div>
                    <div class="profile-number" style="font-size:21px;">{sex_text}</div>
                </div>
                <div>
                    <div class="profile-kicker">Класс</div>
                    <div class="profile-number" style="font-size:21px;">{class_text}</div>
                </div>
                <div>
                    <div class="profile-kicker">Стоимость билета</div>
                    <div class="profile-number">{fare_text}</div>
                </div>
            </div>
            <div style="margin-top:24px;color:#AEB7B4;font-size:12px;">
                Ticket reference: {ticket}
            </div>
        </div>
        """, unsafe_allow_html=True)

        family_count = (
            int(passenger.get("SibSp", 0) or 0)
            + int(passenger.get("Parch", 0) or 0)
        )
        st.caption(
            f"Число родственников на борту по записи: {family_count}"
        )
    else:
        st.info("По выбранным фильтрам пассажиры не найдены.")


# ---------- ВЫВОДЫ ----------
with insights_tab:
    st.markdown(
        '<div class="section-heading">Что рассказывают данные?</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">Краткие выводы на основе исходного набора.</div>',
        unsafe_allow_html=True
    )

    if "Sex" in df.columns:
        women = df[df["Sex"] == "female"]
        men = df[df["Sex"] == "male"]

        women_rate = (
            women["Survived"].mean() * 100 if len(women) else 0
        )
        men_rate = (
            men["Survived"].mean() * 100 if len(men) else 0
        )

        st.markdown(f"""
        <div class="insight-card">
            <div class="archive-label">FINDING 01</div>
            <h3>Разница в выживаемости</h3>
            В исходном наборе выживаемость женщин составляет
            <b>{women_rate:.1f}%</b>, а мужчин — <b>{men_rate:.1f}%</b>.
            Это заметное различие показывает, как пол был связан
            с шансами на спасение.
        </div>
        """, unsafe_allow_html=True)

    if "Pclass" in df.columns:
        class_rates = df.groupby("Pclass")["Survived"].mean() * 100
        best_class = class_rates.idxmax()
        best_rate = class_rates.max()

        class_names = {
            1: "первый",
            2: "второй",
            3: "третий"
        }

        st.markdown(f"""
        <div class="insight-card">
            <div class="archive-label">FINDING 02</div>
            <h3>Класс билета имеет значение</h3>
            Наибольшая доля выживших была среди пассажиров,
            путешествовавших в <b>{class_names.get(best_class, str(best_class))} классе</b>:
            <b>{best_rate:.1f}%</b>. Социальное положение и доступ
            к местам на шлюпках могли влиять на шансы спасения.
        </div>
        """, unsafe_allow_html=True)

    if "Age" in df.columns:
        children = df[df["Age"] < 16]
        adults = df[df["Age"] >= 16]

        if len(children) and len(adults):
            child_rate = children["Survived"].mean() * 100
            adult_rate = adults["Survived"].mean() * 100

            st.markdown(f"""
            <div class="insight-card">
                <div class="archive-label">FINDING 03</div>
                <h3>Возраст и спасение</h3>
                В группе младше 16 лет выживаемость составила
                <b>{child_rate:.1f}%</b>, а среди пассажиров от 16 лет —
                <b>{adult_rate:.1f}%</b>. При этом возраст указан не для
                всех записей, поэтому сравнение нужно трактовать осторожно.
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### О наборе данных")
    st.write(
        "Проект использует учебный набор данных Titanic. "
        "Выводы описывают записи в этом наборе, а не обязательно "
        "полную совокупность всех людей, находившихся на борту."
    )


# ---------- ПОДВАЛ ----------
st.markdown("---")
st.markdown("""
<div style="display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;
            color:#7D827F;font-size:11px;letter-spacing:1px;padding:8px 0;">
    <span>TITANIC ARCHIVE · DATA EXPLORATION</span>
    <span>PYTHON · PANDAS · STREAMLIT · PLOTLY</span>
</div>
""", unsafe_allow_html=True)
