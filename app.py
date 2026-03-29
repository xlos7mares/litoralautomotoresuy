import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Catálogo", page_icon="🚗", layout="wide")

# 2. CSS DE FUERZA BRUTA (Elimina todos los espacios)
st.markdown("""
    <style>
    /* Eliminar el padding superior de toda la página */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }
    
    /* Eliminar espacios que deja Streamlit entre elementos */
    [data-testid="stVerticalBlock"] {
        gap: 0rem !important;
    }

    /* Encabezado pegado al borde superior */
    .header-container { 
        display: flex; 
        align-items: center; 
        background-color: #1d3557; 
        color: white; 
        padding: 20px 30px; 
        border-radius: 0px 0px 15px 15px;
        margin-top: -50px !important; /* Sube el header al tope */
    }
    .header-logo { flex: 1; max-width: 150px; }
    .header-logo img { width: 100%; border-radius: 50%; }
    .header-text { flex: 3; padding-left: 20px; }
    .header-text h1 { font-family: 'Arial Black'; font-size: 2.2em; margin: 0; }
    .header-text p { font-size: 1em; color: #a8dadc; margin: 0; }

    /* Tarjetas de autos pegadas al header */
    .car-card { 
        background-color: white; 
        padding: 15px; 
        border-radius: 12px; 
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1); 
        text-align: center;
        margin-top: 10px !important;
    }
    
    .badge-venta { background-color: #28a745; color: white; padding: 3px 10px; border-radius: 20px; font-weight: bold; font-size: 0.8em; }
    .price-tag { color: #e63946; font-size: 20px; font-weight: bold; margin: 5px 0px; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 10px; margin: 4px 0; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 0.9em; }
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
            <p>Comercializamos vehículos de todas las décadas. Expertos en <b>CONSIGNACIONES</b>.</p>
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
    st.markdown(f"<span class='badge-venta'>EN VENTA!</span> <br> <b>{titulo}</b>", unsafe_allow_html=True)
    if fotos:
        st.image(fotos[0], use_container_width=True)
        # Botón de zoom simplificado para no ocupar espacio arriba
        if st.button(f"🔍 AMPLIAR", key=f"z_{fotos[0]}"):
            st.query_params.update(foto=fotos[0]); st.rerun()
    st.markdown(f'<div class="price-tag">{precio}</div>', unsafe_allow_html=True)
    for d in desc: st.write(f"• {d}")
    u = f"https://wa.me/59899417716?text={msg.replace(' ', '%20')}"
    st.markdown(f'<a href="{u}" target="_blank" class="btn-ws btn-info">💬 INFO</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{u}" target="_blank" class="btn-ws btn-interesa">🔥 INTERÉS</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- GRILLA ---
col1, col2, col3, col4 = st.columns(4)
with col1: tarjeta("VW Saveiro (2011)", "USD 8.000", ["Motor 1.6", "C. Extendida"], f_saveiro, "Saveiro")
with col2: tarjeta("Suzuki Vitara (2016)", "USD 14.800", ["150k km", "Servicio al día"], f_vitara, "Vitara")
with col3: tarjeta("SMA C81 (2009)", "USD 3.500", ["Nafta Iny.", "Full"], f_sma, "SMA")
with col4: tarjeta("Hyundai Accent (95)", "CONSULTE", ["Económico", "Al día"], f_hyundai, "Hyundai")

st.markdown("<p style='text-align: center; color: gray; font-size: 0.8em;'>© 2026 Litoral Automotores</p>", unsafe_allow_html=True)
