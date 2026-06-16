import streamlit as st

st.set_page_config(
    page_title="Маршруты до учебных корпусов СПбГЭУ",
    page_icon="🗺️",
    layout="wide"
)

st.title("🏛️ Дорога до учебных корпусов СПбГЭУ")
st.markdown("### 📍 От общежития №3 по адресу пр. Косыгина, д. 19, к. 2")
st.divider()


st.markdown("""
    <style>
        .colored-container {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 10px;
            color: black !important;
            line-height: 1.0;
            font-size: 21px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .image-container {
            background-color: #FFFFFF; 
           border-radius: 10px;      
           padding: 20px;            
           margin-bottom: 10px;      
            height: 100%;           
           display: flex;
           align-items: center;     
           justify-content: center; 
        }
        .image-container img {
           max-width: 100%;
            max-height: 100%;
           border-radius: 5px;     
           object-fit: contain;    
        }
        .highlight-blue {
            background-color: #B3E5FC;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .text-indent-content {
            position: relative;
            color: black;
            line-height: 1.4;
        }
        .route-info {
            background-color: #FFF3E0;
            border-radius: 10px;
            padding: 15px;
            margin-top: 15px;
            border-left: 4px solid #FF6B00;
        }
        .route-info h4 {
            margin: 0 0 10px 0;
            color: #E65100;
        }
        .route-info p {
            margin: 5px 0;
            font-size: 16px;
        }
        .route-detail {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }
        .route-detail:last-child {
            border-bottom: none;
        }
        .info-footer {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            margin-top: 20px;
        }
        .info-footer a {
            color: #FFD700;
            text-decoration: none;
        }
        .info-footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🏛️ Главный корпус СПбГЭУ</h3> 
                </div>
            </div>
            <br>
            <p>📍 Адрес: <b>наб. канала Грибоедова, 30-32, литер А</b></p>  
            <div class="route-info">
                <h4>🗺️ Маршрут от пр. Косыгина, д. 19, к. 2</h4>
                <div class="route-detail">
                    <span>📏 Расстояние:</span>
                    <span><strong>~9.5 км</strong></span>
                </div>
                <div class="route-detail">
                    <span>⏱️ Время в пути:</span>
                    <span><strong>~35 мин</strong></span>
                </div>
                <div class="route-detail">
                    <span>🚌 Способ:</span>
                    <span><strong>Общественный транспорт</strong></span>
                </div>
                <div style="margin-top: 10px; font-size: 14px; color: #666;">
                    💡 Нажмите на карту для детальных инструкций
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    map_html_1 = """
    <div style="position:relative;overflow:hidden;border-radius: 10px;">
        <a href="https://yandex.ru/maps/2/saint-petersburg/?utm_medium=mapframe&utm_source=maps" 
           style="color:#eee;font-size:12px;position:absolute;top:0px;z-index:10;">
           Санкт‑Петербург
        </a>
        <a href="https://yandex.ru/maps/2/saint-petersburg/?ll=30.404917%2C59.935563&mode=routes&rtext=59.944003%2C30.482263~59.931834%2C30.325628&rtn=1&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzQxMDc1NhJV0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywg0L_RgNC-0YHQv9C10LrRgiDQmtC-0YHRi9Cz0LjQvdCwLCAxOdC6MiIKDa3b80EVqMZvQg%2C%2C~ymapsbm1%3A%2F%2Forg%3Foid%3D1357072604&utm_medium=mapframe&utm_source=maps&z=13" 
           style="color:#eee;font-size:12px;position:absolute;top:14px;z-index:10;">
           Яндекс Карты
        </a>
        <iframe 
            src="https://yandex.ru/map-widget/v1/?ll=30.404917%2C59.935563&mode=routes&rtext=59.944003%2C30.482263~59.931834%2C30.325628&rtn=1&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzQxMDc1NhJV0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywg0L_RgNC-0YHQv9C10LrRgiDQmtC-0YHRi9Cz0LjQvdCwLCAxOdC6MiIKDa3b80EVqMZvQg%2C%2C~ymapsbm1%3A%2F%2Forg%3Foid%3D1357072604&z=13" 
            width="100%" 
            height="430" 
            frameborder="1" 
            allowfullscreen="true" 
            style="position:relative;border-radius: 10px;border: none;">
        </iframe>
    </div>
    """
    st.components.v1.html(map_html_1, height=460)

st.divider()


col3, col4 = st.columns(2, gap="medium")

with col3:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🏛️ Корпус на Москательном переулке</h3> 
                </div>
            </div>
            <br>
            <p>📍 Адрес: <b>Москательный переулок, д. 4</b></p>  
            <div class="route-info">
                <h4>🗺️ Маршрут от пр. Косыгина, д. 19, к. 2</h4>
                <div class="route-detail">
                    <span>📏 Расстояние:</span>
                    <span><strong>~10 км</strong></span>
                </div>
                <div class="route-detail">
                    <span>⏱️ Время в пути:</span>
                    <span><strong>~40 мин</strong></span>
                </div>
                <div class="route-detail">
                    <span>🚌 Способ:</span>
                    <span><strong>Общественный транспорт</strong></span>
                </div>
                <div style="margin-top: 10px; font-size: 14px; color: #666;">
                    💡 Нажмите на карту для детальных инструкций
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    map_html_2 = """
    <div style="position:relative;overflow:hidden;border-radius: 10px;">
        <a href="https://yandex.ru/maps/2/saint-petersburg/?utm_medium=mapframe&utm_source=maps" 
            style="color:#eee;font-size:12px;position:absolute;top:0px;z-index:10;">
            Санкт‑Петербург
        </a>
        <a href="https://yandex.ru/maps/2/saint-petersburg/?ll=30.377173%2C59.935563&mode=routes&rtext=59.944003%2C30.482263~59.930322%2C30.323593&rtn=1&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzQxMDc1NhJV0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywg0L_RgNC-0YHQv9C10LrRgiDQmtC-0YHRi9Cz0LjQvdCwLCAxOdC6MiIKDa3b80EVqMZvQg%2C%2C~ymapsbm1%3A%2F%2Forg%3Foid%3D1118957269&utm_medium=mapframe&utm_source=maps&z=11.95" 
           style="color:#eee;font-size:12px;position:absolute;top:14px;z-index:10;">
           Яндекс Карты
        </a>
        <iframe 
            src="https://yandex.ru/map-widget/v1/?ll=30.377173%2C59.935563&mode=routes&rtext=59.944003%2C30.482263~59.930322%2C30.323593&rtn=1&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzQxMDc1NhJV0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywg0L_RgNC-0YHQv9C10LrRgiDQmtC-0YHRi9Cz0LjQvdCwLCAxOdC6MiIKDa3b80EVqMZvQg%2C%2C~ymapsbm1%3A%2F%2Forg%3Foid%3D1118957269&z=11.95" 
            width="100%" 
            height="430" 
            frameborder="1" 
            allowfullscreen="true" 
            style="position:relative;border-radius: 10px;border: none;">
        </iframe>
    </div>
    """
    st.components.v1.html(map_html_2, height=460)

st.divider()


col5, col6 = st.columns(2, gap="medium")

with col5:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🏛️ Корпус на ул. Марата</h3> 
                </div>
            </div>
            <br>
            <p>📍 Адрес: <b>ул. Марата, д. 27</b></p>  
            <div class="route-info">
                <h4>🗺️ Маршрут от пр. Косыгина, д. 19, к. 2</h4>
                <div class="route-detail">
                    <span>📏 Расстояние:</span>
                    <span><strong>~9.5 км</strong></span>
                </div>
                <div class="route-detail">
                    <span>⏱️ Время в пути:</span>
                    <span><strong>~37 мин</strong></span>
                </div>
                <div class="route-detail">
                    <span>🚌 Способ:</span>
                    <span><strong>Общественный транспорт</strong></span>
                </div>
                <div style="margin-top: 10px; font-size: 14px; color: #666;">
                    💡 Нажмите на карту для детальных инструкций
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col6:
    map_html_3 = """
    <div style="position:relative;overflow:hidden;border-radius: 10px;">
        <a href="https://yandex.ru/maps/2/saint-petersburg/?utm_medium=mapframe&utm_source=maps" 
            style="color:#eee;font-size:12px;position:absolute;top:0px;z-index:10;">
           Санкт‑Петербург
        </a>
        <a href="https://yandex.ru/maps/2/saint-petersburg/?ll=30.377173%2C59.935563&mode=routes&rtd=0&rtext=59.944003%2C30.482263~59.927268%2C30.351716&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzQxMDc1NhJV0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywg0L_RgNC-0YHQv9C10LrRgiDQmtC-0YHRi9Cz0LjQvdCwLCAxOdC6MiIKDa3b80EVqMZvQg%2C%2C~ymapsbm1%3A%2F%2Forg%3Foid%3D24633073600&utm_medium=mapframe&utm_source=maps&z=11.95" 
            style="color:#eee;font-size:12px;position:absolute;top:14px;z-index:10;">
            Яндекс Карты
        </a>    
        <iframe 
            src="https://yandex.ru/map-widget/v1/?ll=30.377173%2C59.935563&mode=routes&rtd=0&rtext=59.944003%2C30.482263~59.927268%2C30.351716&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzQxMDc1NhJV0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywg0L_RgNC-0YHQv9C10LrRgiDQmtC-0YHRi9Cz0LjQvdCwLCAxOdC6MiIKDa3b80EVqMZvQg%2C%2C~ymapsbm1%3A%2F%2Forg%3Foid%3D24633073600&z=11.95" 
            width="100%" 
            height="430" 
            frameborder="1" 
            allowfullscreen="true" 
            style="position:relative;border-radius: 10px;border: none;">
        </iframe>
    </div>
    """
    st.components.v1.html(map_html_3, height=460)

st.divider()


col7, col8 = st.columns(2, gap="medium")

with col7:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🏛️ Корпус на Прилукской ул.</h3> 
                </div>
            </div>
            <br>
            <p>📍 Адрес: <b>ул. Прилукская, д. 3</b></p>  
            <div class="route-info">
                <h4>🗺️ Маршрут от пр. Косыгина, д. 19, к. 2</h4>
                <div class="route-detail">
                    <span>📏 Расстояние:</span>
                    <span><strong>~9 км</strong></span>
                </div>
                <div class="route-detail">
                    <span>⏱️ Время в пути:</span>
                    <span><strong>~35 мин</strong></span>
                </div>
                <div class="route-detail">
                    <span>🚌 Способ:</span>
                    <span><strong>Общественный транспорт</strong></span>
                </div>
                <div style="margin-top: 10px; font-size: 14px; color: #666;">
                    💡 Нажмите на карту для детальных инструкций
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col8:
    map_html_4 = """
    <div style="position:relative;overflow:hidden;border-radius: 10px;">
        <a href="https://yandex.ru/maps/2/saint-petersburg/?utm_medium=mapframe&utm_source=maps" 
            style="color:#eee;font-size:12px;position:absolute;top:0px;z-index:10;">
            Санкт‑Петербург
        </a>
        <a href="https://yandex.ru/maps/2/saint-petersburg/?ll=30.377173%2C59.935563&mode=routes&rtext=59.944003%2C30.482263~59.910432%2C30.341556&rtn=1&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzQxMDc1NhJV0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywg0L_RgNC-0YHQv9C10LrRgiDQmtC-0YHRi9Cz0LjQvdCwLCAxOdC6MiIKDa3b80EVqMZvQg%2C%2C~ymapsbm1%3A%2F%2Forg%3Foid%3D64108962043&utm_medium=mapframe&utm_source=maps&z=11.95" 
            style="color:#eee;font-size:12px;position:absolute;top:14px;z-index:10;">
           Яндекс Карты
        </a>
        <iframe 
            src="https://yandex.ru/map-widget/v1/?ll=30.377173%2C59.935563&mode=routes&rtext=59.944003%2C30.482263~59.910432%2C30.341556&rtn=1&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzQxMDc1NhJV0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywg0L_RgNC-0YHQv9C10LrRgiDQmtC-0YHRi9Cz0LjQvdCwLCAxOdC6MiIKDa3b80EVqMZvQg%2C%2C~ymapsbm1%3A%2F%2Forg%3Foid%3D64108962043&z=11.95" 
            width="100%" 
            height="430" 
            frameborder="1" 
            allowfullscreen="true" 
            style="position:relative;border-radius: 10px;border: none;">
        </iframe>
    </div>
    """
    st.components.v1.html(map_html_4, height=460)

st.divider()


col9, col10 = st.columns(2, gap="medium")

with col9:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🏛️ Корпус на 7-й Красноармейской</h3> 
                </div>
            </div>
            <br>
            <p>📍 Адрес: <b>7-я Красноармейская ул., д. 6-8</b></p>  
            <div class="route-info">
                <h4>🗺️ Маршрут от пр. Косыгина, д. 19, к. 2</h4>
                <div class="route-detail">
                    <span>📏 Расстояние:</span>
                    <span><strong>~9.5 км</strong></span>
                </div>
                <div class="route-detail">
                    <span>⏱️ Время в пути:</span>
                    <span><strong>~38 мин</strong></span>
                </div>
                <div class="route-detail">
                    <span>🚌 Способ:</span>
                    <span><strong>Общественный транспорт</strong></span>
                </div>
                <div style="margin-top: 10px; font-size: 14px; color: #666;">
                    💡 Нажмите на карту для детальных инструкций
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col10:
    map_html_5 = """
    <div style="position:relative;overflow:hidden;border-radius: 10px;">
        <a href="https://yandex.ru/maps/2/saint-petersburg/?utm_medium=mapframe&utm_source=maps" 
            style="color:#eee;font-size:12px;position:absolute;top:0px;z-index:10;">
            Санкт‑Петербург
        </a>
        <a href="https://yandex.ru/maps/2/saint-petersburg/?ll=30.399920%2C59.927935&mode=routes&rtext=59.944003%2C30.482263~59.911288%2C30.316130&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DIgoNrdvzQRWpxm9C~ymapsbm1%3A%2F%2Forg%3Foid%3D1002219955&utm_medium=mapframe&utm_source=maps&z=11.27" style="color:#eee;font-size:12px;position:absolute;top:14px;">
            style="color:#eee;font-size:12px;position:absolute;top:14px;z-index:10;">
            Яндекс Карты
        </a>
        <iframe 
            src="https://yandex.ru/map-widget/v1/?ll=30.399920%2C59.927935&mode=routes&rtext=59.944003%2C30.482263~59.911288%2C30.316130&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DIgoNrdvzQRWpxm9C~ymapsbm1%3A%2F%2Forg%3Foid%3D1002219955&z=11.27" 
            width="100%" 
            height="430" 
            frameborder="1" 
            allowfullscreen="true" 
            style="position:relative;border-radius: 10px;border: none;">
        </iframe>
    </div>
    """
    st.components.v1.html(map_html_5, height=460)
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

