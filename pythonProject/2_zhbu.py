import streamlit as st

st.title("🏢 Жилищно-бытовое управление")
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
        <p><b>Жилищно-бытовое управление (ЖБУ)</b> — это структурное подразделение, отвечающее за 
        содержание и обслуживание студенческого жилья (общежитий).</p>
        <p>Его ключевая задача — создание безопасных и комфортных условий для проживания и обучения студентов.</p>
        <br>
        <p>В жилищно-бытовое управление студент может обратиться по следующим вопросам:</p>
        <p>• Временная регистрация в общежитии;</p>
        <p>• Оформление дополнительного койко-места в общежитии.</p>
    </div>
            """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>Контакты</h3> 
                    </div>
                </div>
            <br>
            <p>📍 Адрес: наб. канала Грибоедова, д. 30-32, лестница № 4</p>  
            <p>📞 Справки по телефону: (812) 458-97-30, доб. 4291, 4294</p>  
            <p>📩 dom@unecon.ru</p>
            <br>
        </div>
                """, unsafe_allow_html=True)
with col2:
    st.components.v1.html("""
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1998.123456789!2d30.3239012!3d59.9314116!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x203c18dc7f0eaf89!2z0JbQuNCy0LjQvdC-LdCy0LXRgNC90LDRjyDQv9GA0L7QsdGA0LDQttC10L3QuNGP!5e0!3m2!1sru!2sru!4v1234567890!5m2!1sru!2sru" 
            width="100%" 
            height="290" 
            style="border:0; border-radius: 10px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
                    """, height=300)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>🕐 Общие часы приёма</h3> 
                </div>
            </div>
        <br>
        <p>ПН: 14:00 — 16:30</p>  
        <p>ВТ: 14:00 — 16:30</p>  
        <p>СР: приема нет</p>
        <p>ЧТ: 14:00 — 16:30</p>
        <p>ПТ: 13:00 — 15:00</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.header("Начальник ЖБУ")
col3, col4 = st.columns([1, 2])
with col3:
    st.image("начальник ЖБУ.jpg")
with col4:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Руководитель волонтерского центра СПбГЭУ</h3> 
                    </div>
                </div>
            <br>
            <p><b>Рябов Сергей Павлович</b></p>  
            <p>📩 dom@unecon.ru</p> 
            <br>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.header("Заместители начальника ЖБУ")
col5, col6 = st.columns([1, 2])
with col5:
    st.image("../администрация/зам. начальника ЖБУ.jpg")
with col6:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заместитель</h3> 
                    </div>
                </div>
            <br>
            <p><b>Мирошниченко Андрей Антонович</b></p>  
            <p>📩 aam@unecon.ru</p> 
            <br>
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>🕐 Часы приёма</h3> 
                    </div>
                </div>
            <br>
            <p>ПН: 14:00 — 16:00</p>  
            <p>ВТ: приема нет</p>  
            <p>СР: приема нет</p>
            <p>ЧТ: 14:00 — 16:00</p>
            <p>ПТ: приема нет</p>
        </div>
                """, unsafe_allow_html=True)

col7, col8 = st.columns([1, 2])
with col7:
    st.image("../администрация/ннн.jpg")
with col8:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заместитель</h3> 
                    </div>
                </div>
            <br>
            <p><b>Забродина Галина Александровна 👩🏼‍💼</b></p>  
            <br>
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>🕐 Часы приёма</h3> 
                    </div>
                </div>
            <br>
            <p>ПН: приема нет</p>  
            <p>ВТ: 14:00 — 16:00</p>  
            <p>СР: приема нет</p>
            <p>ЧТ: 14:00 — 16:00</p>
            <p>ПТ: приема нет</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.header("Специалисты")
st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Паспортист</h3> 
                </div>
            </div>
        <br>
        <p><b>Белова Надежда Викторовна 👩🏼‍💼</b></p>  
        <p>🚪 Кабинет №1</p>  
        <br> 
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>🕐 Часы приёма</h3> 
                </div>
            </div>
        <br>
        <p>ПН: 13:00 — 16:30</p>  
        <p>ВТ: 13:00 — 16:30</p>  
        <p>СР: приема нет</p>
        <p>ЧТ: 14:00 — 17:00</p>
        <p>ПТ: 14:00 — 16:45</p>
        <br>
        <p>🍜 ОБЕД: 12:00 — 13:00</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Ведущий документовед</h3> 
                </div>
            </div>
        <br>
        <p><b>Чигиринова Дарина Владимировна 👩🏼‍💼</b></p>  
        <p>🚪 Кабинет №5</p>  
        <br>
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>🕐 Часы приёма</h3> 
                </div>
            </div>
        <br>
        <p>ПН: 14:00 — 16:30</p>  
        <p>ВТ: 14:00 — 16:30</p>  
        <p>СР: приема нет</p>
        <p>ЧТ: 14:00 — 16:30</p>
        <p>ПТ: 13:00 — 15:00</p>
        <br>
        <p>🍜 ОБЕД: 12:00 — 13:00</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Специалист по работе с молодежью</h3> 
                </div>
            </div>
        <br>
        <p><b>Васильева Валерия Михайловна 👩🏼‍💼</b></p>  
        <p>🚪 Кабинет №5</p>  
        <br>
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>🕐 Часы приёма</h3> 
                </div>
            </div>
        <br>
        <p>ПН: 14:00 — 16:30</p>  
        <p>ВТ: 14:00 — 16:30</p>  
        <p>СР: приема нет</p>
        <p>ЧТ: 14:00 — 16:30</p>
        <p>ПТ: 13:00 — 15:00</p>
        <br>
        <p>🍜 ОБЕД: 12:00 — 13:00</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.write("Тел.: (812) 521-00-32")
st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.write("Тел.: (812) 521-00-33")

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
