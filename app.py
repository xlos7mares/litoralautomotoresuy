import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Paysandú", page_icon="🚗", layout="wide")

# Estilo CSS (Se mantiene igual a como te gustó)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-container { display: flex; align-items: center; background-color: #1d3557; color: white; padding: 30px; border-radius: 15px; margin-bottom: 30px; }
    .header-logo { flex: 1; max-width: 250px; }
    .header-logo img { width: 100%; border-radius: 50%; }
    .header-text { flex: 3; padding-left: 30px; }
    .header-text h1 { font-family: 'Arial Black'; color: white; font-size: 3em; margin-bottom: 10px; }
    .header-text p { font-size: 1.2em; color: #a8dadc; line-height: 1.4; }
    .car-card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 10px; }
    .price-tag { color: #e63946; font-size: 24px; font-weight: bold; margin: 10px 0px; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 15px; margin: 10px 0; border-radius: 8px; font-weight: bold; text-decoration: none; }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado (Logo redondo y descripción)
logo_url = "https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg"
st.markdown(f"""
    <div class='header-container'>
        <div class='header-logo'><img src='{logo_url}'></div>
        <div class='header-text'>
            <h1>LITORAL AUTOMOTORES</h1>
            <p>RECIBIMOS Y COMERCIALIZAMOS TODO TIPO DE VEHÍCULOS DE TODAS LAS DÉCADAS. Especialistas en gestionar <b>CONSIGNACIONES</b> con total transparencia y seguridad. Autos, Camionetas, Motos (Cross, Carrera, Pollerita), Trailers y Casas Rodantes de Todas las Décadas. ¡CONSÚLTENOS!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE FILTRADO DE FOTOS ---
archivos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])

# Identificamos las fotos del SMA (Las que empiezan con 657, 655 y la específica 65615 que es del SMA blanco)
fotos_sma = [f for f in archivos if f.startswith('657') or f.startswith('655') or f.startswith('65615')]

# Identificamos las fotos del Hyundai (Todas las demás que empiezan con 656 pero que NO están en la lista del SMA)
fotos_hyundai = [f for f in archivos if f.startswith('656') and f not in fotos_sma]

col1, col2 = st.columns(2)

# --- COLUMNA 1: SMA ---
with col1:
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    if fotos_sma:
        st.image(fotos_sma[0], use_container_width=True)
        mini_s = st.columns(4)
        for i, foto in enumerate(fotos_sma[1:5]):
            with mini_s[i]: st.image(foto, use_container_width=True)
    st.markdown('<h3>SMA C81 Full 1.8 (2009)</h3>', unsafe_allow_html=True)
    st.markdown('<div class="price-tag">USD 3500.-</div>', unsafe_allow_html=True)
    st.write("✅ 1.8 Nafta Inyección | Versión Full")
    url_s = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20SMA%20C81"
    st.markdown(f'<a href="{url_s}" target="_blank" class="btn-ws btn-info">💬 INFO</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url_s}" target="_blank" class="btn-ws btn-interesa">🔥 ME INTERESA</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLUMNA 2: HYUNDAI (CORREGIDA) ---
with col2:
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    if fotos_hyundai:
        st.image(fotos_hyundai[0], use_container_width=True)
        mini_h = st.columns(4)
        for i, foto in enumerate(fotos_hyundai[1:5]):
            with mini_h[i]: st.image(foto, use_container_width=True)
    st.markdown('<h3>HYUNDAI ACCENT 1.5 (1995)</h3>', unsafe_allow_html=True)
    st.markdown('<div class="price-tag">¡SÚPER ECONÓMICO!</div>', unsafe_allow_html=True)
    st.write("✅ 1.5 Nafta | Documentación al día")
    url_h = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20Hyundai%20Accent"
    st.markdown(f'<a href="{url_h}" target="_blank" class="btn-ws btn-info">💬 INFO</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url_h}" target="_blank" class="btn-ws btn-interesa">🔥 ME INTERESA</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;'>© 2026 Litoral Automotores | 099 417 716</p>", unsafe_allow_html=True)
