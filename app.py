import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Catálogo - Litoral Automotores", page_icon="🚗", layout="wide")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header { text-align: center; margin-bottom: 20px; }
    .header h1 { font-family: 'Arial Black'; color: #1d3557; }
    .header p { color: gray; font-size: 1.1em; }
    .car-card {
        background-color: white; padding: 15px; border-radius: 12px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center;
    }
    .price-tag { color: #e63946; font-size: 24px; font-weight: bold; margin-bottom: 10px; }
    .btn-whatsapp {
        display: block; background-color: #3483fa; color: white !important;
        padding: 12px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 10px;
    }
    .btn-whatsapp:hover { background-color: #25d366; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Principal con Logo Grande
st.markdown("<div class='header'><h1>Litoral Automotores</h1><p>Su destino para vehículos de todas las décadas y tipos: Autos, Camionetas, Motos Cross, Motos de Carrera, Motos Pollerita, Trailers, Casas Rodantes, ¡y más!</p></div>", unsafe_allow_html=True)
st.markdown("---")

# --- LISTA DE VEHÍCULOS (Aquí agregas o quitas fácil) ---
# El 'foto_id' es una parte del nombre del archivo que sea única
vehiculos = [
    {
        "nombre": "SMA C81 Full 1.8 (2009)",
        "precio": "U$S 3.500",
        "info": "📍 Paysandú | Nafta Inyección",
        "foto_id": "656153417", # Los primeros números de la foto del SMA
        "msj": "Hola Leo, me interesa el SMA C81 de 3500"
    },
    {
        "nombre": "Hyundai Accent 1.5 (1995)",
        "precio": "¡Muy Económico!",
        "info": "📍 Paysandú | Documentación al día",
        "foto_id": "656679087", # Los primeros números de la foto del Hyundai
        "msj": "Hola Leo, me interesa el Hyundai Accent 95"
    }
]

# --- LÓGICA DE GRILLA AUTOMÁTICA ---
todos_los_archivos = os.listdir('.')
cols = st.columns(2)

for i, v in enumerate(vehiculos):
    with cols[i % 2]:
        st.markdown('<div class="car-card">', unsafe_allow_html=True)
        
        # BUSCADOR DE FOTO: Busca el archivo que empiece con el foto_id
        foto_encontrada = next((f for f in todos_los_archivos if f.startswith(v["foto_id"]) and f.lower().endswith('.jpg')), None)
        
        if foto_encontrada:
            st.image(foto_encontrada, use_container_width=True)
        else:
            st.warning(f"No se halló foto para {v['nombre']}")
            
        st.markdown(f'<div class="car-name">{v["nombre"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="price-tag">{v["precio"]}</div>', unsafe_allow_html=True)
        st.write(v["info"])
        
        url = f"https://wa.me/59899417716?text={v['msj'].replace(' ', '%20')}"
        st.markdown(f'<a href="{url}" target="_blank" class="btn-whatsapp">Ver / Contactar</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: #999;'>© 2026 Litoral Automotores | Tel: 099 417 716</p>", unsafe_allow_html=True)
