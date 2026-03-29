import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Catálogo", page_icon="🚗", layout="wide")

# 2. CSS DE PRECISIÓN: Logo completo y sin espacios blancos
st.markdown("""
    <style>
    /* Eliminar márgenes de la aplicación */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 95% !important;
    }
    
    .stApp { background-color: #f8f9fa; }

    /* Encabezado Azul - Altura aumentada para que el logo respire */
    .header-container { 
        display: flex; 
        align-items: center; 
        background-color: #1d3557; 
        color: white; 
        padding: 40px 50px; 
        border-radius: 0px 0px 30px 30px;
        margin-top: -60px !important; /* Sube el bloque al tope del navegador */
        min-height: 280px; 
    }
    
    /* Logo: Tamaño controlado para que no se corte jamás */
    .header-logo { flex: 1; max-width: 220px; }
    .header-logo img { 
        width: 220px; 
        height: 220px;
        object-fit: cover;
        border-radius: 50%; 
        border: 4px solid #ffffff;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }
    
    .header-text { flex: 4; padding-left: 40px; }
    .header-text h1 { font-family: 'Arial Black'; font-size: 3.5em; margin: 0; color: white; line-height: 1; }
    .header-text p { font-size: 1.3em; color: #a8dadc; margin-top: 15px; line-height: 1.4; }

    /* Tarjetas de autos: Suben para eliminar el espacio blanco */
    .car-card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0px 8px 20px rgba(0,0,0,0.1); 
        text-align: center;
        margin-top: -40px !important; /* TRUCO: Sube las tarjetas sobre el azul */
        position: relative;
        z-index: 10;
        min-height: 750px;
    }
    
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.9em; }
    .price-tag { color: #e63946; font-size: 26px; font-weight: bold; margin: 15px 0px; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 14px; margin: 8px 0; border-radius: 10px; font-weight: bold; text-decoration: none; font-size: 1.1em; }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN ZOOM ---
if "foto" in st.query_params:
    if st.button("⬅️ VOLVER AL CATÁLOGO"):
        st.query_params.clear()
        st.rerun()
    st.image(st.query_params["foto"], use_container_width=True)
    st.stop()

# --- ENCABEZADO ---
logo_url = "https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg"
st.markdown(f"""
    <div class='header-container'>
        <div class='header-logo'><img src='{logo_url}'></div>
        <div class='header-text'>
            <h1>LITORAL AUTOMOTORES</h1>
            <p>Comercializamos vehículos de todas las décadas. Especialistas en gestionar <b>CONSIGNACIONES</b> con total transparencia y seguridad.</p>
            <p>Autos, Camionetas, Motos, Trailers y Casas Rodantes. ¡CONSÚLTENOS!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE FOTOS ---
archivos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])
f_saveiro = [f for f in archivos if 'savblack' in f.lower()]
f_vitara = [f for f in archivos if 'vitara' in f.lower()]
f_sma = [f for f in archivos if f.startswith('657') or f.startswith('655') or f.startswith('65615')]
f_hyundai = [f for f in archivos if f.startswith('656') and f not in f_sma]

def tarjeta(titulo, precio, desc, fotos, msg):
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    st.markdown(f"<span class='badge-venta'>EN VENTA!</span><br><b style='font-size:1.2em;'>{titulo}</b>", unsafe_allow_html=True)
    if fotos:
        st.image(fotos[0], use_container_width=True)
        if st.button(f"🔍 AMPLIAR FOTO", key=f"z_{fotos[0]}"):
            st.query_params.update(foto=fotos[0]); st.rerun()
    st.markdown(f'<div class="price-tag">{precio}</div>', unsafe_allow_html=True)
    for d in desc: st.write(f"• {d}")
    u = f"https://wa.me/59899417716?text={msg.replace(' ', '%20')}"
    st.markdown(f'<a href="{u}" target="_blank" class="btn-ws btn-info">💬 CONSULTAR</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{u}" target="_blank" class="btn-ws btn-interesa">🔥 LO QUIERO</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- GRILLA ---
col1, col2, col3, col4 = st.columns(4)
with col1: tarjeta("VW Saveiro C.E (2011)", "USD 8.000", ["Motor 1.6 Nafta", "230k km originales"], f_saveiro, "Saveiro")
with col2: tarjeta("Suzuki Vitara GL (2016)", "USD 14.800", ["150k km", "Servicio al día"], f_vitara, "Vitara")
with col3: tarjeta("SMA C81 Full (2009)", "USD 3.500", ["Motor 1.8 Nafta", "Versión Full"], f_sma, "SMA")
with col4: tarjeta("Hyundai Accent (1995)", "¡CONSULTE!", ["Motor 1.5", "Súper Económico"], f_hyundai, "Hyundai")

st.markdown("<p style='text-align: center; color: gray; font-size: 1em; margin-top: 50px;'>© 2026 Litoral Automotores | Paysandú, Uruguay</p>", unsafe_allow_html=True)
