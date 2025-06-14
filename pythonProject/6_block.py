import streamlit as st

st.title("🏘️ Блоки для проживания")
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
        .highlight-green {
            background-color: #C8E6C9;  /* Светло-зеленый фон */
            border-radius: 10px;
            padding-left: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .highlight-red {
            background-color: #FFCDD2;  /* Светло-зеленый фон */
            border-radius: 10px;
            padding-left: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .highlight-blue {
            background-color: #B3E5FC;
            border-radius: 10px;
            padding-left: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .text-indent-content {
            position: relative;
            color: black;
            line-height: 1.4;
        }
    </style>
    <div class="colored-container">
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Комната на двоих</h3> 
                </div>
            </div>
        <p>💵 Стоимость до 6500 руб.</p>
    </div>
            """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("блоки/двушка 1.jpg")
with col2:
    st.image("блоки/двушка 2.jpg")
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Комната на троих</h3> 
                </div>
            </div>
        <p>💵 Стоимость до 6000 руб.</p>
    </div>
            """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.image("блоки/трешка 1.jpg")
with col4:
    st.image("блоки/трешка 2.jpg")
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Дополнительное койко-место</h3> 
                </div>
            </div>
        <p><b>Что такое дополнительное койко-место?</b></p>
        <br>
        <p>У студента есть возможность оформить дополнительное койко-место в том случае, 
        если ему <b>комфортно жить в комнате одному.</b></p>
        <br>
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Документы для оформления:</h3> 
                </div>
            </div>
        <p><b>1.</b> Актуальная флюорография.</p>
        <p><b>2.</b> Справка из кадров.</p>
        <p><b>3.</b> Справка о том, что вы являетесь студентом.</p>
        <p><b>4.</b> Написать заявление на оформление дополнительного койко-места 
        у заведующегося общежития или в Жилищно-бытовом управлении.</p>
        <br>
        <p>💵 Фиксированная стоимость: 4500 руб, без учета стоимости своей койки.</p>
        <p>Приблизительная стоимость комнаты на двоих с оформленным дополнительным койко-местом: 11000 руб.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.markdown("""
<p>📞 <a href="tel:+78125210032">(812) 521-00-32</a></p>
""", unsafe_allow_html=True)
st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.markdown("""
<p>📞 <a href="tel:+78125210033">(812) 521-00-33</a></p>
""", unsafe_allow_html=True)

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
