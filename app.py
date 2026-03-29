import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Venta Hyundai Accent 95 - Litoral Automotores", page_icon="🚗")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #e63946;
        color: white;
        font-weight: bold;
        font-size: 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ba2d3a;
        color: white;
    }
    .price-tag {
        font-size: 30px;
        color: #1d3557;
        font-weight: bold;
        text-align: center;
    }
    .car-title {
        text-align: center;
        color: #1d3557;
        font-family: 'Arial Black';
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.markdown("<h1 class='car-title'>🚗 HYUNDAI ACCENT 1995</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>¡Oportunidad Única - Litoral Automotores!</p>", unsafe_allow_html=True)

# Galería de Imágenes (Ajusta los nombres a tus archivos reales)
# Aquí usamos columnas para mostrar las fotos que subiste
col1, col2 = st.columns(2)
with col1:
    st.image("auto1.jpg", caption="Vista Lateral") # Cambia por tu nombre de archivo
    st.image("auto2.jpg", caption="Vista Trasera")
with col2:
    st.image("auto3.jpg", caption="Detalle Trasero")
    st.image("auto4.jpg", caption="Vista Frontal")

# Detalles del Vehículo
st.markdown("---")
st.subheader("Características Destacadas")
col_a, col_b = st.columns(2)

with col_a:
    st.write("✅ **Motor:** 1.5 Nafta")
    st.write("✅ **Consumo:** ¡Muy económico!")
    st.write("✅ **Documentación:** Títulos y libreta al día.")

with col_b:
    st.write("📍 **Ubicación:** Paysandú, Uruguay")
    st.write("🛡️ **Estado:** Listo para transferir")

# Botones de Acción
st.markdown("---")
whatsapp_link = "https://wa.me/59899417716?text=Hola,%20estoy%20interesado%20en%20el%20Hyundai%20Accent%2095"

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("💬 SOLICITAR MÁS INFO"):
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={whatsapp_link}">', unsafe_allow_html=True)

with col_btn2:
    if st.button("🔥 ¡ME INTERESA!"):
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={whatsapp_link}">', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Litoral Automotores - Calidad y Confianza</p>", unsafe_allow_html=True)
