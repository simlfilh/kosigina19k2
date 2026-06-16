import streamlit as st

st.title("🛤 Дорога до учебных корпусов")
st.divider()

col1, col2 = st.columns(2)
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
            .highlight-green {
                background-color: #C8E6C9; 
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                position: relative;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                position: relative;
            }
            .text-indent-content {
                position: relative;
                color: black;
                line-height: 1.4;
            }
            .yandex-map-container {
                background-color: #FFFFFF;
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 10px;
                height: 100%;
            }
            .yandex-map-container iframe {
                width: 100%;
                height: 430px;
                border: none;
                border-radius: 10px;
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
        </style>
        <div class="colored-container">
            <h3>📍 Адрес: Санкт-Петербург, пр-т Косыгина, д. 19, к. 2</h3>
            <div class="text-indent-content">
                <p class="highlight-blue">🚇 Наиболее удобный маршрут от м. Ладожская:</p>
            </div>
            <p>→ м. Ладожская</p>  
            <p>→ Выход к Ладожскому вокзалу (слева при выходе с эскалатора)</p>  
            <p>→ Трамвай №: 8, 59, 63, 64</p>  
            <p>→ Остановка: "ТК Народный"</p>
            <br>
            <div class="text-indent-content">
                <p class="highlight-green">🚌 Другие маршруты от м. Ладожская:</p>
            </div>
            <p>🚐 Маршрутное такси: № 22, 187, 401, 531, 533</p>
            <p>🚌 Автобус: № 21, 24, 30, 429, 453, 462, 531, 532</p>
            <p>🚎 Троллейбус: № 1, 22</p>
            
            <div class="route-info">
                <h4>🗺️ Маршрут до наб. канала Грибоедова 30-32</h4>
                <div class="route-detail">
                    <span>📏 Расстояние:</span>
                    <span><strong id="distance">~9.5 км</strong></span>
                </div>
                <div class="route-detail">
                    <span>⏱️ Время в пути:</span>
                    <span><strong id="time">~35 мин</strong></span>
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
        <div class="colored-container">
            <h3>🗺️ Мы на Яндекс Картах ⬇️</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Вставьте ваш API ключ вместо YOUR_API_KEY
    YOUR_API_KEY = "YOUR_API_KEY"  # Замените на ваш ключ
    
    yandex_map_html = f"""
    <div class="yandex-map-container">
        <script src="https://api-maps.yandex.ru/v3/?apikey={YOUR_API_KEY}&lang=ru_RU"></script>
        <div id="map" style="width: 100%; height: 430px; border-radius: 10px;"></div>
        <script>
            // Координаты в Санкт-Петербурге
            const START_POINT = [59.9347, 30.4426]; // Косыгина д19 к2
            const END_POINT = [59.9349, 30.3215];   // наб. канала Грибоедова 30-32
            
            function initMap() {{
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
                    
                    const distanceElem = document.getElementById('distance');
                    const timeElem = document.getElementById('time');
                    
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
            if (typeof ymaps !== 'undefined') {{
                ymaps.ready(initMap);
            }} else {{
                console.error('Яндекс Карты не загружены');
            }}
        </script>
    </div>
    """
    
    st.components.v1.html(yandex_map_html, height=480)

st.divider()

# Добавляем дополнительный блок с полезной информацией
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
