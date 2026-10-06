import streamlit as st
import streamlit.components.v1 as components

st.title("🏠 Видеообзор общежития СПбГЭУ №3 | пр-т Косыгина, д. 19, к. 2")
st.divider()

iframe_html = f"""
<iframe 
    src="https://vk.com/video_ext.php?oid=-241063201&id=456239021&hd=2" 
    width="640" 
    height="360" 
    frameborder="0" 
    allowfullscreen>
</iframe>
"""

components.html(iframe_html, height=380)
