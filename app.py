import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Catálogo - Litoral Automotores", page_icon="🚗")

# Estilo personalizado CSS
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .car-title { text-align: center; color: #1d3557; font-family: 'Arial Black'; margin-top: 20px; }
    .feature-list { background-color: #f1f4f9; padding: 20px; border-radius: 15px; margin: 10px 0px; }
    .price-tag { color: #e63946; font-size: 26px; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .btn-whatsapp {
        display: block; width: 100%; text-align: center; background-color: #25d366;
        color: white !important; padding: 15px; margin: 10px 0; border-radius: 12px;
        font-weight: bold; font-size: 18px; text-decoration: none;
    }
    .btn-whatsapp:hover { background-color: #128c7e; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.markdown("<h1 class='car-title'>🚗 LITORAL AUTOMOTORES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Catálogo Digital de Vehículos - Paysandú</p>", unsafe_allow_html=True)

# Pestañas para los autos
tab1, tab2 = st.tabs(["⭐ SMA C81 Full (2009)", "🚘 HYUNDAI ACCENT (1995)"])

# --- SECCIÓN SMA C81 ---
with tab1:
    st.markdown("<h2 class='car-title'>SMA C81 Full 1.8</h2>", unsafe_allow_html=True)
    st.markdown("<p class='price-tag'>USD 3500.-</p>", unsafe_allow_html=True)

    # Buscamos las fotos que empiezan con '657' o '655' (las del SMA)
    fotos_sma = [f for f in os.listdir('.') if f.endswith('.jpg') and (f.startswith('657') or f.startswith('655'))]
    
    if fotos_sma:
        cols = st.columns(2)
        for i, foto in enumerate(fotos_sma):
            with cols[i % 2]:
                st.image(foto, use_container_width=True)
    
    st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
    st.write("✅ **Marca:** SMA")
    st.write("✅ **Modelo:** C81 Full (Sedán muy cómodo)")
    st.write("✅ **Año:** 2009")
    st.write("✅ **Motor:** 1.8 Nafta Inyección")
    st.write("✅ **Estado:** Versión full, muy bien cuidado y espacioso.")
    st.write("📍 **Ubicación:** Paysandú, Uruguay.")
    st.markdown("</div>", unsafe_allow_html=True)

    link_sma = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20SMA%20C81%20Full%20de%20USD%203500"
    st.markdown(f'<a href="{link_sma}" target="_blank" class="btn-whatsapp">💬 CONSULTAR POR EL SMA</a>', unsafe_allow_html=True)

# --- SECCIÓN HYUNDAI ---
with tab2:
    st.markdown("<h2 class='car-title'>HYUNDAI ACCENT 1.5</h2>", unsafe_allow_html=True)
    st.markdown("<p class='price-tag'>¡SUPER ECONÓMICO!</p>", unsafe_allow_html=True)

    # Buscamos las fotos que NO son del SMA (las originales del Hyundai)
    fotos_hyundai = [f for f in os.listdir('.') if f.endswith('.jpg') and f.startswith('656')]
    
    if fotos_hyundai:
        cols = st.columns(2)
        for i, foto in enumerate(fotos_hyundai):
            with cols[i % 2]:
                st.image(foto, use_container_width=True)
    
    st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
    st.write("✅ **Marca:** Hyundai")
    st.write("✅ **Modelo:** Accent")
    st.write("✅ **Año:** 1995")
    st.write("✅ **Motor:** 1.5 Nafta")
    st.write("✅ **Documentos:** Títulos y libreta en regla.")
    st.markdown("</div>", unsafe_allow_html=True)

    link_hyundai = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20Hyundai%20Accent%2095"
    st.markdown(f'<a href="{link_hyundai}" target="_blank" class="btn-whatsapp">💬 CONSULTAR POR EL HYUNDAI</a>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center;'>📞 Contacto Directo: <b>099 417 716</b></p>", unsafe_allow_html=True)
