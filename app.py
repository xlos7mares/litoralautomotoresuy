import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Catálogo", page_icon="🚗", layout="wide")

# Estilo CSS para que las imágenes parezcan botones y el encabezado sea profesional
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-container { display: flex; align-items: center; background-color: #1d3557; color: white; padding: 30px; border-radius: 15px; margin-bottom: 30px; }
    .header-logo { flex: 1; max-width: 250px; }
    .header-logo img { width: 100%; border-radius: 50%; }
    .header-text { flex: 3; padding-left: 30px; }
    .header-text h1 { font-family: 'Arial Black'; color: white; font-size: 3em; margin-bottom: 10px; }
    .header-text p { font-size: 1.2em; color: #a8dadc; line-height: 1.4; }
    
    /* Estilo para que la imagen sea clickeable */
    .img-container { cursor: pointer; transition: 0.3s; }
    .img-container:hover { opacity: 0.8; transform: scale(1.02); }
    
    .car-card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 10px; }
    .price-tag { color: #e63946; font-size: 24px; font-weight: bold; margin: 10px 0px; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 15px; margin: 10px 0; border-radius: 8px; font-weight: bold; text-decoration: none; }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    .btn-volver { background-color: #6c757d; color: white !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN (FOTO EN GRANDE) ---
# Revisamos si el usuario hizo clic en alguna foto
params = st.query_params
if "foto" in params:
    foto_grande = params["foto"]
    st.markdown("---")
    if st.button("⬅️ VOLVER AL CATÁLOGO"):
        st.query_params.clear()
        st.rerun()
    
    st.image(foto_grande, use_container_width=True)
    
    if st.button("Cerrar y volver"):
        st.query_params.clear()
        st.rerun()
    st.stop() # Detiene el resto de la web para mostrar solo la foto

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
fotos_sma = [f for f in archivos if f.startswith('657') or f.startswith('655') or f.startswith('65615')]
fotos_hyundai = [f for f in archivos if f.startswith('656') and f not in fotos_sma]

col1, col2 = st.columns(2)

# Función para mostrar tarjeta de auto
def mostrar_auto(titulo, precio, caracteristicas, lista_fotos, ws_link):
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
    st.markdown(f'<h3>{titulo}</h3>', unsafe_allow_html=True)
    
    if lista_fotos:
        # Foto Principal (Clickable)
        if st.button(f"Ver Portada 🔍", key=lista_fotos[0]):
            st.query_params.update(foto=lista_fotos[0])
            st.rerun()
        st.image(lista_fotos[0], use_container_width=True)
        
        # Miniaturas (Clickables)
        mini = st.columns(4)
        for i, foto in enumerate(lista_fotos[1:5]):
            with mini[i]:
                if st.button("🔍", key=f"btn_{foto}"):
                    st.query_params.update(foto=foto)
                    st.rerun()
                st.image(foto, use_container_width=True)

    st.markdown(f'<div class="price-tag">{precio}</div>', unsafe_allow_html=True)
    for c in caracteristicas:
        st.write(f"✅ {c}")
    
    st.markdown(f'<a href="{ws_link}" target="_blank" class="btn-ws btn-info">💬 CONSULTAR INFO</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{ws_link}" target="_blank" class="btn-ws btn-interesa">🔥 ME INTERESA</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- RENDERIZADO ---
with col1:
    mostrar_auto("SMA C81 Full 1.8 (2009)", "USD 3500.-", 
                 ["1.8 Nafta Inyección", "Versión Full", "Excelente estado"], 
                 fotos_sma, "https://wa.me/59899417716?text=Interés%20SMA")

with col2:
    mostrar_auto("HYUNDAI ACCENT 1.5 (1995)", "¡ECONÓMICO!", 
                 ["1.5 Nafta", "Documentos al día", "Listo para transferir"], 
                 fotos_hyundai, "https://wa.me/59899417716?text=Interés%20Hyundai")

st.markdown("<p style='text-align: center; color: gray;'>© 2026 Litoral Automotores | Paysandú</p>", unsafe_allow_html=True)
