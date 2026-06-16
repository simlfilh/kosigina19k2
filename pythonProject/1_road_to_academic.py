import streamlit as st

st.set_page_config(
    page_title="Маршрут в Санкт-Петербурге",
    page_icon="🗺️",
    layout="wide"
)

st.title("🛤 Дорога до учебных корпусов")
st.divider()

col1, col2 = st.columns(2, gap="medium")

with col1:
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
        <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🏛️ Главный корпус СПбГЭУ</h3> 
                </div>
            </div>
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
    st.markdown("""
        <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h3>🗺️ Маршрут на Яндекс Картах</h3>
        </div>
    """, unsafe_allow_html=True)
    
    map_html = """
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
    
    st.components.v1.html(map_html, height=460)

