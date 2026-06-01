import streamlit as st

st.title("👩🏽‍💻 Руководство общежития СПбГЭУ №3")
st.divider()

st.markdown("""
    <style>
        .colored-container {
            background-color: #FFFFFF; 
            border-radius: 10px;     
            padding: 20px;            
            margin-bottom: 20px;      
            color: black !important;  
            line-height: 1.0;
            font-size: 21px;
        }
        .highlight-green {
            background-color: #C8E6C9;  
            border-radius: 10px;
            padding-left: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .highlight-red {
            background-color: #FFCDD2;  
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
        <p>В администрацию общежития входят:</p>
        <p>• заведующий студенческим общежитием;</p>
        <p>• заместитель заведующего студенческим общежитием;</p>
        <p>• комендант;</p>
        <p>• заведующий хозяйственной частью;</p>
        <p>• паспортист (наб. канала Грибоедова, д. 30-32, лестница №4, кабинет №1).</p>
        <br>
        <p>В общежитии также организовано студенческое самоуправление в виде Студенческого совета общежития.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Студенты могут обращаться к администрации общежития по широкому кругу вопросов, связанных с проживанием, бытовыми условиями и соблюдением правил.</p>
        <br>
        <p class="highlight-blue"><b>1.</b> Организационные вопросы.</p>
        <p class="highlight-blue"><b>2.</b> Бытовые проблемы.</p>
        <p class="highlight-blue"><b>3.</b> Коммунальные услуги и оплата.</p>
        <p class="highlight-blue"><b>4.</b> Безопасность.</p>
        <p class="highlight-blue"><b>5.</b> Инфраструктура и благоустройство.</p>
    </div>
            """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("администрация_к19/заведующий_к19.jpg", width=250)
with col2:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3> Заведующий студенческим общежитием</h3> 
                    </div>
                </div>
            <br>
            <p><b>Васильев Александр Владимирович<b></p>  
            <br>  
            <p>📞 <a href="tel:+78125210032">(812) 521-00-32</a>, <a href="tel:+78124589730,1120">(812) 458-97-30, доб. 1120</a></p>
            <p>📩 <a href="mailto:KOS19@UNECON.RU">KOS19@UNECON.RU</a></p>
        </div>
                """, unsafe_allow_html=True)

col3, col4 = st.columns([1, 3])
with col3:
    st.image("администрация_к19/комендант_к19.jpg", width=250)
with col4:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заместитель заведующего студенческим общежитием</h3> 
                    </div>
                </div>
            <br>
            <p><b>Левашова Людмила Григорьевна<b></p>
            <br>
            <p>📞 <a href="tel:+78125210033">(812) 521-00-33</a></p>
            <p>📩 <a href="mailto:KOS19@UNECON.RU">KOS19@UNECON.RU</a></p>
        </div>
                """, unsafe_allow_html=True)

col5, col6 = st.columns([1, 3])
with col5:
    st.image("администрация_к19/завхоз_к19.jpg", width=250)
with col6:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заведующий хозяйственной частью</h3> 
                    </div>
                </div>
            <br>
            <p><b>Хижняк Наталья Сергеевна<b></p>
            <br> 
            <p>📞 <a href="tel:+78124589730,1132">(812) 458-97-30, доб. 1132</a></p>
            <p>📩 <a href="mailto:khizhnyak.ns@unecon.ru">maksimova.o@unecon.ru</a></p>
        </div>
                """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>🚪 Вся администрация общежития расположена на первом этаже общежития.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")

st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.markdown("""
    <style>
        .custom-links a {
            color: white !important;
            text-decoration: none; 
        }
        .custom-links a:hover {
            color: #ccc !important;  
            text-decoration: underline; 
        }
    </style>
    <div class="custom-links">
        <p>📞 <a href="tel:+78125210032">(812) 521-00-32</a></p>
    </div>
""", unsafe_allow_html=True)

st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.markdown("""
    <div class="custom-links">
        <p>📞 <a href="tel:+78125210033">(812) 521-00-33</a></p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="custom-links">
        🆘 <a href="https://t.me/helperKosygina19k2_bot">Чат со студенческим советом</a>
    </div>
""", unsafe_allow_html=True)
