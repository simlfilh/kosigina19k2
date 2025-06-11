import streamlit as st

st.title("👫 Студенческий совет общежития СПБГЭУ №3")
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
            padding: 10px;
            margin-bottom: 20px;
            position: relative;
        }
        .highlight-blue-2 {
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
        <p><b>Студенческий совет общежития</b> — это выборный орган самоуправления, созданный студентами для 
        защиты их интересов, организации досуга и взаимодействия с администрацией.</p> 
        <p>Это "мост" между проживающими и руководством общежития и ВУЗа.</p> 
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Студенты могут обращаться к студенческому совету по широкому кругу вопросов, связанных с проживанием, 
        бытовыми условиями и соблюдением правил.</p>
        <br>
        <p class="highlight-blue"><b>1.</b> Защита прав студентов.</p>
        <p>— Контроль за соблюдением условий проживания (ремонт, уборка, коммунальные услуги).</p>
        <p>— Разрешение конфликтов (с соседями, администрацией).</p>
        <br>
        <p class="highlight-blue"><b>2.</b> Организация жизни в общежитии.</p>
        <p>— Проведение мероприятий.</p>
        <p>— Создание комфортной среды.</p>
        <br>
        <p class="highlight-blue"><b>3.</b> Взаимодействие с администрацией.</p>
        <p>— Передача коллективных жалоб или предложений.</p>
        <p>— Участие в комиссиях по заселению/выселению.</p>
        <br>
        <p class="highlight-blue"><b>4.</b> Информационная поддержка.</p>
        <p>— Разъяснение правил проживания первокурсникам.</p>
        <p>— Оперативное оповещение.</p>
        <br>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.header("Председатель студенческого совета")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\председатель.jpg", width=250)
with col2:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Староста общежития</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/necrogenes1s" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Томаев Азамат Александрович</b></p>
                </div>
            <br>
            <p>🚪 Блок: 130/2</p>  
            <p>📞 +79388830726</p>  
            <p>📩 azam1306@mail.ru</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.header("Заместители председателя")
col3, col4 = st.columns([1, 3])
with col3:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 2.jpg", width=250)
with col4:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заместитель председателя</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/simlfilh" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Савченко Валерия Андреевна</b></p>
                </div>
            <br>
            <p>🚪 Блок: 161/1</p>
            <p>📞 +79600046973</p>  
            <p>📩 valerasavchenkoprivet@gmail.com</p>
        </div>
                """, unsafe_allow_html=True)

col5, col6 = st.columns([1, 3])
with col5:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 6.jpg", width=250)
with col6:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заместитель председателя</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/shushaanik" target="_blank" style="margin-left: 5px; font-size: 25px;">                        <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Комышев Никита Михайлович</b></p>
                </div>
            <br>
            <p>🚪 Блок: 183/2</p>  
            <p>📞 +79283102210</p>  
            <p>📩 vip.nike2006@mail.ru</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.header("Старосты")

# 2 ЭТАЖ
col7, col8 = st.columns([1, 3])
with col7:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 2.jpg", width=250)
with col8:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 2 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/simlfilh" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Савченко Валерия Андреевна</b></p>
                </div>
            <br>
            <p>🚪 Блок: 161/1</p>
            <p>📞 +79600046973</p>  
            <p>📩 valerasavchenkoprivet@gmail.com</p>
        </div>
                """, unsafe_allow_html=True)

# 3 ЭТАЖ
col9, col10 = st.columns([1, 3])
with col9:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 3.jpg", width=250)
with col10:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 3 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/id456304845" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Педин Максим Олегович</b></p>
                </div>
            <br>
            <p>🚪 Блок: 35/1</p>  
            <p>📞 +79181572998</p>  
            <p>📩 pedinmax@gmail.com</p>
        </div>
                """, unsafe_allow_html=True)

# 4 ЭТАЖ
col11, col12 = st.columns([1, 3])
with col11:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 4.jpg", width=250)
with col12:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 4 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/9cuteex" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Радченко Диас</b></p>
                </div>
            <br>
            <p>🚪 Блок: 57/1</p>  
            <p>📞 +79531529087</p>  
            <p>📩 danzel.loren@mail.ru</p>
        </div>
                """, unsafe_allow_html=True)

# 5 ЭТАЖ
col13, col14 = st.columns([1, 3])
with col13:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 5.jpg", width=250)
with col14:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 5 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/ddtka" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Ткаченко Дарья Дмитриевна</b></p>
                </div>
            <br>
            <p>🚪 Блок: 58/2</p>  
            <p>📞 +79628651615</p>  
            <p>📩 d.d.t13@mail.ru</p>
        </div>
                """, unsafe_allow_html=True)

# 6 ЭТАЖ
col15, col16 = st.columns([1, 3])
with col15:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 6.jpg", width=250)
with col16:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 6 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/shushaanik" target="_blank" style="margin-left: 5px; font-size: 25px;">                        <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Комышев Никита Михайлович</b></p>
                </div>
            <br>
            <p>🚪 Блок: 183/2</p>  
            <p>📞 +79283102210</p>  
            <p>📩 vip.nike2006@mail.ru</p>
        </div>
                """, unsafe_allow_html=True)

# 7 ЭТАЖ
col17, col18 = st.columns([1, 3])
with col17:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 7.jpg", width=250)
with col18:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 7 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/grellsatckliww" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Гончарова Софья Аркадьевна</b></p>
                </div>
            <br>
            <p>🚪 Блок: 99/1</p>  
            <p>📞 +79054244094</p>  
            <p>📩 sofagon278@gmail.com</p>
        </div>
                """, unsafe_allow_html=True)

# 8 ЭТАЖ
col19, col20 = st.columns([1, 3])
with col19:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 8.jpg", width=250)
with col20:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 8 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/alexa__nikiforova" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Дробко Александра Максимовна</b></p>
                </div>
            <br>
            <p>🚪 Блок: 108/1</p>  
            <p>📞 +79140875194</p>  
            <p>📩 aleksandra.drobko@mail.ru</p>
        </div>
                """, unsafe_allow_html=True)

# 9 ЭТАЖ
col21, col22 = st.columns([1, 3])
with col21:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 9.jpg", width=250)
with col22:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 9 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/vasushkakeef" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Таршиков Василий Александрович</b></p>
                </div>
            <br>
            <p>🚪 Блок: 130/1</p>  
            <p>📞 +79292424866</p>  
            <p>📩 sowatasheryt@gmail.com</p>
        </div>
                """, unsafe_allow_html=True)

# 10 ЭТАЖ
col23, col24 = st.columns([1, 3])
with col23:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 10.jpg", width=250)
with col24:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 10 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/alv_av" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Волкова Александра Сергеевна</b></p>
                </div>
            <br>
            <p>🚪 Блок: 138/2</p>  
            <p>📞 +79201204040</p>  
            <p>📩 Alvolkova@internet.ru</p>
        </div>
                """, unsafe_allow_html=True)

# 11 ЭТАЖ
col25, col26 = st.columns([1, 3])
with col25:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\староста 11.jpg", width=250)
with col26:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 11 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/bagaurid" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Багаури Диана Бакуриевна</b></p>
                </div>
            <br>
            <p>🚪 Блок: 162/1</p>  
            <p>📞 +79995325717</p>  
            <p>📩 bagauri_diana@mail.ru</p>
        </div>
                """, unsafe_allow_html=True)

# 12 ЭТАЖ
col27, col28 = st.columns([1, 3])
with col27:
    st.image("C:\\Users\\simlfilh\\OneDrive\\Desktop\\СПбГЭУ\\2 курс\\4 семестр\\Практика\\администрация"
             "\\нн.jpg", width=250)
with col28:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 12 этажа</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/bagaurid" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>N N N</b></p>
                </div>
            <br>
            <p>🚪 Блок: 00/0</p>  
            <p>📞 +79000000000</p>  
            <p>📩 mail.ru</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.write("Тел.: (812) 521-00-32")
st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.write("Тел.: (812) 521-00-33")

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
