import streamlit as st
import requests
from io import StringIO

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
            .highlight-green {
                background-color: #C8E6C9;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
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
            <h3>📍 Адрес: Санкт-Петербург, пр-т Косыгина, д. 19, к. 2</h3>
            <div class="highlight-blue">
                <strong>🚇 Наиболее удобный маршрут от м. Ладожская:</strong>
            </div>
            <p>→ м. Ладожская</p>  
            <p>→ Выход к Ладожскому вокзалу (слева при выходе с эскалатора)</p>  
            <p>→ Трамвай №: 8, 59, 63, 64</p>  
            <p>→ Остановка: "ТК Народный"</p>
            <br>
            <div class="highlight-green">
                <strong>🚌 Другие маршруты от м. Ладожская:</strong>
            </div>
            <p>🚐 Маршрутное такси: № 22, 187, 401, 531, 533</p>
            <p>🚌 Автобус: № 21, 24, 30, 429, 453, 462, 531, 532</p>
            <p>🚎 Троллейбус: № 1, 22</p>
            
            <div class="route-info">
                <h4>🗺️ Маршрут до наб. канала Грибоедова 30-32</h4>
                <div class="route-detail">
                    <span>📏 Расстояние:</span>
                    <span><strong id="distance">Загрузка...</strong></span>
                </div>
                <div class="route-detail">
                    <span>⏱️ Время в пути:</span>
                    <span><strong id="time">Загрузка...</strong></span>
                </div>
                <div class="route-detail">
                    <span>🚗 Способ:</span>
                    <span><strong>Автомобиль</strong></span>
                </div>
                <div style="margin-top: 10px; font-size: 14px; color: #666;">
                    💡 Нажмите на маршрут на карте для детальных инструкций
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h3>🗺️ Мы на Яндекс Картах</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Используем готовый виджет Яндекс Карт
    st.components.v1.iframe(
        src="https://yandex.ru/map-widget/v1/?um=constructor%3A1a2b3c4d5e6f7g8h9i0j&source=constructor",
        width=None,
        height=430,
        scrolling=False
    )
