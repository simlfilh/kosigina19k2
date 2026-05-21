import streamlit as st

st.title("👫 Заселение в общежитие СПбГЭУ №3")
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
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Информация о заселении первокурсников в общежития</h3>
                </div>
            </div>
        <p>Уважаемые первокурсники!</p>
        <p>❗️ Актуальные списки заселяющихся будут опубликованы по 
        <a href="https://priem.unecon.ru/stat/stat_hotel_grafik.php?z=1">ссылке</a>.</p>
        <br>
        <p>В день заселения в общежитие взимается плата за проживание на 3 месяца вперёд.</p>
        <br>
        <p>Студенты льготных категорий заселяются преимущественно в общежития СПбГЭУ.
        Перед заселением в общежитие студентам, имеющим льготы, необходимо предоставить 
        подтверждающие документы в Социальное управление по адресу: 
        наб. канала Грибоедова, 30/32, административный коридор, 2 этаж, комн. 2121.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-red">
            <div class="text-indent-content">
                <h3>❗️ Начало заселения в общежития СПбГЭУ 21.08.2026.</h3>
            </div>
        </div>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Порядок бронирования общежития для первокурсников:</h3>
                </div>
            </div>
        <p><b>1.</b> Проверить наличие вашего ФИО в
        <a href="https://priem.unecon.ru/stat/stat_hotel_grafik.php?z=1">актуальном списке заселяющихся</a>.</p>
        <p><b>2.</b> Выбрать дату заселения, общежитие, комнату.</p>
        <p><b>3.</b> Прибыть в выбранный день с 10:00 до 17:00 по адресу выбранного общежития.</p>
        <p><b>4.</b> Студенты, не включенные в список на заселение, обеспечиваются общежитием после основного потока заселения 
        при наличии свободных мест (обращаться в чат Жилищно-бытового управления через Личный кабинет).</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <br>
        <p>❗️ Студентам, зачисленным на программы среднего профессионального образования (СПО), 
        общежитие предоставляется по адресу: Новоизмайловский пр., д. 16.</p>
        <br>
        <p>❗️ Оформление договора найма жилого помещения производится только при наличии всех  документов из списка.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Перечень документов, необходимых для заселения в общежития для граждан 
                    Российской Федерации, поступивших на программы бакалавриата, специалитета и магистратуры:</h3>
                </div>
            </div>
        <p><b>1.</b> Копия паспорта с регистрацией по месту жительства (исключается г. Санкт-Петербург);</p>
        <p><b>2.</b> Копия медицинской справки (форма 086) с результатами флюорографического обследования;</p>
        <p><b>3.</b> 1 фото (любой формат);</p>
        <p><b>4.</b> Для несовершеннолетних студентов: оригинал нотариально заверенного согласия родителей 
        (опекунов) на заключение договора найма жилого помещения в общежитии
        (<a href="https://unecon.ru/wp-content/uploads/2022/05/obrazec_soglasiya_dlya_roditeley_opekunov_0.pdf">образец заявления</a>).</p>
            <br>
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Адреса общежитий для поступивших на программы бакалавриата и специалитета:</h3>
                </div>
            </div>
        <p><b>Общежития СПбГЭУ</b></p>
        <p><b>•</b> пр. Косыгина, д.19/2 (блочный тип), метро «Ладожская»;</p>
        <p><b>•</b> Воронежская ул., д.38 (коридорный тип), метро «Обводный канал»;</p>
        <p><b>•</b> Воронежская ул., д.69 (блочный тип), метро «Обводный канал»;</p>
        <p><b>•</b> Чкаловский пр., д.27 (коридорный тип), метро «Чкаловская», «Петроградская».</p>
            <br>
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Адреса общежитий для поступивших на программы магистратуры и аспирантуры:</h3>
                </div>
            </div>
        <p><b>Общежития СПбГЭУ</b></p>
        <p><b>•</b> ул. Рабфаковская, д.3/1 (квартирный тип), метро «Пролетарская»;</p>
            <br>
        <p><b>Арендуемые общежития</b></p>
        <p><b>•</b> Новоизмайловский пр., д. 16 (коридорный тип), метро «Электросила».</p>
        <p><b>•</b> МСГ, метро «Парк Победы».</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Перечень документов, необходимых для заселения в общежития для граждан иностранных государств:</h3>
                </div>
            </div>
        <p><b>1.</b> Копия паспорта с заверенным переводом на русский язык;</p>
        <p><b>2.</b> Копия медицинской справки с результатами флюорографического обследования;</p>
        <p><b>3.</b> 1 фото (любой формат);</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-red">
                <div class="text-indent-content">
                    <h3>Временная регистрация</h3>
                </div>
            </div>
        <p>Получение временной регистрации происходит в течение 1-2 месяцев.</p>
        <p>Первыми временную регистрацию получают юноши, после - девушки.</p>
        <p>Списки с готовыми регистрациями будут опубликованы в общем чате общежития, TG-канале общежития 
        и будут находиться у администрации общежития.</p>
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


