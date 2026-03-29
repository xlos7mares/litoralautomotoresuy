import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Catálogo", page_icon="🚗", layout="wide")

# Estilo CSS para Galería, Zoom y Encabezado
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-container { display: flex; align-items: center; background-color: #1d3557; color: white; padding: 30px; border-radius: 15px; margin-bottom: 30px; }
    .header-logo { flex: 1; max-width: 200px; }
    .header-logo img { width: 100%; border-radius: 50%; }
    .header-text { flex: 3; padding-left: 30px; }
    .header-text h1 { font-family: 'Arial Black'; color: white; font-size: 2.8em; margin-bottom: 10px; }
    .header-text p { font-size: 1.1em; color: #a8dadc; line-height: 1.4; }
    
    .car-card { background-color: white; padding: 15px; border-radius: 12px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center; min-height: 750px; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 10px; }
    .price-tag { color: #e63946; font-size: 22px; font-weight: bold; margin: 10px 0px; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 12px; margin: 5px 0; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 1em; }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN (ZOOM DE FOTOS) ---
params = st.query_params
if "foto" in params:
    foto_grande = params["foto"]
    st.markdown("---")
    if st.button("⬅️ VOLVER AL CATÁLOGO"):
        st.query_params.clear()
        st.rerun()
    st.image(foto_grande, use_container_width=True)
    if st.button("Cerrar Vista"):
        st.query_params.clear()
        st.rerun()
    st.stop()

# --- ENCABEZADO ---
logo_url = "https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg"
st.markdown(f"""
    <div class='header-container'>
        <div class='header-logo'><img src='{logo_url}'></div>
        <div class='header-text'>
            <h1>LITORAL AUTOMOTORES</h1>
            <p>RECIBIMOS Y COMERCIALIZAMOS TODO TIPO DE VEHÍCULOS DE TODAS LAS DÉCADAS. Especialistas en gestionar <b>CONSIGNACIONES</b> con total transparencia y seguridad. Autos, Camionetas, Motos, Trailers y Casas Rodantes. ¡CONSÚLTENOS!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- FILTRADO DE FOTOS ---
archivos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])
fotos_saveiro = [f for f in archivos if 'savblack' in f.lower()]
fotos_vitara = [f for f in archivos if 'suzukivitara' in f.lower() or 'suzukvitara' in f.lower()]
fotos_sma = [f for f in archivos if f.startswith('657') or f.startswith('655') or f.startswith('65615')]
fotos_hyundai = [f for f in archivos if f.startswith('656') and f not in fotos_sma]

# Función para mostrar tarjeta de auto
def mostrar_auto(titulo, precio, caracteristicas, lista_fotos, ws_msg):
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    st.markdown(f'<div style="height: 60px; font-weight: bold; font-size: 1.1em;">{titulo}</div>', unsafe_allow_html=True)
    
    if lista_fotos:
        # Portada con botón de Zoom
        if st.button(f"🔍 Ver Grande", key=f"main_{lista_fotos[0]}"):
            st.query_params.update(foto=lista_fotos[0])
            st.rerun()
        st.image(lista_fotos[0], use_container_width=True)
        
        # Miniaturas con Zoom
        mini = st.columns(3)
        for i, foto in enumerate(lista_fotos[1:4]):
            with mini[i]:
                if st.button("🔍", key=f"zoom_{foto}"):
                    st.query_params.update(foto=foto)
                    st.rerun()
                st.image(foto, use_container_width=True)

    st.markdown(f'<div class="price-tag">{precio}</div>', unsafe_allow_html=True)
    for c in caracteristicas:
        st.write(f"• {c}")
    
    ws_url = f"https://wa.me/59899417716?text={ws_msg.replace(' ', '%20')}"
    st.markdown(f'<a href="{ws_url}" target="_blank" class="btn-ws btn-info">💬 CONSULTAR</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{ws_url}" target="_blank" class="btn-ws btn-interesa">🔥 LO QUIERO</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- RENDERIZADO DEL CATÁLOGO ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    mostrar_auto("VW Saveiro Cab. Extendida (2011)", "USD 8.000.-", 
                 ["230.430 km | Motor 1.6", "Protector de caja y barras", "Matrícula Paysandú (IAG)"], 
                 fotos_saveiro, "Hola Leo, me interesa la Saveiro 2011")

with col2:
    mostrar_auto("Suzuki Vitara GL (2016)", "USD 14.800.-", 
                 ["150.000 km | 4 cubiertas nuevas", "Servicio al día", "Muy sana, sin detalles"], 
                 fotos_vitara, "Hola Leo, me interesa la Suzuki Vitara 2016")

with col3:
    mostrar_auto("SMA C81 Full 1.8 (2009)", "USD 3.500.-", 
                 ["Motor 1.8 Nafta Inyección", "Versión Full equipada", "Excelente estado"], 
                 fotos_sma, "Hola Leo, me interesa el SMA C81")

with col4:
    mostrar_auto("Hyundai Accent 1.5 (1995)", "¡CONSULTE!", 
                 ["Motor 1.5 Nafta", "Súper Económico", "Documentación al día"], 
                 fotos_hyundai, "Hola Leo, me interesa el Hyundai Accent")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Litoral Automotores | 099 417 716 | Paysandú, Uruguay</p>", unsafe_allow_html=True)
