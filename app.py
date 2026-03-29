import streamlit as st
import os

# Configuración de la página (Título y icono en el navegador)
st.set_page_config(page_title="Catálogo - Litoral Automotores", page_icon="🚗")

# Estilo personalizado con CSS para botones profesionales
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .car-title { text-align: center; color: #1d3557; font-family: 'Arial Black'; margin-bottom: 0px; }
    .feature-list { background-color: #f1f4f9; padding: 20px; border-radius: 15px; margin: 10px 0px; }
    .price-tag { color: #e63946; font-size: 24px; font-weight: bold; text-align: center; }
    .btn-whatsapp {
        display: block; width: 100%; text-align: center; background-color: #e63946;
        color: white !important; padding: 15px; margin: 10px 0; border-radius: 12px;
        font-weight: bold; font-size: 18px; text-decoration: none;
    }
    .btn-whatsapp:hover { background-color: #ba2d3a; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Principal
st.markdown("<h1 class='car-title'>🚗 NUESTROS VEHÍCULOS DISPONIBLES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Litoral Automotores - Paysandú, Uruguay</p>", unsafe_allow_html=True)

# Definimos las pestañas para cada auto
tab1, tab2 = st.tabs(["🚗 SMA C81 Full (2009)", "🚗 HYUNDAI ACCENT (1995)"])

# ---------------------------------------------------------
# PESTAÑA 1: SMA C81 Full
# ---------------------------------------------------------
with tab1:
    st.markdown("<h2 class='car-title'>SMA C81 Full 1.8 (2009)</h2>", unsafe_allow_html=True)
    st.markdown("<p class='price-tag'>¡Oportunidad! Precio USD 3500.-</p>", unsafe_allow_html=True)

    # Buscamos las fotos específicas del SMA. Asegúrate de tenerlas en GitHub.
    # Aquí busco archivos que empiecen con '65' que es el prefijo de tus fotos nuevas.
    fotos_sma = [f for f in os.listdir('.') if f.endswith('.jpg') and f.startswith('65')]
    
    if fotos_sma:
        cols = st.columns(2)
        for i, foto in enumerate(fotos_sma):
            with cols[i % 2]:
                # Mostramos las fotos en una cuadrícula. Puedes ajustar caption si quieres
                st.image(foto, caption=f"SMA - Vista {i+1}", use_container_width=True)
    else:
        st.warning("No se encontraron fotos del SMA en la carpeta del proyecto.")

    # Características SMA
    st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
    st.subheader("Características del Vehículo")
    st.write("**Descripción:** Excelente oportunidad! Un sedán cómodo, espacioso y listo para rodar. Ideal para quienes buscan un vehículo confiable con un motor potente.")
    st.write("✅ **Marca:** SMA")
    st.write("✅ **Modelo:** C81 Full")
    st.write("✅ **Año:** 2009")
    st.write("✅
