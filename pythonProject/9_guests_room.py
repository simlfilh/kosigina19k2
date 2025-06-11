import streamlit as st

st.title("🏨 Гостевые блоки")
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
        <p>В общежитии №3 на 1 этаже сейчас подготовлены 4 гостевых блока.</p>
        <p>Заселяться могут только ближайшие родственники: мама, папа, братья, сестры, бабушки, дедушки. 👩‍👧‍👦</p>
        <p>Для заселения родственника в гостевой блок, студент самостоятельно подходит к 
        заведующему/коменданту/завхозу ЗА НЕДЕЛЮ до приезда родственника и получает пропуск для заезжающего, 
        оплачивает срок проживания и т.д. ✍️</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Оснащение комнаты:</h3> 
                </div>
            </div> 
        <p>В комнате есть:</p>
        <p>🫖 Электрический чайник</p>
        <p>🛋️ Вся необходимая мебель: стол, стул, кровать с матрасом.</p>
        <p>🛌 Общежитие выдает: постельное белье, подушку, одеяло, можно попросить полотенце.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Стоимость: <b>650 р/сутки с человека</b>.</p>
        <p>Все включено в посуточную стоимость, больше ни за что платить не нужно.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Пока запросов мало, в блоке живёт одна семья. 
        Если запросов станет много, в блоке/комнате могут жить 
        несколько семей.</p>
        <p>🚫 Студент с родителями в одном блоке жить не может.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.write("Тел.: (812) 521-00-32")
st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.write("Тел.: (812) 521-00-33")

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
