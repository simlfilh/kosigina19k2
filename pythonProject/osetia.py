import streamlit as st

st.title("Лучшие студенты общежития")
st.divider()

st.markdown("""
            <style>
                .colored-container {
                   background-color: #FFFFFF;  /* Белый цвет фона */
                   border-radius: 10px;      /* Закругление углов на 10px */
                   padding: 20px;            /* Внутренние отступы 20px */
                   margin-bottom: 20px;      /* Внешний отступ снизу 20px */
                   color: black !important;  /* Черный цвет текста */
                   line-height: 1.0;
                   font-size: 21px;
                }
                .highlight-blue {
                    background-color: #B3E5FC;  /* Светло-голубой фон */
                    border-radius: 10px;      /* Закругление углов на 10px */
                    padding: 20px;            /* Внутренние отступы 20px */
                    margin-bottom: 20px;      /* Внешний отступ снизу 20px */
                    color: black !important;  /* Черный цвет текста */
                    line-height: 1.0;
                    text-indent: 20px;
                }
                .highlight-red {
                    background-color: #FFCDD2;  /* Светло-зеленый фон */
                    border-radius: 10px;      /* Закругление углов на 10px */
                    padding: 20px;            /* Внутренние отступы 20px */
                    margin-bottom: 20px;      /* Внешний отступ снизу 20px */
                    color: black !important;  /* Черный цвет текста */
                    line-height: 1.0;
                    text-indent: 20px;
                }
            </style>

            <div class="colored-container">
                <h3 class="highlight-blue">Количество проживающих осетин в общежитии</h3>
            </div>
            """, unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns([1, 3])
with col2:
    st.markdown("""
            <div class="colored-container">
                <h3 class="highlight-red">🥇 БАГАУРИ ДИАНА БАКУРИЕВНА</h3>
            </div>
            """, unsafe_allow_html=True)
with col1:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\Диана.jpg")

st.markdown("""
            <div class="colored-container">
                <p>и два Азамата</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
            <div class="colored-container">
                <p>Всего 3, но нам хватает, даже много</p>
            </div>
            """, unsafe_allow_html=True)

st.divider()

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
