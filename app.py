import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Catálogo", page_icon="🚗", layout="wide")

# Estilo CSS para que parezca una galería de ventas
st.markdown("""
    <style>
    .main { background-color: #f4f4f4; }
    .car-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .price-tag {
        color: #00a650; /* Verde Mercado Libre */
        font-size: 22px;
        font-weight: bold;
        margin: 5px 0px;
    }
    .car-name {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        height: 45px;
    }
    .btn-whatsapp {
        display: block;
        background-color: #3483fa; /* Azul Mercado Libre */
        color: white !important;
        padding: 10px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título de la Web
st.markdown("<h1 style='text-align: center; color: #333;'>🚗 Litoral Automotores</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Seleccioná el vehículo de tu interés</p>", unsafe_allow_html=True)
st.markdown("---")

# --- LÓGICA DE LA GRILLA (2 columnas para que se vea bien en móvil y PC) ---
col1, col2 = st.columns(2)

# --- AUTO 1: SMA C81 FULL ---
with col1:
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    # Foto principal del SMA (Asegúrate que este nombre sea uno de los tuyos)
    st.image("656153417_3758670710939148_5286495334834758579_n.jpg", use_container_width=True)
    st.markdown('<div class="car-name">SMA C81 Full 1.8 (2009)</div>', unsafe_allow_html=True)
    st.markdown('<div class="price-tag">U$S 3.500</div>', unsafe_allow_html=True)
    st.write("📍 Paysandú | 1.8 Nafta")
    
    link_sma = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20SMA%20C81%20de%203500"
    st.markdown(f'<a href="{link_sma}" target="_blank" class="btn-whatsapp">Ver Detalles / Contactar</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- AUTO 2: HYUNDAI ACCENT ---
with col2:
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    # Foto principal del Hyundai
    st.image("656679087_3758448937627992_433051286710756078_n.jpg", use_container_width=True)
    st.markdown('<div class="car-name">Hyundai Accent 1.5 (1995)</div>', unsafe_allow_html=True)
    st.markdown('<div class="price-tag">¡Consultar Precio!</div>', unsafe_allow_html=True)
    st.write("📍 Paysandú | Muy Económico")
    
    link_hyundai = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20Hyundai%20Accent%2095"
    st.markdown(f'<a href="{link_hyundai}" target="_blank" class="btn-whatsapp">Ver Detalles / Contactar</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: #999;'>© 2026 Litoral Automotores | Tel: 099 417 716</p>", unsafe_allow_html=True)
