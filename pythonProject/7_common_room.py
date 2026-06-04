import streamlit as st

def create_button(url, text):
    return f"""
    <div class="custom-button">
        <a href="{url}" style="text-decoration: none;">
            <button style="
                width: 100%;
                color: white;
                background-color: #DC3545;
                border: none;
                padding: 10px 0;
                border-radius: 5px;
                font-weight: bold;
                cursor: pointer;
            ">{text}</button>
        </a>
    </div>
    """

st.title("🧺 Бытовое пространство")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.image("рекреации/прачечная.jpg")
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
                        <h3>🧺 Прачечная | 1 ЭТАЖ</h3> 
                    </div>
                </div>
            <p>Оснащение: 11 стиральных машин, 1 сушильная машина.</p>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://t.me/Landromaticbot" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i></a>
                    <p style="margin: 0; font-size: 21px;">Оплата: в банкомате на 1-ом этаже или через 
                    телеграм-бот "Ландроматик"</p>
                </div>
        </div>
                """, unsafe_allow_html=True)
st.divider()

col4, col5 = st.columns([2, 1])
with col4:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>🛌 Бельевая | 1 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>Работник бельевой: Раевская Елена Валентиновна</p>  
            <br> 
            <p>В бельевой можно получить/поменять:</p>  
            <p>• подушку</p>
            <p>• одеяло</p>
            <p>• покрывало</p>
            <p>• шторы</p>
            <p>• наматрасник</p>
            <p>• полный комплект постельного белья</p>
            <br>
            <p>Постельное белье меняется 1 раз в неделю бесплатно: отдали грязное - тут же получили чистое.</p>
        </div>
                """, unsafe_allow_html=True)
with col5:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>🕐 Режим работы:</h3> 
                    </div>
                </div>
            <p>ПН: 14:00 — 19:00</p>  
            <p>ВТ: 14:00 — 18:00</p>  
            <p>СР: приема нет</p>
            <p>ЧТ: 10:45 — 15:45</p>
            <p>ПТ: 14:00 — 17:00</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🔐 Камера хранения | 1 ЭТАЖ</h3> 
                </div>
            </div>
    </div>
            """, unsafe_allow_html=True)
st.divider()

col6, col7 = st.columns(2)
with col6:
    st.image("рекреации/сушильная.jpg")
with col7:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>2 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>💨 Сушильная комната</p>
            <p>🕐 24/7</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🔧 Сантехник</h3> 
                </div>
            </div>
        <p>Работник: Цуцу Константин Георгиевич</p>
        <p>📖 Заявки подаются в журнал в холле 1-го этажа</p>
        <p>📞 При срочных авариях <a href="tel:+79117136982">+79117136982</a></p>
    </div>
            """, unsafe_allow_html=True)
st.markdown(create_button("https://requestsunecondorms.streamlit.app/", "Оставить электронную заявку"), unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>💡 Электрик</h3> 
                </div>
            </div>
        <p>Работник: Потемкин Сергей Михайлович</p>
        <p>📖 Заявки подаются в журнал в холле 1-го этажа</p>
        <p>🕐 ПН-ПТ: 17:00 — 19:30</p>
    </div>
            """, unsafe_allow_html=True)
st.markdown(create_button("https://requestsunecondorms.streamlit.app/", "Оставить электронную заявку"), unsafe_allow_html=True)
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

