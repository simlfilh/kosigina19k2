import streamlit as st

st.title("🏨 Гостевые блоки")
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
        <p>В общежитии №3 на 1 этаже расположены гостевые блоки.</p>
        <p>Гостевые блоки предназначены для временного расположения студентов заочной формы обучения на период 
        сессии и близких родственников (папа, мама, сестры, братья) обучающихся очной формы обучения, 
        проживающих в общежитии.</p>
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
        <p>🛋️ Вся необходимая мебель: стол, стул, кровать с матрасом, шкаф и тумбочка.</p>
        <p>🛌 Общежитие выдает: постельное белье, подушку, одеяло, полотенце.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Для заселения родственника в гостевой блок студент пишет соответствующее заявление 
        у заведующего студенческим общежитием (в его отсутствие - у заместителя заведующего 
        студенческим общежитием или коменданта), оплачивает срок проживания, получает пропуск.</p>
        <p>Обязательным условием для оформления гостевого тарифа является отсутствие у студента 
        задолженности по оплате проживания в общежитии.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Стоимость</h3> 
                </div>
            </div> 
        <p>• 400 руб/сутки - для студентов заочной формы обучения;</p>
        <p>• 650 руб/сутки - для родственников студентов, проживающих в общежитии. </p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>🚫 Студент с родителями в одном блоке жить не может.</p>
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
