import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Catálogo", page_icon="🚗", layout="wide")

# ESTILO CSS PARA ELIMINAR ESPACIOS BLANCOS
st.markdown("""
    <style>
    /* 1. Eliminar márgenes de Streamlit por defecto */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin-top: -30px !important;
    }
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* 2. Encabezado pegado arriba */
    .header-container { 
        display: flex; 
        align-items: center; 
        background-color: #1d3557; 
        color: white; 
        padding: 20px 30px; 
        border-radius: 0px 0px 15px 15px; 
        margin-bottom: 10px !important;
        margin-top: 0px !important;
    }
    .header-logo { flex: 1; max-width: 180px; }
    .header-logo img { width: 100%; border-radius: 50%; }
    .header-text { flex: 3; padding-left: 25px; }
    .header-text h1 { font-family: 'Arial Black'; color: white; font-size: 2.5em; margin: 0; }
    .header-text p { font-size: 1.1em; color: #a8dadc; margin: 0; line-height: 1.2; }

    /* 3. Tarjetas de autos pegadas al encabezado */
    .car-card { 
        background-color: white; 
        padding: 15px; 
        border-radius: 12px; 
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1); 
        text-align: center; 
        min-height: 700px;
        margin-top: 0px !important;
    }
    
    .badge-venta { background-color: #28a745; color: white; padding: 4px 12px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 5px; }
    .price-tag { color: #e63946; font-size: 22px; font-weight: bold; margin: 8px 0px; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 10px; margin: 5px 0; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 0.9em; }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN ZOOM ---
params = st.query_params
if "foto" in params:
    foto_grande = params["foto"]
    if st.button("⬅️ VOLVER AL CATÁLOGO"):
        st.query_params.clear()
        st.rerun()
    st.image(foto_grande, use_container_width=True)
    st.stop()

# --- ENCABEZADO ---
logo_url = "https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg"
st.markdown(f"""
    <div class='header-container'>
        <div class='header-logo'><img src='{logo_url}'></div>
        <div class='header-text'>
            <h1>LITORAL AUTOMOTORES</h1>
            <p>RECIBIMOS Y COMERCIALIZAMOS VEHÍCULOS. Expertos en <b>CONSIGNACIONES</b>.</p>
            <p>Autos, Camionetas, Motos, Trailers y Casas Rodantes. ¡CONSÚLTENOS!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- FILTRADO DE FOTOS ---
archivos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])
f_saveiro = [f for f in archivos if 'savblack' in f.lower()]
f_vitara = [f for f in archivos if 'vitara' in f.lower()]
f_sma = [f for f in archivos if f.startswith('657') or f.startswith('655') or f.startswith('65615')]
f_hyundai = [f for f in archivos if f.startswith('656') and f not in f_sma]

def mostrar_auto(titulo, precio, caracteristicas, fotos, msg):
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    st.markdown(f'<div style="font-weight: bold; margin-bottom: 10px;">{titulo}</div>', unsafe_allow_html=True)
    
    if fotos:
        if st.button(f"🔍 Ver Grande", key=f"main_{fotos[0]}"):
            st.query_params.update(foto=fotos[0]); st.rerun()
        st.image(fotos[0], use_container_width=True)
        mini = st.columns(3)
        for i, foto in enumerate(fotos[1:4]):
            with mini[i]:
                if st.button("🔍", key=f"z_{foto}"):
                    st.query_params.update(foto=foto); st.rerun()
                st.image(foto, use_container_width=True)

    st.markdown(f'<div class="price-tag">{precio}</div>', unsafe_allow_html=True)
    for c in caracteristicas: st.write(f"• {c}")
    
    url = f"https://wa.me/59899417716?text={msg.replace(' ', '%20')}"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-ws btn-info">💬 CONSULTAR</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url}" target="_blank" class="btn-ws btn-interesa">🔥 LO QUIERO</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- GRILLA SIN ESPACIOS ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    mostrar_auto("VW Saveiro C.E (2011)", "USD 8.000", ["Motor 1.6", "Protector de caja"], f_saveiro, "Interés Saveiro")
with col2:
    mostrar_auto("Suzuki Vitara GL (2016)", "USD 14.800", ["4 cubiertas nuevas", "Muy sana"], f_vitara, "Interés Vitara")
with col3:
    mostrar_auto("SMA C81 Full (2009)", "USD 3.500", ["Nafta Inyección", "Excelente estado"], f_sma, "Interés SMA")
with col4:
    mostrar_auto("Hyundai Accent (1995)", "¡CONSULTE!", ["Motor 1.5", "Documentación al día"], f_hyundai, "Interés Hyundai")

st.markdown("<p style='text-align: center; color: gray; margin-top: 20px;'>© 2026 Litoral Automotores | Paysandú</p>", unsafe_allow_html=True)
