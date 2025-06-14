import streamlit as st

st.title("👩🏽‍💻 Руководство общежития СПбГЭУ №3")
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
            padding: 10px;
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
        <p><b>Администрация общежития</b> — это группа сотрудников, отвечающих за организацию проживания студентов, 
            поддержание порядка, безопасность и решение бытовых вопросов.</p>
        <br>
        <p>В неё входят:</p>
        <p>• Заведующий общежитием;</p>
        <p>• Комендант | Заместитель заведующего;</p>
        <p>• Заведующий хозяйственной частью;</p>
        <p>• Студенческий совет;</p>
        <p>• Технический персонал (электрик, сантехник, уборщицы и т.п.).</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Студенты могут обращаться к администрации общежития по широкому кругу вопросов, связанных с проживанием, бытовыми условиями и соблюдением правил.</p>
        <br>
        <p class="highlight-blue"><b>1.</b> Организационные вопросы.</p>
        <p>• Заселение/выселение</p>
        <p>— Получение места в общежитии.</p>
        <p>— Переселение в другую комнату.</p>
        <p>— Временное сохранение места на время академического отпуска.</p>
        <p>• Документы</p>
        <p>— Оформление договора найма, справок о проживании.</p>
        <br>
        <p class="highlight-blue"><b>2.</b> Бытовые проблемы.</p>
        <p>• Санитария и уборка</p>
        <p>— Наличие насекомых или грызунов.</p>
        <p>• Мебель и оборудование</p>
        <p>— Поломка мебели.</p>
        <p>— Неработоспособность плиты.</p>
        <br>
        <p class="highlight-blue"><b>3.</b> Коммунальные услуги и оплата.</p>
        <p>• Платежи за проживание</p>
        <p>— Перерасчет при отъезде более чем на 5 дней.</p>
        <p>— Льготы и отсрочки платежей.</p>
        <p>• Энергосбережение</p>
        <p>— Жалобы на отключение света/воды по графику.</p>
        <br>
        <p class="highlight-blue"><b>4.</b> Безопасность.</p>
        <p>• Пожарная безопасность</p>
        <p>— Неисправные датчики дыма, забитые эвакуационные выходы.</p>
        <br>
        <p class="highlight-blue"><b>5.</b> Инфраструктура и благоустройство.</p>
        <p>• Ремонт</p>
        <p>— Трещины в стенах, плесень, требующая устранения.</p>
        <p>— Недостаточное освещение в коридорах или на территории.</p>
        <p>• Комфорт</p>
        <p>— Проблемы с отоплением зимой.</p>
        <br>
    </div>
            """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("администрация/заведующий.jpg", width=250)
with col2:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заведующий общежитием</h3> 
                    </div>
                </div>
            <br>
            <p><b>Васильев Александр Владимирович<b></p>  
            <p>🚪 Кабинет на 1-ом этаже</p>  
            <p>📞 (812) 521-00-32</p> 
            <p>📩 <a href="mailto:KOS19@UNECON.RU">KOS19@UNECON.RU</a></p>
        </div>
                """, unsafe_allow_html=True)

col3, col4 = st.columns([1, 3])
with col3:
    st.image("администрация/комендант.jpg", width=250)
with col4:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Комендант общежития</h3> 
                    </div>
                </div>
            <br>
            <p><b>Левашова Людмила Григорьевна<b></p>
            <p>🚪 Кабинет на 1-ом этаже</p>
            <p>📞 (812) 521-00-33</p>  
            <p>📩 <a href="mailto:KOS19@UNECON.RU">KOS19@UNECON.RU</a></p>
        </div>
                """, unsafe_allow_html=True)

col5, col6 = st.columns([1, 3])
with col5:
    st.image("администрация/завхоз.jpg", width=250)
with col6:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Зав. хоз. общежития</h3> 
                    </div>
                </div>
            <br>
            <p><b>Максимова Ольга Юрьевна<b></p>
            <p>🚪 Кабинет в правом крыле 1-го этажа</p>  
            <p>📞 -</p>  
            <p>📩 <a href="mailto:maksimova.o@unecon.ru">maksimova.o@unecon.ru</a></p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.write("Тел.: (812) 521-00-32")
st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.write("Тел.: (812) 521-00-33")

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
