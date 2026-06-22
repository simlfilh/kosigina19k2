import streamlit as st

st.title("🏫 Бюро пропусков")
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
        <p><b>Бюро пропусков</b> — это подразделение, отвечающее за оформление, выдачу и контроль пропускной 
        системы университета. Оно регулирует доступ на территорию кампуса и в здания СПбГЭУ для студентов, 
        сотрудников и посетителей.</p>
        <br>
        <p><b>Основные функции Бюро пропусков:</b></p>
        <p class="highlight-blue"><b>1.</b> Оформление пропусков</p>
        <p>• Для студентов, преподавателей, сотрудников и подрядчиков.</p>
        <p class="highlight-blue"><b>2.</b> Восстановление пропусков</p>
        <p>• При утере или повреждении.</p>
        <p>• Замена при изменении статуса (например, переход с временного на постоянный пропуск).</p>
        <p class="highlight-blue"><b>3.</b> Информационная поддержка</p>
        <p>• Консультации по вопросам пропускного режима.</p>
        <p>• Работа с обращениями по проблемам доступа.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>🕐 График работы:</h3> 
                    </div>
                </div>
            <p>ПН-ПТ: 09:00 — 18:00</p>  
            <p>СБ-ВС: выходные дни</p>
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>🚶‍♀️Приём посетителей:</h3> 
                    </div>
                </div>
            <p>09:05 — 11:55</p>
            <p>13:00 — 16:55</p>
            <br>
            <p>🍜 Обеденный перерыв: с 12:00 — 13:00</p>
        </div>
                """, unsafe_allow_html=True)
with col2:
    st.components.v1.html("""
        <iframe 
            src="https://yandex.ru/map-widget/v1/?um=constructor%3Ac1e2590fd5b6de05293321a22e9c4acfacdbff29dfc50eef266e905a4b03ac5e&amp;source=constructor" 
            width="100%" 
            height="430" 
            frameborder="1" 
            allowfullscreen="true" 
            style="position:relative;border-radius: 10px;border: none;">
        </iframe>, 
                    """, height=450)
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
