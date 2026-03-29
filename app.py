import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Venta Hyundai Accent 95 - Litoral Automotores", page_icon="🚗")

# Estilo personalizado con CSS (Botones de WhatsApp Reales)
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .car-title {
        text-align: center;
        color: #1d3557;
        font-family: 'Arial Black';
        margin-bottom: 0px;
    }
    .feature-list {
        background-color: #f1f4f9;
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0px;
    }
    /* Estilo para los botones de enlace */
    .btn-whatsapp {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #e63946;
        color: white !important;
        padding: 15px;
        margin: 10px 0;
        border-radius: 12px;
        font-weight: bold;
        font-size: 18px;
        text-decoration: none;
    }
    .btn-whatsapp:hover {
        background-color: #ba2d3a;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.markdown("<h1 class='car-title'>🚗 HYUNDAI ACCENT 1995</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em; color: gray;'>¡Oportunidad Única - Litoral Automotores!</p>", unsafe_allow_html=True)

# Galería de Imágenes
col1, col2 = st.columns(2)

with col1:
    st.image("656018921_3758448887627997_8510609175985780951_n.jpg", caption="Vista Lateral")
    st.image("656778717_375844807628005_2040901742418574192_n.jpg", caption="Vista Trasera")

with col2:
    st.image("656916897_3758448750961344_3819844090740414086_n.jpg", caption="Detalle Trasero")
    st.image("656679087_3758448937627992_433051286710756078_n.jpg", caption="Vista Frontal")

# Características
st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
st.subheader("Características del Vehículo")
st.write("✅ **Motor:** 1.5 Nafta")
st.write("✅ **Consumo:** ¡Muy económico, ideal para uso diario!")
st.write("✅ **Documentación:** Títulos y libreta en regla.")
st.write("📍 **Ubicación:** Paysandú, Uruguay.")
st.markdown("</div>", unsafe_allow_html=True)

# Link de WhatsApp directo a tu número
whatsapp_url = "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20Hyundai%20Accent%2095"

# Botones de Acción (Usando HTML para que el link no falle)
st.markdown("---")
st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="btn-whatsapp">💬 SOLICITAR MÁS INFO</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="btn-whatsapp">🔥 ¡ME INTERESA EL AUTO!</a>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: #777;'>© 2026 Litoral Automotores - Paysandú</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>📞 Contacto: 099 417 716</p>", unsafe_allow_html=True)
