import streamlit as st
import os

# Configuración de la página (Título y icono)
st.set_page_config(page_title="Litoral Automotores - Catálogo", page_icon="🚗", layout="wide")

# Estilo personalizado con CSS para botones y tarjetas
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .car-title { text-align: center; color: #1d3557; font-family: 'Arial Black'; margin-top: 15px; }
    .feature-list { background-color: #f1f4f9; padding: 20px; border-radius: 15px; margin: 15px 0px; }
    .price-tag { color: #e63946; font-size: 26px; font-weight: bold; text-align: center; margin-bottom: 10px; }
    /* Estilo para los botones de enlace de WhatsApp */
    .btn-whatsapp {
        display: block; width: 100%; text-align: center; background-color: #25d366;
        color: white !important; padding: 15px; margin: 10px 0; border-radius: 12px;
        font-weight: bold; font-size: 18px; text-decoration: none;
    }
    .btn-whatsapp:hover { background-color: #128c7e; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Principal
st.markdown("<h1 class='car-title'>🚗 LITORAL AUTOMOTORES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Catálogo Digital de Vehículos - Paysandú</p>", unsafe_allow_html=True)

# Definimos las pestañas para cada auto
tab1, tab2 = st.tabs(["⭐ SMA C81 Full (2009)", "🚘 HYUNDAI ACCENT (1995)"])

# ---------------------------------------------------------
# PESTAÑA 1: SMA C81 Full
# ---------------------------------------------------------
with tab1:
    st.markdown("<h2 class='car-title'>SMA C81 Full 1.8</h2>", unsafe_allow_html=True)
    st.markdown("<p class='price-tag'>Precio: USD 3500.-</p>", unsafe_allow_html=True)

    # Buscamos las fotos específicas del SMA (empiezan con '65' o '655')
    fotos_sma = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg') and (f.startswith('657') or f.startswith('655'))])
    
    if fotos_sma:
        # Mostramos las fotos en una cuadrícula de 2 columnas
        cols_sma = st.columns(2)
        for i, foto in enumerate(fotos_sma):
            with cols_sma[i % 2]:
                st.image(foto, caption=f"SMA - Vista {i+1}", use_container_width=True)
    else:
        st.warning("No se encontraron fotos del SMA en la carpeta del proyecto.")

    # Características SMA
    st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
    st.subheader("Características del Vehículo")
    st.write("✅ **Marca:** SMA")
    st.write("✅ **Modelo:** C81 Full (Sedán Cómodo y Espacioso)")
    st.write("✅ **Año:** 2009")
    st.write("✅ **Motor:** 1.8 Nafta Inyección (Potente)")
    st.write("✅ **Estado:** Versión full, muy bien cuidado y espacioso.")
    st.write("✅ **Precio:** **USD 3500.-**")
    st.write("📍 **Ubicación:** Paysandú, Uruguay.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Link de WhatsApp específico para el SMA
    whatsapp_sma = "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20SMA%20C81%20Full%202009%20de%20USD%203500"

    # Botones SMA Reales (HTML)
    st.markdown("---")
    st.markdown(f'<a href="{whatsapp_sma}" target="_blank" class="btn-whatsapp">💬 SOLICITAR MÁS INFO (SMA)</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{whatsapp_sma}" target="_blank" class="btn-whatsapp">🔥 ¡ME INTERESA EL SMA!</a>', unsafe_allow_html=True)


# ---------------------------------------------------------
# PESTAÑA 2: HYUNDAI ACCENT (Original)
# ---------------------------------------------------------
with tab2:
    st.markdown("<h2 class='car-title'>HYUNDAI ACCENT 1.5</h2>", unsafe_allow_html=True)
    st.markdown("<p class='price-tag'>¡MÁXIMA ECONOMÍA!</p>", unsafe_allow_html=True)

    # Buscamos las fotos que NO son del SMA (las originales del Hyundai, empiezan con '656')
    fotos_hyundai = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg') and f.startswith('656')])
    
    if fotos_hyundai:
        cols_h = st.columns(2)
        for i, foto in enumerate(fotos_hyundai):
            with cols_h[i % 2]:
                st.image(foto, caption=f"Hyundai - Vista {i+1}", use_container_width=True)
    else:
        st.warning("No se encontraron fotos del Hyundai en la carpeta del proyecto.")

    # Características Hyundai
    st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
    st.subheader("Características del Vehículo")
    st.write("✅ **Marca:** Hyundai")
    st.write("✅ **Modelo:** Accent")
    st.write("✅ **Año:** 1995")
    st.write("✅ **Motor:** 1.5 Nafta (¡Muy económico!)")
    st.write("✅ **Documentación:** Títulos y libreta en regla.")
    st.write("📍 **Ubicación:** Paysandú, Uruguay.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Link de WhatsApp específico para el Hyundai
    whatsapp_hyundai = "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20Hyundai%20Accent%2095"

    # Botones Hyundai Reales (HTML)
    st.markdown("---")
    st.markdown(f'<a href="{whatsapp_hyundai}" target="_blank" class="btn-whatsapp">💬 SOLICITAR MÁS INFO (Hyundai)</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{whatsapp_hyundai}" target="_blank" class="btn-whatsapp">🔥 ¡ME INTERESA EL HYUNDAI!</a>', unsafe_allow_html=True)

# Pie de página unificado
st.markdown("---")
st.markdown("<p style='text-align: center; color: #777;'>© 2026 Litoral Automotores | Tel: 099 417 716</p>", unsafe_allow_html=True)
