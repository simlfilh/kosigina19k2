import streamlit as st

st.title("👫 Правила проживания")
st.divider()

st.markdown("""
    <style>
        .colored-container {
           background-color: #FFFFFF;  /* Белый цвет фона */
           border-radius: 10px;      /* Закругление углов на 10px */
           padding: 20px;            /* Внутренние отступы 20px */
           margin-bottom: 20px;      /* Внешний отступ снизу 20px */
           color: black !important;  /* Черный цвет текста */
           line-height: 1.0;
           font-size: 21px;
        }
        .highlight-green {
            background-color: #C8E6C9;  /* Светло-зеленый фон */
            border-radius: 10px;
            padding-left: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .highlight-red {
            background-color: #FFCDD2;  /* Светло-зеленый фон */
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
        <h3 class="highlight-blue">🕐 Режим тишины: 23:00 - 07:00</h3>
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
        <p><b>3.</b> Курить кальян, электронные и обычные сигареты и т.п. внутри общежития. 
        Для этого есть специально отведенное место при входе в общежитие.</p>
        <p><b>4.</b> Предоставлять жилую площадь для проживания не проживающим в блоке.</p>
        <p><b>5.</b> Находиться в общежитии в состоянии алкогольного/наркотического опьянения; Вносить, 
        потреблять и хранить психоактивные вещества и осуществлять их продажу.</p>
        <p><b>6.</b> Использовать открытый огонь.</p>
        <p><b>7.</b> Заводить животных.</p>
        <p><b>8.</b> Иметь внутри блока микроволновку, стиральную машину, электроплиту,
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
        <p>Раз в 3-6 месяцев в общежитии проводится проверка блоков на чистоту, наличие запрещенки, 
        пожарная инспекция, проверки от ВУЗа. Проверка может быть от факультета.</p>
        <p>Студенческий совет предупреждает в беседах этажей о всех известных грядущих проверках.</p>
        <p>Чтобы избежать неприятных ситуаций, добавьтесь в чаты общежития и этажа.</p>
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
        получает выговор. После получения трёх выговоров, включая выговора за пропуски пар в университете, 
        студента отчисляют из учебного заведения.</p>
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
    st.image("пвр/9.jpg")
    st.image("пвр/10.jpg")
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.write("Тел.: (812) 521-00-32")
st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.write("Тел.: (812) 521-00-33")

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
