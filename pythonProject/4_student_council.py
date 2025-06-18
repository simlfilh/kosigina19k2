import streamlit as st

st.title("👫 Студенческий совет общежития СПбГЭУ №3")
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
        <p><b>Студенческий совет общежития</b> является органом студенческого самоуправления в общежитии СПбГЭУ, 
        образованным по инициативе обучающихся в целях учета мнения обучающихся по вопросам реализации молодежной 
        политики и воспитательной деятельности в сфере социальной поддержки и социальной защиты обучающихся, 
        проживающих в общежитиях, и утвержденный решением администрации Университета.</p> 
        <p>Целями деятельности органов студенческого самоуправления в общежитиях СПбГЭУ являются формирование у 
        обучающихся активной гражданской позиции, сознательного и ответственного отношения к возможностям своей 
        социальной самоорганизации и культурно-нравственного саморазвития, развитие умений и навыков самоуправления 
        и подготовка обучающихся к компетентному и ответственному участию в жизни общества.</p> 
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <p><b>Задачами деятельности органов студенческого самоуправления в общежитиях СПбГЭУ являются:</b></p>
                </div>
            </div>
        <p>—  учет мнения обучающихся, проживающих в общежитии;</p>
        <p>—  организация взаимодействия администрации СПбГЭУ и студенческих общежитий в части улучшения 
        жилищных условий проживания обучающихся совместно с ПО;</p>
        <p>—  содействие обучающимся в решении социальных вопросов, связанных с проживанием в общежитии 
        совместно с ПО;</p>
        <p>—  организация просветительских, культурно-досуговых, спортивно-оздоровительных и адаптационных 
        мероприятий для обучающихся, проживающих в общежитии;</p>
        <p>—  противодействие деструктивной идеологии в студенческой среде.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.header("Председатель студенческого совета")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("администрация/председатель.jpg", width=250)
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
            <p>📞 <a href="tel:+79388830726">+79388830726</a></p>
            <p>📩 <a href="mailto:azam1306@mail.ru">azam1306@mail.ru</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.header("Заместители председателя")
col3, col4 = st.columns([1, 3])
with col3:
    st.image("администрация/староста 2.jpg", width=250)
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
            <p>📞 <a href="tel:+79600046973">+79600046973</a></p>
            <p>📩 <a href="mailto:valerasavchenkoprivet@gmail.com">valerasavchenkoprivet@gmail.com</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

col5, col6 = st.columns([1, 3])
with col5:
    st.image("администрация/староста 6.jpg", width=250)
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
            <p>📞 <a href="tel:+79283102210">+79283102210</a></p>
            <p>📩 <a href="mailto:vip.nike2006@mail.ru">vip.nike2006@mail.ru</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.header("Старосты")

# 2 ЭТАЖ
col7, col8 = st.columns([1, 3])
with col7:
    st.image("администрация/староста 2.jpg", width=250)
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
            <p>📞 <a href="tel:+79600046973">+79600046973</a></p>
            <p>📩 <a href="mailto:valerasavchenkoprivet@gmail.com">valerasavchenkoprivet@gmail.com</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 3 ЭТАЖ
col9, col10 = st.columns([1, 3])
with col9:
    st.image("администрация/староста 3.jpg", width=250)
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
            <p>📞 <a href="tel:+79181572998">+79181572998</a></p>
            <p>📩 <a href="mailto:pedinmax@gmail.com">pedinmax@gmail.com</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 4 ЭТАЖ
col11, col12 = st.columns([1, 3])
with col11:
    st.image("администрация/староста 4.jpg", width=250)
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
            <p>📞 <a href="tel:+79531529087">+79531529087</a></p>
            <p>📩 <a href="mailto:danzel.loren@mail.ru">danzel.loren@mail.ru</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 5 ЭТАЖ
col13, col14 = st.columns([1, 3])
with col13:
    st.image("администрация/староста 5.jpg", width=250)
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
            <p>📞 <a href="tel:+79628651615">+79628651615</a></p>
            <p>📩 <a href="mailto:d.d.t13@mail.ru">d.d.t13@mail.ru</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 6 ЭТАЖ
col15, col16 = st.columns([1, 3])
with col15:
    st.image("администрация/староста 6.jpg", width=250)
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
            <p>📞 <a href="tel:+79283102210">+79283102210</a></p>
            <p>📩 <a href="mailto:vip.nike2006@mail.ru">vip.nike2006@mail.ru</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 7 ЭТАЖ
col17, col18 = st.columns([1, 3])
with col17:
    st.image("администрация/староста 7.jpg", width=250)
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
            <p>📞 <a href="tel:+79054244094">+79054244094</a></p>
            <p>📩 <a href="mailto:sofagon278@gmail.com">sofagon278@gmail.com</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 8 ЭТАЖ
col19, col20 = st.columns([1, 3])
with col19:
    st.image("администрация/староста 8.jpg", width=250)
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
            <p>📞 <a href="tel:+79140875194">+79140875194</a></p>
            <p>📩 <a href="mailto:aleksandra.drobko@mail.ru">aleksandra.drobko@mail.ru</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 9 ЭТАЖ
col21, col22 = st.columns([1, 3])
with col21:
    st.image("администрация/староста 9.jpg", width=250)
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
            <p>📞 <a href="tel:+79292424866">+79292424866</a></p>
            <p>📩 <a href="mailto:sowatasheryt@gmail.com">sowatasheryt@gmail.com</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 10 ЭТАЖ
col23, col24 = st.columns([1, 3])
with col23:
    st.image("администрация/староста 10.jpg", width=250)
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
            <p>📞 <a href="tel:+79201204040">+79201204040</a></p>
            <p>📩 <a href="mailto:Alvolkova@internet.ru">Alvolkova@internet.ru</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 11 ЭТАЖ
col25, col26 = st.columns([1, 3])
with col25:
    st.image("администрация/староста 11.jpg", width=250)
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
            <p>📞 <a href="tel:+79995325717">+79995325717</a></p>
            <p>📩 <a href="mailto:bagauri_diana@mail.ru">bagauri_diana@mail.ru</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 12 ЭТАЖ
col27, col28 = st.columns([1, 3])
with col27:
    st.image("администрация/нн.jpg", width=250)
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
            <p>📞 +79000000000</p>  
            <p>📩 mail.ru</p>
            <br>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Васильев Александр Владимирович 👨🏼‍💼")
st.markdown("""
<p>📞 <a href="tel:+78125210032">(812) 521-00-32</a></p>
""", unsafe_allow_html=True)
st.write("Зам. зав. общежитием: Левашова Людмила Григорьевна 👩🏼‍💼")
st.markdown("""
<p>📞 <a href="tel:+78125210033">(812) 521-00-33</a></p>
""", unsafe_allow_html=True)

st.markdown("🆘 [Чат со студенческим советом](https://t.me/helperKosygina19k2_bot)")
