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
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1998.2520184102325!2d30.48016407706522!3d59.94455297491812!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46962de52f91ffd5%3A0x149fa7d72033b95b!2z0L_RgC4g0JrQvtGB0YvQs9C40L3QsCwgMTkg0LrQvtGA0L_Rg9GBIDIsINCh0LDQvdC60YIt0J_QtdGC0LXRgNCx0YPRgNCzLCAxOTU0MjY!5e0!3m2!1sru!2sru!4v1749385448662!5m2!1sru!2sru" 
            width="100%" 
            height="430" 
            style="border:0; border-radius: 10px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
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
