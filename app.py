import streamlit as st
import os
import requests

# 1. Configuración de la página (Ancho completo para estilo catálogo)
st.set_page_config(page_title="Catálogo Digital - Litoral Automotores", page_icon="🚗", layout="wide")

# 2. Estilo CSS Profesional y Limpio
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-box { background-color: #1d3557; color: white; padding: 30px; border-radius: 0 0 25px 25px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .header-logo { width: 150px; height: 150px; border-radius: 50%; border: 4px solid white; object-fit: cover; }
    .header-text h1 { font-family: 'Arial Black', sans-serif; font-size: 3em; color: white; margin: 0; }
    .header-text p { font-size: 1.1em; color: #a8dadc; margin-top: 10px; }
    .car-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 25px; text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: space-between; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; }
    .price-tag { color: #e63946; font-size: 24px; font-weight: bold; margin: 15px 0; }
    .feature-list { font-size: 0.95em; text-align: left; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 12px; margin: 8px 0; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 1.1em; }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    .footer { text-align: center; color: gray; margin-top: 50px; padding: 20px; border-top: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado Profesional con Logo y Descripción Completa
st.markdown("""
    <div class="header-box">
        <div style="display: flex; align-items: center; justify-content: center;">
            <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg" class="header-logo">
            <div class="header-text" style="margin-left: 30px;">
                <h1>LITORAL AUTOMOTORES</h1>
                <p>Comercializamos vehículos de todas las décadas. Especialistas en gestionar <b>CONSIGNACIONES</b> con total transparencia.</p>
                <p>Autos, Camionetas, Motos Cross, Motos de Carrera, Motos Pollerita, Trailers y Casas Rodantes. ¡CONSÚLTENOS!</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. Lógica de Navegación para Zoom y Galerías
params = st.query_params
if "foto" in params:
    foto_grande = params["foto"]
    st.markdown("---")
    if st.button("⬅️ VOLVER AL CATÁLOGO"):
        st.query_params.clear()
        st.rerun()
    st.image(foto_grande, use_container_width=True)
    if st.button("Cerrar y Volver"):
        st.query_params.clear()
        st.rerun()
    st.stop() # Detiene el renderizado del catálogo para mostrar solo la foto

# 5. Lógica de Separación Estricta de Fotos
todos_los_archivos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])

# Función para filtrar fotos que EMPIECEN con el prefijo dado
def filtrar_fotos(prefijo):
    return [f for f in todos_los_archivos if f.startswith(prefijo)]

# Separamos las fotos por código exacto para evitar mezclas
fotos_sma = filtrar_fotos('65587') # SMA Pizarrones
fotos_hyundai = filtrar_fotos('65601') # Hyundai Rojo

# Función para mostrar tarjeta de auto
def mostrar_tarjeta(titulo, precio, caracteristicas, fotos_id, ws_link, columna):
    with columna:
        st.markdown('<div class="car-card">', unsafe_allow_html=True)
        st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
        st.markdown(f'<h3>{titulo}</h3>', unsafe_allow_html=True)
        
        if fotos_id:
            st.image(fotos_id[0], caption="Portada - Clic para Zoom 🔍", use_container_width=True)
            # Miniaturas clickables para galería
            mini_cols = st.columns(min(len(fotos_id[1:]), 3)) # Hasta 3 miniaturas
            for i, foto in enumerate(fotos_id[1:]):
                with mini_cols[i]:
                    if st.button(f"🔍", key=f"btn_{foto}"):
                        st.query_params.update(foto=foto)
                        st.rerun()
                    st.image(foto, use_container_width=True)

        st.markdown(f'<div class="price-tag">{precio}</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-list">', unsafe_allow_html=True)
        for c in caracteristicas: st.write(f"✅ {c}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown(f'<a href="{ws_link}" class="btn-ws btn-info">💬 CONSULTAR</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{ws_link}" class="btn-ws btn-interesa">🔥 LO QUIERO</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Renderizado del Catálogo en 2 Columnas Limpias
col_h, col_s = st.columns(2)

# --- COLUMNA HYUNDAI ACCENT (Auto Rojo) ---
mostrar_tarjeta(
    "🚗 HYUNDAI ACCENT 1.5 (1995)",
    "¡ECONÓMICO!",
    ["Motor 1.5 Nafta (Consumo Mínimo)", "Muy económico", "Documentación al día", "Listo para transferir"],
    fotos_hyundai,
    "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20Hyundai%20Accent",
    col_h
)

# --- COLUMNA SMA C81 (Pizarrones) ---
mostrar_tarjeta(
    "🚗 SMA C81 FULL 1.8 (2009)",
    "USD 3.500.-",
    ["Motor 1.8 Nafta Inyección (Potente)", "Versión Full equipada", "Excelente estado general", "Paysandú, Uruguay"],
    fotos_sma,
    "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20SMA%20C81",
    col_s
)

# 7. Pie de página
st.markdown("<p class='footer'>© 2026 Litoral Automotores | Contacto: 099 417 716 | Paysandú, Uruguay</p>", unsafe_allow_html=True)
