import streamlit as st

st.title("🚻 Студенческое пространство")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.image("рекреации/спортзал.jpg")
with col2:
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
                        <h3>5 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>💪 Спортзал</p> 
            <p>🕐 9:00 — 22:00</p>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/dk_rus_123" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;">Ответственный за спортзал Роман</p>
                </div>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.image("рекреации/зал аэробики.jpg")
with col4:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>5 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>👯 Зал аэробики</p> 
            <p>🕐 9:00 — 22:00</p>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/doraz04" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;">Ответственная за зал аэробики Дарина</p>
                </div>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
    st.image("рекреации/еда.jpg")
with col6:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>6 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>🍱 Вендинг-аппараты</p>
            <p>🕐 24/7</p>
        </div>
                """, unsafe_allow_html=True)

col7, col8 = st.columns(2)
with col7:
    st.image("рекреации/вода.png")
with col8:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>6 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>💧 Аппарат с водой</p>
            <p>🕐 24/7</p>
        </div>
                """, unsafe_allow_html=True)

col9, col10 = st.columns(2)
with col9:
    st.image("рекреации/игровая комната.jpg")
with col10:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>7 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>🧩 Игровая комната</p>
            <p>🕐 9:00 — 23:00</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col11, col12 = st.columns(2)
with col11:
    st.image("рекреации/теннис.jpg")
with col12:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>8 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>🏓 Теннисный стол</p>
            <p>🕐 9:00 — 23:00</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col13, col14 = st.columns(2)
with col13:
    st.image("рекреации/учебная комната.jpg")
with col14:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>10 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>📚 Учебная комната</p>
            <p>🕐 24/7</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col15, col16 = st.columns(2)
with col15:
    st.image("рекреации/кинозал.png")
with col16:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>10 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>🌌 Кинозал</p>
            <p>🕐 9:00 — 23:00</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col17, col18 = st.columns(2)
with col17:
    st.image("рекреации/комната отдыха.jpg")
with col18:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>11 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>🛋 Комната отдыха</p>
            <p>🕐 9:00 — 23:00</p>
            <p>🔑 Ключ на охране</p> 
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

