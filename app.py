import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Venta Hyundai Accent 95 - Litoral Automotores", page_icon="🚗")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .car-title { text-align: center; color: #1d3557; font-family: 'Arial Black'; margin-bottom: 0px; }
    .feature-list { background-color: #f1f4f9; padding: 20px; border-radius: 15px; margin: 10px 0px; }
    .btn-whatsapp {
        display: block; width: 100%; text-align: center; background-color: #e63946;
        color: white !important; padding: 15px; margin: 10px 0; border-radius: 12px;
        font-weight: bold; font-size: 18px; text-decoration: none;
    }
    .btn-whatsapp:hover { background-color: #ba2d3a; }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.markdown("<h1 class='car-title'>🚗 HYUNDAI ACCENT 1995</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em; color: gray;'>¡Oportunidad Única - Litoral Automotores!</p>", unsafe_allow_html=True)

# BUSCADOR AUTOMÁTICO DE FOTOS
# Esto evita errores de escritura: busca todos los archivos .jpg en tu repo
fotos = [f for f in os.listdir('.') if f.endswith('.jpg')]

if fotos:
    # Mostramos las fotos en una cuadrícula
    cols = st.columns(2)
    for i, foto in enumerate(fotos):
        with cols[i % 2]:
            st.image(foto, use_container_width=True)
else:
    st.warning("No se encontraron fotos en la carpeta del proyecto.")

# Características
st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
st.subheader("Características del Vehículo")
st.write("✅ **Motor:** 1.5 Nafta")
st.write("✅ **Consumo:** ¡Muy económico, ideal para uso diario!")
st.write("✅ **Documentación:** Títulos y libreta en regla.")
st.write("📍 **Ubicación:** Paysandú, Uruguay.")
st.markdown("</div>", unsafe_allow_html=True)

# Link de WhatsApp directo
whatsapp_url = "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20Hyundai%20Accent%2095"

# Botones de Acción
st.markdown("---")
st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="btn-whatsapp">💬 SOLICITAR MÁS INFO</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="btn-whatsapp">🔥 ¡ME INTERESA EL AUTO!</a>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: #777;'>© 2026 Litoral Automotores - Paysandú</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>📞 Contacto: 099 417 716</p>", unsafe_allow_html=True)
