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
        
        /* Таблица документов - с внешней чёрной рамкой */
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
            background-color: #2196F3;
            color: white;
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
        
        /* Таблица стоимости - с внешней чёрной рамкой */
        .price-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 18px;
            border: 10px solid #000000;
            border-radius: 12px;
            overflow: hidden;
        }
        .price-table th {
            background-color: #4CAF50;
            color: white;
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
        <p>❗️ Бронирование мест в общежитиях будет доступно <b>после публикации приказа</b> 
        о зачислении на 1 курс.</p>
        <br>
        <p>Студенты <b>льготных категорий</b> заселяются преимущественно в общежития СПбГЭУ.
        Перед заселением в общежитие студентам, имеющим льготы, необходимо предоставить 
        подтверждающие документы в Социальное управление по адресу: 
        наб. канала Грибоедова, 30/32, административный коридор, 2 этаж, комн. 2121.</p>
        <br>
        <p>Студентам, зачисленным на <b>программы среднего профессионального образования (СПО)</b>, 
        общежитие предоставляется по адресу:
        Новоизмайловский пр., д. 16 (ФГБУ «Межвузовский студенческий городок в Санкт-Петербурге»). 
        Для получения места в данном общежитии необходимо подать заявку в Жилищно-бытовом управлении.</p>
    </div>
""", unsafe_allow_html=True)

# --- Таблица документов для граждан РФ ---
st.markdown("""
    <div class="colored-container">
        <div class="highlight-blue">
            <div class="text-indent-content">
                <h3>Перечень документов, необходимых для заселения в общежития для граждан Российской Федерации:</h3>
            </div>
        </div>
        <table class="docs-table">
            <thead>
                <tr><th>Бакалавриат, специалитет, магистратура</th><th>Аспирантура</th></tr>
            </thead>
            <tbody>
                <tr><td>1) для несовершеннолетних студентов: оригинал нотариально заверенного согласия родителей (законных представителей) на заключение договора найма жилого помещения в общежитии;</td><td>1) копия паспорта с регистрацией по месту жительства;</td></tr>
                <tr><td>2) копия паспорта с регистрацией по месту жительства;</td><td>2) копия медицинской справки с результатами флюорографического обследования;</td></tr>
                <tr><td>3) копия медицинской справки с результатами флюорографического обследования;</td><td>3) 1 фото размером 3 x 4.</td></tr>
                <tr><td>4) 1 фото размером 3 x 4;</td><td></td></tr>
                <tr><td>5) документы и копии документов, подтверждающих льготы, указанные в ч. 5 ст. 36 Федерального закона от 29 декабря 2012 г. №273-ФЗ «Об образовании в Российской Федерации» (при наличии).</td><td></td></tr>
            </tbody>
        </table>
    </div>
""", unsafe_allow_html=True)

# --- Таблица для иностранцев ---
st.markdown("""
    <div class="colored-container">
        <div class="highlight-blue">
            <div class="text-indent-content">
                <h3>Перечень документов, необходимых для заселения в общежития для граждан иностранных государств:</h3>
                <p>Бакалавриат, специалитет, магистратура, аспирантура</p>
            </div>
        </div>
        <p><b>1)</b> Студентам, не достигшим 18-летнего возраста дополнительно предоставить НОТАРИАЛЬНО ЗАВЕРЕННОЕ СОГЛАСИЕ РОДИТЕЛЕЙ (ОПЕКУНОВ) на заключение договора найма жилого помещения в общежитии (образец заявления на странице Жилищно-бытового управления);</p>
        <p><b>2)</b> Паспорт (с нотариально заверенным переводом на русский язык либо переводом, заверенным подписью руководителя Управления международного сотрудничества и печатью);</p>
        <p><b>3)</b> Медицинская справка с результатами флюорографического обследования + копия.</p>
    </div>
""", unsafe_allow_html=True)

# --- Количество мест ---
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

# --- Адреса бакалавриат/специалитет ---
st.markdown("""
    <div class="colored-container">
        <div class="highlight-blue">
            <div class="text-indent-content">
                <h3>Адреса общежитий для поступивших на программы бакалавриата, специалитета:</h3>
            </div>
        </div>
        <p><b>Общежития СПбГЭУ:</b></p>
        <p>• пр. Косыгина, д.19/2 (блочный тип), метро «Ладожская»;</p>
        <p>• Воронежская ул., д.38 (коридорный тип), метро «Обводный канал»;</p>
        <p>• Воронежская ул., д.69 (блочный тип), метро «Обводный канал»;</p>
        <p>• Чкаловский пр., д.27 (коридорный тип), метро «Чкаловская», «Петроградская».</p>
        <br>
        <p><b>Арендуемые общежития:</b></p>
        <p>• Новоизмайловский пр., д. 16 (коридорный тип), метро «Парк Победы» (ФГБУ «Межвузовский студенческий городок в Санкт-Петербурге»).</p>
        <p>• Дополнительная информация: <a href="https://msg-spb.ru/" target="_blank">https://msg-spb.ru/</a></p>
    </div>
""", unsafe_allow_html=True)

# --- Адреса магистратура/аспирантура ---
st.markdown("""
    <div class="colored-container">
        <div class="highlight-blue">
            <div class="text-indent-content">
                <h3>Адреса общежитий для поступивших на программы магистратуры, аспирантуры:</h3>
            </div>
        </div>
        <p><b>Общежития СПбГЭУ:</b></p>
        <p>• ул. Рабфаковская, д.3/1 (квартирный тип), метро «Пролетарская».</p>
        <br>
        <p><b>Арендуемые общежития:</b></p>
        <p>• Новоизмайловский пр., д. 16 (коридорный тип), метро «Парк Победы» (ФГБУ «Межвузовский студенческий городок в Санкт-Петербурге»).</p>
        <p>• Дополнительная информация: <a href="https://msg-spb.ru/" target="_blank">https://msg-spb.ru/</a></p>
    </div>
""", unsafe_allow_html=True)

# --- Таблица стоимости ---
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

# --- Таблица сторонних организаций ---
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

# --- Примечание о ценах ---
st.markdown("""
    <div class="colored-container">
        <div class="small-note">
            *Уважаемые студенты и абитуриенты!<br>
            Обращаем ваше внимание, что цены, указанные в таблице, не являются окончательными и устанавливаются в соответствии с возможными изменениями локально-нормативных актов Университета и распоряжениями Комитета по тарифам г. Санкт-Петербург.
        </div>
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
