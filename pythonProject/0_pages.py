import streamlit as st

st.set_page_config(
    page_title="Общежитие СПбГЭУ №3", 
    page_icon="🏠",                  
    layout="wide",                    
    initial_sidebar_state="expanded"  
)

with st.sidebar:
    st.link_button("Вернуться на главную", 
                 "https://unecondorms.streamlit.app/",
                 type="primary",  
                 use_container_width=True)
    
    # Пустое пространство между кнопкой и возможным меню в сайдбаре
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

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

# Затем навигация
pg = st.navigation(pages)
pg.run()

