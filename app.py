import streamlit as st
import os

# Configuración de la página (Título y icono)
st.set_page_config(page_title="Litoral Automotores - Paysandú", page_icon="🚗", layout="wide")

# Estilo personalizado con CSS profesional
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-container { display: flex; align-items: center; justify-content: center; padding: 20px; background-color: #1d3557; color: white; border-radius: 12px; margin-bottom: 30px; }
    .header-logo { width: 150px; margin-right: 30px; }
    .header-text { text-align: left; max-width: 600px; }
    .header-text h1 { font-family: 'Arial Black'; margin-bottom: 5px; color: white; }
    .header-text p { font-size: 1.1em; color: #a8dadc; margin-bottom: 0; }
    .car-card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.9em; display: inline-block; margin-bottom: 10px; }
    .car-title { font-size: 1.3em; font-weight: bold; color: #333; height: 50px; overflow: hidden; margin-bottom: 10px; }
    .price-tag { color: #e63946; font-size: 24px; font-weight: bold; margin: 10px 0px; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 15px; margin: 10px 0; border-radius: 8px; font-weight: bold; font-size: 1.1em; text-decoration: none; }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    .btn-ws:hover { text-decoration: none; color: white !important; opacity: 0.9; }
    .footer { text-align: center; color: gray; margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Principal con Logo y Descripción
st.markdown(f"""
    <div class='header-container'>
        <img src='https://raw.githubusercontent.com/LitoralAutomotoresPaysandu/Litoral/main/Litoral%20Uruguay%20Logo.png' class='header-logo' alt='Litoral Automotores Logo'>
        <div class='header-text'>
            <h1>LITORAL AUTOMOTORES</h1>
            <p>RECIBIMOS Y COMERCIALIZAMOS TODO TIPO DE VEHÍCULOS DE TODAS LAS DÉCADAS. Especialistas en gestionar CONSIGNACIONES con total transparencia y seguridad. Autos, Camionetas, Motos (Cross, Carrera, Pollerita), Trailers y Casas Rodantes de Todas las Décadas. ¡CONSÚLTENOS!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Obtener TODAS las fotos .jpg del repositorio
fotos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])

col1, col2 = st.columns(2)

# --- AUTO 1: SMA C81 (FOTOS NUEVAS: Empiezan con 657 y 655) ---
with col1:
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    
    # Buscamos las fotos que empiezan con '657' o '655' (las del SMA)
    fotos_sma = [f for f in fotos if f.startswith('657') or f.startswith('655')]
    
    if fotos_sma:
        st.image(fotos_sma[0], use_container_width=True) # Principal Pizarrón/Blanco
        # Sub-galería si hay más fotos
        if len(fotos_sma) > 1:
            mini_cols_sma = st.columns(4)
            for i, foto in enumerate(fotos_sma[1:5]):
                with mini_cols_sma[i]:
                    st.image(foto, use_container_width=True)
    
    st.markdown('<div class="car-name">SMA C81 Full 1.8 (2009)</div>', unsafe_allow_html=True)
    st.markdown('<div class="price-tag">PRECIO USD 3500.-</div>', unsafe_allow_html=True)
    st.write("✅ Versión Full equipada")
    st.write("✅ Motor 1.8 Nafta Inyección (Potente)")
    st.write("✅ Espacioso y muy bien cuidado")
    
    url_sma = "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20SMA%20C81%20de%203500"
    st.markdown(f'<a href="{url_sma}" target="_blank" class="btn-ws btn-info">💬 SOLICITAR MÁS INFO</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url_sma}" target="_blank" class="btn-ws btn-interesa">🔥 ¡ME INTERESA!</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- AUTO 2: HYUNDAI ACCENT (FOTOS ORIGINALES: Empiezan con 656) ---
with col2:
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    
    # Buscamos las fotos que empiezan con '656' (las originales del Hyundai)
    fotos_hyundai = [f for f in fotos if f.startswith('656')]
    
    if fotos_hyundai:
        st.image(fotos_hyundai[0], use_container_width=True) # Principal Roja
        # Sub-galería si hay más fotos
        if len(fotos_hyundai) > 1:
            mini_cols_hyundai = st.columns(4)
            for i, foto in enumerate(fotos_hyundai[1:5]):
                with mini_cols_hyundai[i]:
                    st.image(foto, use_container_width=True)
    
    st.markdown('<div class="car-name">HYUNDAI ACCENT 1.5 (1995)</div>', unsafe_allow_html=True)
    st.write("✅ ¡Muy Económico!")
    st.write("✅ Motor 1.5 Nafta")
    st.write("✅ Títulos y libreta al día")
    st.write("📍 Paysandú")
    
    url_hyundai = "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20Hyundai%20Accent"
    st.markdown(f'<a href="{url_hyundai}" target="_blank" class="btn-ws btn-info">💬 SOLICITAR MÁS INFO</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url_hyundai}" target="_blank" class="btn-ws btn-interesa">🔥 ¡ME INTERESA!</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Litoral Automotores - Calidad y Confianza</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>📞 Contacto: 099 417 716</p>", unsafe_allow_html=True)
