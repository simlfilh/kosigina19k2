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

        .docs-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 18px;
            border: 2px solid #000000;
            border-radius: 12px;
            overflow: hidden;
        }
        .docs-table th {
            background-color: #000000;
            color: black;
            padding: 12px;
            text-align: center;
            border: 1px solid #000000;
        }
        .docs-table td {
            padding: 12px;
            text-align: left;
            vertical-align: top;
            background-color: white;
            border: 1px solid #000000;
        }

        .price-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 18px;
            border: 2px solid #000000;
            border-radius: 12px;
            overflow: hidden;
        }
        .price-table th {
            background-color: #000000;
            color: black;
            padding: 12px;
            text-align: center;
            border: 1px solid #000000;
        }
        .price-table td {
            padding: 12px;
            text-align: left;
            background-color: white;
            border: 1px solid #000000;
        }

        .small-note {
            font-size: 16px;
            color: #555;
            font-style: italic;
        }
    </style>
    <div class="colored-container">
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Информация о заселении первокурсников в общежития</h3>
                </div>
            </div>
        <p>Уважаемые первокурсники!</p>
        <p>Бронирование мест в общежитиях будет доступно после публикации приказа о зачислении на 1 курс.</p>
        <br>
        <p>Студенты льготных категорий заселяются преимущественно в общежития СПбГЭУ.
        Перед заселением в общежитие студентам, имеющим льготы, необходимо предоставить 
        подтверждающие документы в Социальное управление по адресу: 
        наб. канала Грибоедова, 30/32, административный коридор, 2 этаж, комн. 2121.</p>
        <br>
        <p>❗️ Студентам, зачисленным на программы среднего профессионального образования (СПО), 
        общежитие предоставляется по адресу: Новоизмайловский пр., д. 16 (ФГБУ "Межвузовский студенческий 
        городок в Санкт-петербурге"). Для получения места в данном общежитии необходимо подать заявку
        в Жилищно-бытовом управлении.</p>
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
        <p><b>1.</b> Копия паспорта с регистрацией по месту жительства;</p>
        <p><b>2.</b> Копия медицинской справки с результатами флюорографического обследования;</p>
        <p><b>3.</b> 1 фото формата 3х4;</p>
        <p><b>4.</b> Для несовершеннолетних студентов: оригинал нотариально заверенного согласия родителей 
        (опекунов) на заключение договора найма жилого помещения в общежитии
        (<a href="https://unecon.ru/wp-content/uploads/2022/05/obrazec_soglasiya_dlya_roditeley_opekunov_0.pdf">образец заявления</a>);</p>
        <p><b>5.</b> Документы и копии документов, подтверждающих льготы, указанные в ч. 5 ст. 36 Федерального закона от 29 декабря 2012 г. 
        №273-ФЗ «Об образовании в Российской Федерации» (при наличии).</p>
            <br>
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Перечень документов, необходимых для заселения в общежития для граждан 
                    Российской Федерации, поступивших на программу аспирантуры:</h3>
                </div>
            </div>
        <p><b>1.</b> Копия паспорта с регистрацией по месту жительства;</p>
        <p><b>2.</b> Копия медицинской справки с результатами флюорографического обследования;</p>
        <p><b>3.</b> 1 фото формата 3х4;</p>
            <br>
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Перечень документов, необходимых для заселения в общежития для граждан иностранных государств,
                    поступивших на программы бакалавриата, специалитета, магистратуры и аспирантуры:</h3>
                </div>
            </div>
        <p><b>1.</b> Для несовершеннолетних студентов: оригинал нотариально заверенного согласия родителей 
        (опекунов) на заключение договора найма жилого помещения в общежитии
        (<a href="https://unecon.ru/wp-content/uploads/2022/05/obrazec_soglasiya_dlya_roditeley_opekunov_0.pdf">образец заявления</a>);</p>
        <p><b>2.</b> Паспорт (с нотариально заверенным переводом на русский язык либо переводом, заверенным подписью руководителя 
        Управления международного сотрудничества и печатью);</p>
        <p><b>3.</b> Медицинская справка с результатами флюорографического обследования + копия;</p>
    </div>
        """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-green">
            <div class="text-indent-content">
                <h3>Предварительная информация о количестве мест для заселения первокурсников в 2026 году:</h3>
            </div>
        </div>
        <p>Бакалавриат – 508 к/м</p>
        <p>Магистратура – 100 к/м</p>
        <br>
        <p>Информация о количестве мест в ФГБУ «Межвузовский студенческий городок в Санкт-Петербурге» будет опубликована позднее.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
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
        <p><b>Арендуемые общежития</b></p>
        <p><b>•</b> Новоизмайловский пр., д. 16 (коридорный тип), метро «Парк Победы» (ФГБУ "Межвузовский 
        студенческий городок в Санкт-Петербурге").</p>
        <p>Дополнительная информация: https://msg-spb.ru/</p>
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
        <p><b>•</b> Новоизмайловский пр., д. 16 (коридорный тип), метро «Парк Победы» (ФГБУ "Межвузовский 
        студенческий городок в Санкт-Петербурге").</p>
        <p>Дополнительная информация: https://msg-spb.ru/</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-red">
            <div class="text-indent-content">
                <h3>Стоимость проживания*:</h3>
            </div>
        </div>
        <table class="price-table">
            <thead>
                <tr><th>Адрес</th><th>Стоимость, руб.</th></tr>
            </thead>
            <tbody>
                <tr><td>Чкаловский пр., 27</td><td>4 538,00 - 4 961,00</td></tr>
                <tr><td>Косыгина пр., 19/2</td><td>6 732,00 - 7 122,00</td></tr>
                <tr><td>Воронежская ул., 38</td><td>4 476,00 - 4 893,00</td></tr>
                <tr><td>Воронежская ул., 69</td><td>3 532,00 - 3 922,00</td></tr>
                <tr><td>Рабфаковская ул., 3/1</td><td>4 500,00 — 10 000,00</td></tr>
            </tbody>
        </table>
        <br>
        <p>Первоначальная оплата проживания в общежитии производится за 3 месяца.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-blue">
            <div class="text-indent-content">
                <h3>Общежития сторонних организаций</h3>
            </div>
        </div>
        <table class="price-table">
            <thead>
                <tr><th>Адрес</th><th>Стоимость, руб.</th></tr>
            </thead>
            <tbody>
                <tr><td>Новоизмайловский пр-т, 16<br>(ФГБУ «Межвузовский студенческий городок в Санкт-Петербурге»)</td><td>5 500,00 — 15 500,00</td></tr>
            </tbody>
        </table>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="small-note">
            *Уважаемые студенты и абитуриенты!<br>
            Обращаем ваше внимание, что цены, указанные в таблице, не являются окончательными и устанавливаются в соответствии с возможными изменениями локально-нормативных актов Университета и распоряжениями Комитета по тарифам г. Санкт-Петербург.
        </div>
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

# --- Контакты ---
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





