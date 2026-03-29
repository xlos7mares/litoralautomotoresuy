import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Clasificados", page_icon="🚗", layout="wide")

# 2. Estilo CSS Profesional
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .header-container { text-align: center; padding: 20px; background-color: white; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); }
    .car-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); margin-bottom: 30px; min-height: 850px; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.9em; display: inline-block; }
    .price-tag { background-color: #e9ecef; color: #1d3557; padding: 5px 15px; border-radius: 5px; font-weight: bold; font-size: 1.2em; display: inline-block; margin-top: 10px; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 12px; margin: 8px 0; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 1.1em; }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    .footer { text-align: center; padding: 20px; background-color: #1d3557; color: white; margin-top: 50px; border-radius: 10px 10px 0 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado
st.markdown("""
    <div class='header-container'>
        <h1 style='color: #1d3557; margin-bottom: 0;'>Litoral Automotores</h1>
        <p style='color: #457b9d; font-weight: bold;'>Catálogo Digital de Vehículos - Paysandú</p>
        <p style='font-size: 0.9em; color: #666;'>Autos, Camionetas, Motos, Trailers y Casas Rodantes.</p>
        <h2 style='color: #1d3557; border-top: 2px solid #eee; padding-top: 10px;'>🚗 UNIDADES DISPONIBLES</h2>
    </div>
    """, unsafe_allow_html=True)

# 4. FILTRADO ESTRICTO DE IMÁGENES
# Obtenemos todos los archivos .jpg
archivos = [f for f in os.listdir('.') if f.lower().endswith('.jpg')]

# Separamos por nombres exactos para evitar mezclas
# Fotos del SMA (Pizarrón y Auto Blanco)
fotos_sma = [f for f in archivos if f.startswith('65711') or f.startswith('65705') or f.startswith('65587') or f.startswith('65615') or f.startswith('65759')]

# Fotos del Hyundai (Auto Rojo)
fotos_hyundai = [f for f in archivos if f.startswith('65601') or f.startswith('65677') or f.startswith('65691') or f.startswith('65667')]

# 5. Renderizado
col_h, col_s = st.columns(2)

# --- COLUMNA HYUNDAI ACCENT ---
with col_h:
    st.markdown("<div class='car-card'>", unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    st.markdown("<h3>🚗 HYUNDAI ACCENT 1.5 (1995)</h3>", unsafe_allow_html=True)
    
    if fotos_hyundai:
        st.image(fotos_hyundai[0], use_container_width=True) # Principal Roja
        mini_h = st.columns(3)
        for i, foto in enumerate(fotos_hyundai[1:]):
            with mini_h[i % 3]:
                st.image(foto, use_container_width=True)
    
    st.write("✅ **Motor:** 1.5 Nafta (Consumo mínimo)")
    st.write("✅ **Documentación:** Títulos y libreta al día.")
    
    ws_h = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20Hyundai%20Accent"
    st.markdown(f"<a href='{ws_h}' class='btn-ws btn-info'>💬 CONSULTAR AHORA</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{ws_h}' class='btn-ws btn-interesa'>🔥 ME INTERESA</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- COLUMNA SMA C81 ---
with col_s:
    st.markdown("<div class='car-card'>", unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    st.markdown("<h3>🚗 SMA C81 FULL 1.8 (2009)</h3>", unsafe_allow_html=True)
    st.markdown("<div class='price-tag'>PRECIO USD 3500</div>", unsafe_allow_html=True)
    
    if fotos_sma:
        st.image(fotos_sma[0], use_container_width=True) # Principal Pizarrón/Blanco
        mini_s = st.columns(3)
        for i, foto in enumerate(fotos_sma[1:]):
            with mini_s[i % 3]:
                st.image(foto, use_container_width=True)

    st.write("✅ **Motor:** 1.8 Nafta Inyección (Potente)")
    st.write("✅ **Estado:** Versión Full, muy cómodo.")
    
    ws_s = "https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20SMA%20C81"
    st.markdown(f"<a href='{ws_s}' class='btn-ws btn-info'>💬 CONSULTAR AHORA</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{ws_s}' class='btn-ws btn-interesa'>🔥 ME INTERESA</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Pie de página
st.markdown("<div class='footer'><p>© 2026 Litoral Automotores | Contacto: 099 417 716</p></div>", unsafe_allow_html=True)
