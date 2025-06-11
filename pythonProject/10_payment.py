import streamlit as st

st.title("💵 Оплата проживания")
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
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>📆 ЗА СЕМЕСТР</h3> 
                </div>
            </div> 
        <p>Оплата производится за семестр (сентябрь - январь) проживания вперед.</p>
        <p>Если Вы уезжаете за этот период более чем на 5 дней, Вы можете запросить перерасчет.</p>
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>📅 ЕЖЕМЕСЯЧНО</h3> 
                </div>
            </div>
        <p>Оплата за МЕСЯЦ производится ДО 10 числа в ЛК студента, не позже. Иначе, будет задолженность. 
        Так со всеми последующими месяцами.</p>
        <p>Пример: Оплата за сентябрь до 10 сентября, оплата за октябрь до 10 октября и т.д.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>ШАГ 1</h3> 
                </div>
            </div>
        <p>В личном кабинете студента в разделе "Сведения обо мне" перейти 
        во вкладку "Мои договоры".</p>
    </div>
            """, unsafe_allow_html=True)
st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\оплата общежития\\1.png")

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>ШАГ 2</h3> 
                </div>
            </div>
        <p>Выбрать актуальный договор для оплаты, нажать "Печать квитанции". 
        После этого перед вами откроется окно с квитанцией.</p>
    </div>
            """, unsafe_allow_html=True)
st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\оплата общежития\\2.png")

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>ШАГ 3</h3> 
                </div>
            </div>
        <p>Проверить все данные на актуальность и корректность.</p>
    </div>
            """, unsafe_allow_html=True)
st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\оплата общежития\\3.png")

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>ШАГ 4</h3> 
                </div>
            </div>
        <p>Отсканировать через приложение Сбербанка QR-код "ИЗВЕЩЕНИЕ".</p>
    </div>
            """, unsafe_allow_html=True)
st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\оплата общежития\\4.png")

st.markdown("""
    <div class="colored-container">
        <p>Как только QR-код будет прочитан, перед вами всплывут окна для ввода и проверки данных
         и окно для подтверждения оплаты. Внимательно ознакомьтесь со всей информацией.</p>
        <p>Если у вас возникнут вопросы, обращайтесь к старосте своего этажа или напишите нашему Боту 
        Поддержки в tg.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.write("Тел.: (812) 521-00-32")
st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.write("Тел.: (812) 521-00-33")

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
