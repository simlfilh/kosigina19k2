import streamlit as st
import streamlit.components.v1 as components

video_id = "-241063201_456239017"  # oid_id

iframe_html = f"""
<iframe 
    src="https://vk.com/video_ext.php?oid=-241063201&id=456239017&hd=2" 
    width="640" 
    height="360" 
    frameborder="0" 
    allowfullscreen>
</iframe>
"""

components.html(iframe_html, height=380)
