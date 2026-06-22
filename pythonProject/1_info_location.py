import streamlit as st

st.title("🏠 Общежитие СПбГЭУ №3")
st.divider()

st.subheader("Приветствуем вас, дорогие студенты, в нашем общежитии!")
st.subheader("Мы рады, что вы стали частью нашей дружной студенческой семьи!")
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
        </style>
        <div class="colored-container">
            <h3>Адрес: Санкт-Петербург, пр-т Косыгина, д. 19, к. 2</h3>
                <div class="text-indent-content">
                    <p class="highlight-blue">Наиболее удобный маршрут от м. Ладожская:</p>
                </div>
            <p>→ м. Ладожская</p>  
            <p>→ Выход к Ладожскому вокзалу (слева при выходе с эскалатора)</p>  
            <p>→ Трамвай №: 8, 59, 63, 64</p>  
            <p>→ Остановка: "ТК Народный"</p>
        <br>
                <div class="text-indent-content">
                    <p class="highlight-green">Другие маршруты от м. Ладожская:</p>
                </div>
            <p>  Маршрутное такси: № 22, 187, 401, 531, 533</p>
            <p>  Автобус: № 21, 24, 30, 429, 453, 462, 531, 532</p>
            <p>  Троллейбус: № 1, 22</p>
        </div>
                """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="colored-container">
            <h3>Мы в Google Maps ⬇️</h3>
        </div>
                """, unsafe_allow_html=True)
    st.components.v1.html("""
        <div style="position:relative;overflow:hidden;">
            <a href="https://yandex.ru/maps/2/saint-petersburg/?utm_medium=mapframe&utm_source=maps" 
                style="color:#eee;font-size:12px;position:absolute;top:0px;">
                Санкт‑Петербург
            </a>
            <a href="https://yandex.ru/maps/2/saint-petersburg/?ll=30.462418%2C59.938208&mode=routes&rtext=59.932429%2C30.439201~59.944003%2C30.482263&rtt=mt&ruri=ymapsbm1%3A%2F%2Ftransit%2Fstop%3Fid%3Dstation__9805940~&utm_medium=mapframe&utm_source=maps&z=14.94" 
                style="color:#eee;font-size:12px;position:absolute;top:14px;">
                Яндекс Карты
            </a>
            <iframe src="https://yandex.ru/map-widget/v1/?ll=30.462418%2C59.938208&mode=routes&rtext=59.932429%2C30.439201~59.944003%2C30.482263&rtt=mt&ruri=ymapsbm1%3A%2F%2Ftransit%2Fstop%3Fid%3Dstation__9805940~&z=14.94" 
                width="100%" 
                height="400" 
                frameborder="1" 
                allowfullscreen="true" 
                style="position:relative;border-radius: 10px;border: none;">
            </iframe>
        </div>
                    """, height=440)
st.divider()

col3, col4 = st.columns([1, 2])
with col4:
    st.markdown("""
        <div class="colored-container">
            <h3>Об общежитии</h3>
            <p>• Блочный тип проживания (2-3 комнаты по 2-3 человека, собственный санузел на блок)</p>  
            <p>• 12 этажей | 966 мест</p>
            <p>• На каждом этаже 2 кухни, оснащенные электрическими плитами, столами, микроволновками</p>
            <p>• Общая прачечная</p>
            <p>• Бесплатный интернет</p>
            <p>• 5-10 минут от метро на трамвае, 20-30 минут пешком от метро</p>
        </div>
                """, unsafe_allow_html=True)
with col3:
    st.image("здание общежития_к19.jpg",
             use_container_width=True)
st.divider()

st.markdown("*❗️ Пожалуйста, прежде чем связываться с администрацией, ознакомьтесь со всей информацией на сайте.*")
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
