import streamlit as st
import os

# Configuración
st.set_page_config(page_title="Litoral Automotores", page_icon="🚗", layout="wide")

# Estilo Estilo Mercado Libre
st.markdown("""
    <style>
    .main { background-color: #f4f4f4; }
    .car-card {
        background-color: white; padding: 15px; border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center;
    }
    .price-tag { color: #00a650; font-size: 24px; font-weight: bold; margin: 5px 0px; }
    .car-name { font-size: 19px; font-weight: bold; color: #333; height: 50px; overflow: hidden; }
    .btn-whatsapp {
        display: block; background-color: #3483fa; color: white !important;
        padding: 12px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🚗 Litoral Automotores</h1>", unsafe_allow_html=True)
st.markdown("---")

# Obtener TODAS las fotos .jpg del repositorio
fotos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])

col1, col2 = st.columns(2)

# --- AUTO 1: SMA C81 ---
with col1:
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    # Intentamos cargar la primera foto de la lista
    if len(fotos) > 0:
        st.image(fotos[0], use_container_width=True)
    
    st.markdown('<div class="car-name">SMA C81 Full 1.8 (2009)</div>', unsafe_allow_html=True)
    st.markdown('<div class="price-tag">U$S 3.500</div>', unsafe_allow_html=True)
    st.write("📍 Paysandú | 1.8 Nafta Inyección")
    
    url_sma = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20SMA%20C81"
    st.markdown(f'<a href="{url_sma}" target="_blank" class="btn-whatsapp">Ver / Contactar</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- AUTO 2: HYUNDAI ACCENT ---
with col2:
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    # Intentamos cargar la última foto de la lista (que suele ser el Hyundai por nombre)
    if len(fotos) > 1:
        st.image(fotos[-1], use_container_width=True)
    
    st.markdown('<div class="car-name">Hyundai Accent 1.5 (1995)</div>', unsafe_allow_html=True)
    st.markdown('<div class="price-tag">¡Súper Económico!</div>', unsafe_allow_html=True)
    st.write("📍 Paysandú | Documentación al día")
    
    url_h = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20Hyundai%20Accent"
    st.markdown(f'<a href="{url_h}" target="_blank" class="btn-whatsapp">Ver / Contactar</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #999;'>© 2026 Litoral Automotores | Paysandú</p>", unsafe_allow_html=True)
