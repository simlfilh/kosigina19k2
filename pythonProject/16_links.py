import streamlit as st

st.title("📲 Наши социальные сети")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <style>
            .colored-container {
               background-color: #FFFFFF; 
               border-radius: 10px;     
               padding: 10px;          
               margin-bottom: 20px;     
               color: black !important;
               line-height: 1.0;
               font-size: 21px;
            }
            .highlight-green {
                background-color: #C8E6C9; 
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .highlight-red {
                background-color: #FFCDD2; 
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .text-indent-content {
                position: relative;
                left: 20px;
                color: black;
                line-height: 1.4;
            }
        </style>
        <div class="colored-container">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <a href="https://vk.com/kosygina19k2?from=groups" target="_blank">
                    <i class="fab fa-vk fa-2x"></i></a>
                    <h3>СПбГЭУ Общежитие №3 | Косыгина 19к2.</h3>
                </div>
            <p>• Чтобы вашу заявку приняли, отправьте скрин из личного кабинета из раздела "Информация" 
            в сообщения сообщества (см. фото справа).</p>
            <p>• Доступ к ИНФО-Каналу общежития в TG см. в разделе "Ссылки" в ВК-сообществе.</p>
        </div>
                """, unsafe_allow_html=True)
    
with col2:
    st.image("инструкция вк.png",
             width=250)
    st.markdown("""
    <p>Скриншот из раздела "Информация" ⬆️<p>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("""
        <div class="colored-container">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <a href="https://t.me/Kosygina19k2_bot" target="_blank">
                    <i class="fab fa-telegram fa-2x"></i></a>
                    <h3>БОТ Общежития №3.</h3>
                </div>
        </div>
                """, unsafe_allow_html=True)

st.markdown("""
        <div class="colored-container">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <a href="https://t.me/helperKosygina19k2_bot" target="_blank">
                    <i class="fab fa-telegram fa-2x"></i></a>
                    <h3>ПОДДЕРЖКА Общежития №3.</h3>
                </div>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("""
        <div class="colored-container">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <a href="https://max.ru/id7840483155_gos17" target="_blank">
                        <i class="fas fa-comment-dots fa-2x" style="color: #00BFFF;"></i>
                    </a>
                    <h3>Канал «Общежития СПбГЭУ» в MAX.</h3>
                </div>
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
