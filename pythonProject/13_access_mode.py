import streamlit as st

st.title("🪪 Порядок допуска студентов")
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
        <p>Совершеннолетние студенты: 🕐 вход/выход 24/7</p>
        <p>Несовершеннолетние студенты: 🕐 выход до 23:00</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.title("🪪 Порядок допуска посетителей")
st.divider()

st.markdown("""
    <div class="colored-container">
        <p>Открыт допуск посетителей в общежитие, в число которых входят 
        родственники проживающих и студенты СПбГЭУ.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Согласно ПОЛОЖЕНИЯ о пропускном и внутриобъектовом режимах,
        устанавливаются следующие правила посещения:</p>
        <p><b>1.</b> Посетителям общежития проход разрешен с 10:00 до 20:00.</p>
        <p><b>2.</b> Вход и выход посетителей возможен только в сопровождении
        проживающего лица, к которому они прибыли.</p>
        <p><b>3.</b> Родственники проходят только по письменному заявлению
        заместителя заведующего. При себе иметь документы удостоверяющие
        проживающего или с личного разрешения заведующего или
        личность и степень родства.</p>
        <p><b>4.</b> Посетителям-студентам при себе иметь студенческий билет или
        пропуск с фотографией.</p>
        <p><b>5.</b> При проходе гостя, сотрудник охраны производит запись в журнале
        посетителей и изымает пропуск у проживающего студента, на всё
        время посещения.</p>
        <p><b>6.</b> Проживающий студент должен самостоятельно разъяснить гостям
        правила внутреннего распорядка в общежитии и несёт персональную
        ответственность за их неукоснительное соблюдение посетителями.</p>
        <p><b>7.</b> В случае нарушения гостями и проживающим лицом любого из
        пунктов правил посещения, допуск всех гостей прекращается до даты
        допущенного нарушения.
        окончания разбирательства администрацией и студсоветом общежития.</p>
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
