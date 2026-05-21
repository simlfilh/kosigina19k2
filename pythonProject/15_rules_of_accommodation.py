import streamlit as st

st.title("👫 Правила проживания")
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
        <div class="highlight-blue">
            <h3>🕐 Режим тишины: 23:00 - 07:00</h3>
        </div>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-red">
                <div class="text-indent-content">
                    <h3>ЗАПРЕЩЕНО:</h3> 
                </div>
            </div>
        <p><b>1.</b> Самостоятельно переселяться, переносить инвентарь общежития из блока и комнаты в любые 
        другие блоки и комнаты.</p>
        <p><b>2.</b> Самостоятельно заменять электропроводку, менять дверные замки, делать ремонт 
        без согласования с администрацией общежития.</p>
        <p><b>3.</b> Курить кальян, электронные и обычные сигареты и т.п. внутри общежития.</p>
        <p><b>4.</b> Проводить родственников и гостей в общежитие и (или) оставлять их ночевать в общежитии,
        нарушая установленный порядок и правила проживания в общежитии.</p>
        <p><b>5.</b> Предоставлять жилую площадь для проживания посторонним лицам (не проживающим в жилом помещении).</p>
        <p><b>6.</b> Находиться в общежитии в состоянии алкогольного/наркотического опьянения.</p>
        <p><b>7.</b> Вносить, потреблять, хранить алкогольные напитки и психоактивные вещества, а также осуществлять их продажу.</p>
        <p><b>8.</b> Наклеивать на стены и иные поверхности (кроме специально отведенных для этой цели мест) 
        объявления, расписания и т.п.</p>
        <p><b>9.</b> Хранить и (или) использовать оружие (в том числе холодное, пневматическое и травматическое).</p>
        <p><b>10.</b> Использовать открытый огонь.</p>
        <p><b>11.</b> Заводить животных.</p>
        <p><b>12.</b> Иметь внутри блока микроволновку, стиральную машину, электроплиту,
        обогреватель, мультиварку.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-red">
                <div class="text-indent-content">
                    <h3>Проверка</h3> 
                </div>
            </div>
        <p>Раз в 3-6 месяцев в общежитии проводится проверка блоков на чистоту, наличие запрещенных предметов, 
        пожарная инспекция, проверки от ВУЗа.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-red">
                <div class="text-indent-content">
                    <h3>Пожарная безопасность</h3> 
                </div>
            </div>
        <p>Датчики пожарной безопасности расположены в зонах общего пользования и внутри блоков.</p>
        <p>В случае, если датчик пожарной безопасности сработает, приедут пожарные. Вам будет необходимо 
        написать объяснительную на имя заведующего и подойти к нему в ближайший рабочий день.</p>
        <p>Датчики пожарной безопасности запрещено чем-либо перекрывать.</p>
        <p>Сушилки для одежды не должны стоять в коридорах общего пользования, по той причине, что это 
        является препятствием для выхода из блока в случае пожара.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>❗️За нарушение любого из вышеперечисленных пунктов, за нарушение любых прав 
        и обязанностей нанимателя, перечисленных в договоре найма жилого помещения в общежитии СПбГЭУ студент 
        получает выговор.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <style>
        div[data-testid="stExpander"] {
            background: #FFFFFF !important;
            border: 2px solid #E0E0E0 !important;
            border-radius: 8px !important;
            margin: 12px 0 !important;
            padding: 0 !important;
        }
        div[data-testid="stExpander"] > div[role="button"] {
            background: #FFFFFF !important;
            padding: 12px !important;
        }
        div[data-testid="stExpander"] > div[role="button"] p {
            color: #000000 !important;
            font-size: 18px !important;
            font-weight: 700 !important;
            margin: 0 !important;
        }
        div[data-testid="stExpander"] svg {
            color: #000000 !important;
        }
        div[data-testid="stExpander"] div[data-testid="stVerticalBlock"] {
            color: #000000 !important;
            padding: 12px !important;
            font-size: 16px !important;
        }
        div[data-testid="stExpander"] * {
            color: #000000 !important;
        }
    </style>
            """, unsafe_allow_html=True)

with st.expander("**ПРИЛОЖЕНИЕ к Положению об общежитиях ФГБОУ ВО СПбГЭУ**"):
    st.image("пвр/1.jpg")
    st.image("пвр/2.jpg")
    st.image("пвр/3.jpg")
    st.image("пвр/4.jpg")
    st.image("пвр/5.jpg")
    st.image("пвр/6.jpg")
    st.image("пвр/7.jpg")
    st.image("пвр/8.jpg")
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
