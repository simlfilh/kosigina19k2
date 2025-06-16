import streamlit as st

# Настройка вкладки
st.set_page_config(
    page_title="Общежитие СПбГЭУ №3", # Заголовок вкладки браузера
    page_icon="🏠",                  # Иконка
    layout="wide",                    # Широкий режим 
    initial_sidebar_state="expanded"  # Развёрнутое боковое меню
)

st.markdown("""
    <link rel="apple-touch-icon" href="https://raw.githubusercontent.com/simlfilh/kosigina19k2/main/%D0%B8%D0%BA%D0%BE%D0%BD%D0%BA%D0%B0.jpg">
    <meta name="theme-color" content="#4285f4">
""", unsafe_allow_html=True)

# Фон сайта (линейный градиент от бирюзового к фиолетовому)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom,
            rgb(48, 183, 171),
            rgb(70, 108, 185),
            rgb(92, 33, 199));
        min-height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

pages = {
    "🏠 ОБЩЕЖИТИЕ СПбГЭУ №3": [
        st.Page("1_info_location.py", title="— Как нас найти?")
    ],
    "🧑‍💻 АДМИНИСТРАЦИЯ ОБЩЕЖИТИЯ": [
        st.Page("2_zhbu.py", title="— Жилищно-бытовое управление"),
        st.Page("3_guide.py", title="— Руководство общежития"),
        st.Page("4_student_council.py", title="— Студенческий совет")
    ],
    "🧳 ЗАСЕЛЕНИЕ В ОБЩЕЖИТИЕ": [
        st.Page("5_settling.py", title="— Поселение в общежитие"),
    ],
    "📍 ЧТО ЕСТЬ В ОБЩЕЖИТИИ?": [
        st.Page("6_block.py", title="— Блоки для проживания"),
        st.Page("7_common_room.py", title="— Бытовое пространство"),
        st.Page("8_student_room.py", title="— Студенческое пространство"),
        st.Page("9_guests_room.py", title="— Гостевые блоки")
    ],
    "📋 ДОКУМЕНТЫ": [
        st.Page("10_payment.py", title="— Оплата проживания"),
        st.Page("11_recalculation.py", title="— Перерасчёт проживания"),
        st.Page("12_eviction.py", title="— Выселение из общежития")
    ],
    "🪪 РЕЖИМ В ОБЩЕЖИТИИ": [
        st.Page("13_access_mode.py", title="— Правила пропускного режима"),
        st.Page("14_bureau.py", title="— Бюро пропусков"),
        st.Page("15_rules_of_accommodation.py", title="— Правила проживания")
    ],
    "📱 НАШИ СОЦИАЛЬНЫЕ СЕТИ": [
        st.Page("16_links.py", title="— Ссылки")
    ]
}

pg = st.navigation(pages)
pg.run()
