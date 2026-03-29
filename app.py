import streamlit as st

# Configuración de la página para que se vea bien en celulares
st.set_page_config(page_title="Venta Hyundai Accent 95 - Litoral Automotores", page_icon="🚗")

# Estilo personalizado con CSS (Colores y Botones)
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #e63946;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        background-color: #ba2d3a;
        color: white;
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
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.markdown("<h1 class='car-title'>🚗 HYUNDAI ACCENT 1995</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em; color: gray;'>¡Oportunidad Única - Litoral Automotores!</p>", unsafe_allow_html=True)

# Galería de Imágenes con los nombres EXACTOS de tus archivos en GitHub
col1, col2 = st.columns(2)

with col1:
    st.image("656018921_3758448887627997_8510609175985780951_n.jpg", caption="Vista Lateral")
    st.image("656778717_3758448807628005_2040901742418574192_n.jpg", caption="Vista Trasera")

with col2:
    st.image("656916897_3758448750961344_3819844090740414086_n.jpg", caption="Detalle Trasero")
    st.image("656679087_3758448937627992_433051286710756078_n.jpg", caption="Vista Frontal")

# Sección de características
st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
st.subheader("Características del Vehículo")
st.write("✅ **Motor:** 1.5 Nafta")
st.write("✅ **Consumo:** ¡Muy económico, ideal para uso diario!")
st.write("✅ **Documentación:** Títulos y libreta en regla.")
st.write("📍 **Ubicación:** Paysandú, Uruguay.")
st.markdown("</div>", unsafe_allow_html=True)

# Enlace de WhatsApp con mensaje automático
whatsapp_link = "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20Hyundai%20Accent%2095"

# Botones de Acción
st.markdown("---")
if st.button("💬 SOLICITAR MÁS INFO"):
    st.markdown(f'<meta http-equiv="refresh" content="0;URL={whatsapp_link}">', unsafe_allow_html=True)

if st.button("🔥 ¡ME INTERESA EL AUTO!"):
    st.markdown(f'<meta http-equiv="refresh" content="0;URL={whatsapp_link}">', unsafe_allow_html=True)

# Pie de página profesional
st.markdown("---")
st.markdown("<p style='text-align: center; color: #777;'>© 2026 Litoral Automotores - Paysandú</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>📞 Contacto: 099 417 716</p>", unsafe_allow_html=True)
