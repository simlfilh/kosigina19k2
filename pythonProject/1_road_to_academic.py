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
    
    # Ваш API ключ
    API_KEY = "b1a79f0f-8389-4c37-b62c-2829d48b7241"
    
    # HTML с картой
    map_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://api-maps.yandex.ru/v3/?apikey={API_KEY}&lang=ru_RU"></script>
        <style>
            body {{ margin: 0; padding: 0; }}
            #map {{ width: 100%; height: 430px; border-radius: 10px; }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            // Координаты в Санкт-Петербурге
            const START_POINT = [59.9347, 30.4426]; // Косыгина д19 к2
            const END_POINT = [59.9349, 30.3215];   // наб. канала Грибоедова 30-32
            
            function initMap() {{
                // Создаем карту
                const map = new ymaps.Map('map', {{
                    center: [(START_POINT[0] + END_POINT[0]) / 2, (START_POINT[1] + END_POINT[1]) / 2],
                    zoom: 12,
                    controls: ['zoomControl', 'fullscreenControl']
                }});
                
                // Создаем метки
                const startMarker = new ymaps.Placemark(START_POINT, {{
                    hintContent: 'Косыгина д19 к2',
                    balloonContent: '📍 Начало маршрута<br>пр. Косыгина, д. 19, корп. 2'
                }}, {{
                    preset: 'islands#greenDotIcon'
                }});
                
                const endMarker = new ymaps.Placemark(END_POINT, {{
                    hintContent: 'наб. канала Грибоедова 30-32',
                    balloonContent: '📍 Конец маршрута<br>наб. канала Грибоедова, д. 30-32'
                }}, {{
                    preset: 'islands#redDotIcon'
                }});
                
                map.geoObjects.add(startMarker);
                map.geoObjects.add(endMarker);
                
                // Строим маршрут
                const multiRoute = new ymaps.multiRouter.MultiRoute({{
                    referencePoints: [START_POINT, END_POINT],
                    params: {{
                        routingMode: 'auto',
                        results: 1,
                        avoidTrafficJams: true
                    }}
                }}, {{
                    boundsAutoApply: true,
                    routeStrokeColor: '#0066ff',
                    routeStrokeWidth: 5,
                    routeActiveStrokeColor: '#FF6B00',
                    wayPointVisible: false,
                    viaPointVisible: false
                }});
                
                map.geoObjects.add(multiRoute);
                
                // Обновляем информацию
                multiRoute.events.add('ready', function() {{
                    const routes = multiRoute.getRoutes();
                    const firstRoute = routes[0];
                    const length = firstRoute.getLength();
                    const time = firstRoute.getTime();
                    
                    // Обновляем элементы в родительском окне
                    const distanceElem = window.parent.document.getElementById('distance');
                    const timeElem = window.parent.document.getElementById('time');
                    
                    if (distanceElem) {{
                        distanceElem.textContent = (length / 1000).toFixed(1) + ' км';
                    }}
                    if (timeElem) {{
                        const minutes = Math.floor(time / 60);
                        if (minutes < 60) {{
                            timeElem.textContent = '~' + minutes + ' мин';
                        }} else {{
                            const hours = Math.floor(minutes / 60);
                            const mins = minutes % 60;
                            timeElem.textContent = '~' + hours + ' ч ' + mins + ' мин';
                        }}
                    }}
                }});
            }}
            
            // Загружаем карту
            ymaps.ready(initMap);
        </script>
    </body>
    </html>
    """
    
    # Отображаем карту в Streamlit
    st.components.v1.html(map_html, height=460)

st.divider()

# Дополнительная информация
st.markdown("""
<style>
    .info-footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-top: 20px;
    }
    .info-footer h3 {
        margin-top: 0;
    }
    .info-footer a {
        color: #FFD700;
        text-decoration: none;
    }
    .info-footer a:hover {
        text-decoration: underline;
    }
</style>
<div class="info-footer">
    <h3>🚀 Полезная информация</h3>
    <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: space-between;">
        <div>
            <strong>📱 Приложения для навигации:</strong><br>
            • Яндекс Навигатор<br>
            • 2ГИС<br>
            • Google Maps
        </div>
        <div>
            <strong>🚕 Такси:</strong><br>
            • Яндекс Go<br>
            • Максим<br>
            • Gett
        </div>
        <div>
            <strong>🕐 Время работы:</strong><br>
            • Будни: 8:00 - 22:00<br>
            • Выходные: 9:00 - 20:00
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# JavaScript для обновления информации из iframe
st.markdown("""
<script>
    // Функция для обновления информации о маршруте
    function updateRouteInfo(distance, time) {
        const distanceElem = document.getElementById('distance');
        const timeElem = document.getElementById('time');
        
        if (distanceElem) {
            distanceElem.textContent = distance + ' км';
        }
        if (timeElem) {
            const minutes = Math.floor(time / 60);
            if (minutes < 60) {
                timeElem.textContent = '~' + minutes + ' мин';
            } else {
                const hours = Math.floor(minutes / 60);
                const mins = minutes % 60;
                timeElem.textContent = '~' + hours + ' ч ' + mins + ' мин';
            }
        }
    }
</script>
""", unsafe_allow_html=True)
