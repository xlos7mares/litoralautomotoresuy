import streamlit as st
import os

# 1. Configuración de la página (Ancho completo para estilo catálogo)
st.set_page_config(page_title="Litoral Automotores - Clasificados", page_icon="🚗", layout="wide")

# 2. Estilo CSS para imitar el diseño de la imagen
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .header-container { text-align: center; padding: 20px; background-color: white; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); }
    .car-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); margin-bottom: 30px; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.9em; display: inline-block; }
    .price-tag { background-color: #e9ecef; color: #1d3557; padding: 5px 15px; border-radius: 5px; font-weight: bold; font-size: 1.2em; display: inline-block; margin-top: 10px; }
    .feature-list { margin-top: 15px; font-size: 0.95em; line-height: 1.6; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 12px; margin: 8px 0; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 1.1em; }
    .btn-info { background-color: #dc3545; }
    .btn-interesa { background-color: #c82333; }
    .footer { text-align: center; padding: 20px; background-color: #1d3557; color: white; margin-top: 50px; border-radius: 10px 10px 0 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado con Logo y Descripción
st.markdown("""
    <div class='header-container'>
        <h1 style='color: #1d3557; margin-bottom: 0;'>Litoral Automotores</h1>
        <p style='color: #457b9d; font-weight: bold;'>Calidad y Confianza en Paysandú</p>
        <p style='font-size: 0.9em; color: #666;'>Autos, Camionetas, Motos (Cross, Carrera, Pollerita), Trailers y Casas Rodantes.</p>
        <h2 style='color: #1d3557; border-top: 2px solid #eee; padding-top: 10px;'>🚗 NUESTROS VEHÍCULOS DISPONIBLES</h2>
    </div>
    """, unsafe_allow_html=True)

# 4. Lógica de separación de fotos (Basado en tus archivos reales de GitHub)
todos_los_archivos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])
# Fotos SMA: Empiezan con 657 o 655
fotos_sma = [f for f in todos_los_archivos if f.startswith('657') or f.startswith('655')]
# Fotos Hyundai: Empiezan con 656 o el resto de 65
fotos_hyundai = [f for f in todos_los_archivos if f.startswith('656') or (f.startswith('65') and f not in fotos_sma)]

# 5. Renderizado del Catálogo
col_izq, col_der = st.columns(2)

# --- COLUMNA IZQUIERDA: HYUNDAI ACCENT ---
with col_izq:
    st.markdown("<div class='car-card'>", unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom:0;'>🚗 HYUNDAI ACCENT 1.5 (1995)</h3>", unsafe_allow_html=True)
    
    if fotos_hyundai:
        st.image(fotos_hyundai[0], use_container_width=True) # Foto Principal
        # Galería de miniaturas debajo
        if len(fotos_hyundai) > 1:
            mini_cols = st.columns(4)
            for i, foto in enumerate(fotos_hyundai[1:5]): # Muestra hasta 4 miniaturas
                with mini_cols[i]:
                    st.image(foto, use_container_width=True)
    
    st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
    st.write("✅ **Motor:** 1.5 Nafta (Muy Económico)")
    st.write("✅ **Estado:** Listo para rodar, documentación al día.")
    st.write("📍 **Ubicación:** Paysandú, Uruguay.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    ws_h = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20Hyundai%20Accent"
    st.markdown(f"<a href='{ws_h}' class='btn-ws btn-info'>💬 SOLICITAR MÁS INFO</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{ws_h}' class='btn-ws btn-interesa'>🔥 ¡ME INTERESA!</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- COLUMNA DERECHA: SMA C81 ---
with col_der:
    st.markdown("<div class='car-card'>", unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom:0;'>🚗 SMA C81 FULL 1.8 (2009)</h3>", unsafe_allow_html=True)
    st.markdown("<div class='price-tag'>PRECIO USD 3500</div>", unsafe_allow_html=True)
    
    if fotos_sma:
        st.image(fotos_sma[0], use_container_width=True) # Foto Principal
        # Galería de miniaturas debajo
        if len(fotos_sma) > 1:
            mini_cols_s = st.columns(4)
            for i, foto in enumerate(fotos_sma[1:5]):
                with mini_cols_s[i]:
                    st.image(foto, use_container_width=True)

    st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
    st.write("✅ **Motor:** 1.8 Nafta Inyección")
    st.write("✅ **Equipamiento:** Versión Full, espacioso y cómodo.")
    st.write("✅ **Estado:** Muy bien cuidado.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    ws_s = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20SMA%20C81"
    st.markdown(f"<a href='{ws_s}' class='btn-ws btn-info'>💬 SOLICITAR MÁS INFO</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{ws_s}' class='btn-ws btn-interesa'>🔥 ¡ME INTERESA!</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 6. Pie de página
st.markdown(f"""
    <div class='footer'>
        <p>© 2026 Litoral Automotores - Calidad y Confianza</p>
        <p>📞 Contacto: 099 417 716 | 📍 Paysandú, Uruguay</p>
    </div>
    """, unsafe_allow_html=True)
