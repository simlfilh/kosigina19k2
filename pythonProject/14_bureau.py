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
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1999.0260521530026!2d30.321633177064342!3d59.93170987491158!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469631068482e895%3A0x15dbd342b4e6a45d!2z0JHRjtGA0L4g0L_RgNC-0L_Rg9GB0LrQvtCy!5e0!3m2!1sru!2sru!4v1749661667659!5m2!1sru!2sru" 
            width="100%" 
            height="440" 
            style="border:0; border-radius: 10px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
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
