import streamlit as st
import base64

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
    
    # Способ 1: Использование iframe с HTML файлом
    st.components.v1.iframe(
        src="map.html",
        width=None,
        height=450,
        scrolling=False
    )

st.divider()

# Добавляем JavaScript для обновления информации
st.markdown("""
<script>
    // Слушаем сообщения от iframe
    window.addEventListener('message', function(event) {
        if (event.data.type === 'routeInfo') {
            const distanceElem = document.getElementById('distance');
            const timeElem = document.getElementById('time');
            
            if (distanceElem) {
                distanceElem.textContent = event.data.distance + ' км';
            }
            if (timeElem) {
                const minutes = event.data.time;
                if (minutes < 60) {
                    timeElem.textContent = '~' + minutes + ' мин';
                } else {
                    const hours = Math.floor(minutes / 60);
                    const mins = minutes % 60;
                    timeElem.textContent = '~' + hours + ' ч ' + mins + ' мин';
                }
            }
        }
    });
</script>
""", unsafe_allow_html=True)

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
