import streamlit as st

st.title("Выселение из общежития")
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
            padding: 20px;
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
                    <h3>Для выселения из общежития необходимо:</h3> 
                </div>
            </div> 
        <p><b>1.</b> Написать заявление на выезд у заведующего студенческим общежитием.</p>
        <p><b>2.</b> Погасить задолженность за проживание в общежитии.</p>
        <p><b>3.</b> Получить обходной лист.</p>
        <p><b>4.</b> Заполнить обходной лист (заведующий студенческим общежитием, 
        Жилищно-бытовое управление (кабинет №1 и №5), Бюро пропусков, бельевая, камера хранения).</p>
        <p><b>5.</b> Заполненный обходной лист отдать заведующему студенческим общежитием вместе с ключами от комнаты.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p class="highlight-red"><b>❗️ Выезд из общежития БЕЗ ОБХОДНОГО ЛИСТА не осуществляется. Оплата за 
        проживание в общежитии будет также накапливаться.</b></p>
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

# st.markdown("""
#     <div class="custom-links">
#         🆘 <a href="https://t.me/helperKosygina19k2_bot">Чат со студенческим советом</a>
#     </div>
# """, unsafe_allow_html=True)
