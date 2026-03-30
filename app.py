import streamlit as st
import os

# 1. Configuración de la página (Ancho completo profesional)
st.set_page_config(page_title="Litoral Automotores - Catálogo Digital", page_icon="🚗", layout="wide")

# 2. Estilos CSS (Sin espacios blancos y diseño de tarjetas limpio)
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; }
    .header-box { background-color: #1d3557; color: white; padding: 30px; border-radius: 0 0 25px 25px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
    .header-logo { width: 160px; height: 160px; border-radius: 50%; border: 4px solid white; margin-bottom: 15px; object-fit: cover; }
    .header-text h1 { font-family: 'Arial Black', sans-serif; font-size: 3em; color: white; margin: 0; }
    .header-text p { font-size: 1.2em; color: #a8dadc; margin-top: 10px; line-height: 1.3; }
    
    /* Estilo de Tarjetas de Catálogo */
    .car-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 25px; text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: space-between; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.9em; }
    .price-tag { color: #e63946; font-size: 26px; font-weight: bold; margin: 15px 0; }
    
    /* Botones de Contacto profesional */
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 12px; margin: 8px 0; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 1.1em; transition: 0.3s; }
    .btn-info { background-color: #007bff; }
    .btn-info:hover { background-color: #0056b3; }
    .btn-interesa { background-color: #dc3545; }
    .btn-interesa:hover { background-color: #a71d2a; }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Navegación para Zoom y Galerías (Mantenida)
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

# 4. Encabezado Profesional con Logo y Descripción Completa (Resaltando CONSIGNACIONES)
st.markdown("""
    <div class="header-box">
        <div style="display: flex; align-items: center; justify-content: center;">
            <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg" class="header-logo">
            <div class="header-text" style="margin-left: 35px; text-align: left;">
                <h1>LITORAL AUTOMOTORES</h1>
                <p>RECIBIMOS Y COMERCIALIZAMOS TODO TIPO DE VEHÍCULOS DE TODAS LAS DÉCADAS. Especialistas en gestionar <b>CONSIGNACIONES</b> con total transparencia y seguridad.</p>
                <p>Autos, Camionetas, Motos (Cross, Carrera, Pollerita), Trailers y Casas Rodantes. ¡CONSÚLTENOS!</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 5. LÓGICA DE BÚSQUEDA AUTOMÁTICA DE IMÁGENES (Buscador Inteligente Verificado)
base_url = "https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/"

# Escaneamos los archivos reales que hay en la carpeta de GitHub
# (Streamlit busca en la carpeta donde corre el script)
archivos_en_repositorio = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])

# Función para filtrar fotos que EMPIECEN con el nombre dado
def filtrar_fotos_unidad(prefijo):
    return [f for f in archivos_en_repositorio if f.startswith(prefijo)]

# Buscamos las fotos de la Saveiro (Mantenida)
fotos_saveiro = filtrar_fotos_unidad('savblack')

# Buscamos las fotos de la Vitara (Mantenida)
fotos_vitara = filtrar_fotos_unidad('suzukivitara')

# Buscamos las fotos de la SMA C81 (USANDO LOS NUEVOS NOMBRES sma1.jpg, sma2.jpg, etc.)
# Esto asegura que aparezcan múltiples miniaturas
fotos_sma = filtrar_fotos_unidad('sma')

# Buscamos las fotos de la Hyundai Accent (USANDO LOS NUEVOS NOMBRES hyundaiaccentX.jpg y hyunudaiaccent1.jpg con typo)
fotos_hyundai = filtrar_fotos_unidad('hyundaiaccent')
# Agregamos la que tiene el typo por si acaso
foto_typo_hyundai = next((f for f in archivos_en_repositorio if f.startswith('hyunudaiaccent1')), None)
if foto_typo_hyundai and foto_typo_hyundai not in fotos_hyundai:
    # La agregamos al principio como portada si es la principal
    fotos_hyundai.insert(0, foto_typo_hyundai)
# Ordenamos para asegurar consistencia
fotos_hyundai = sorted(fotos_hyundai)

# Función para mostrar tarjeta de auto con galería dinámica
def mostrar_tarjeta(titulo, precio, caracteristicas, fotos_id, ws_link, columna):
    with columna:
        st.markdown('<div class="car-card">', unsafe_allow_html=True)
        st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
        st.markdown(f'<h3 style="margin-top: 10px; font-weight: bold; font-size: 1.3em;">{titulo}</h3>', unsafe_allow_html=True)
        
        if fotos_id:
            # Foto principal clickeable para Zoom
            st.image(fotos_id[0], caption="Portada - Clic para Zoom 🔍", use_container_width=True)
            
            # Miniaturas clickables para galería
            if len(fotos_id) > 1:
                st.write("Más fotos del vehículo:")
                # Creamos columnas para miniaturas dinámicas (hasta 4)
                cols_mini = st.columns(min(len(fotos_id[1:]), 4))
                for idx, foto_galeria in enumerate(fotos_id[1:5]): # Mostramos hasta 4 miniaturas extra
                    with cols_mini[idx]:
                        if st.button(f"🔍", key=f"btn_{foto_galeria}_{idx}"):
                            # Al hacer clic, abre la vista de Zoom de esa foto
                            st.query_params.update(foto=foto_galeria)
                            st.rerun()
                        st.image(foto_galeria, use_container_width=True)

        st.markdown(f'<div class="price-tag">{precio}</div>', unsafe_allow_html=True)
        st.write(f"• {caracteristicas[0]}<br>• {caracteristicas[1]}<br>• {caracteristicas[2]}<br>• {caracteristicas[3]}", unsafe_allow_html=True)
        
        st.markdown(f'<a href="{ws_link}" class="btn-ws btn-info">💬 CONSULTAR</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{ws_link}" class="btn-ws btn-interesa">🔥 LO QUIERO</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Renderizado del Catálogo en Columnas Limpias

# --- FILA 1: VW SAVEIRO C.E (2011) ---
c1, c2 = st.columns(2)
# Mantenemos la descripción detallada de la Saveiro C.E que tanto costó
mostrar_tarjeta(
    "🚗 VW SAVEIRO C.E (2011)", 
    "USD 8.000.-", 
    ["Cabina extendida (Espacio interior)", "Motor 1.6 Nafta (Potente y fiable)", "Incluye protector de caja y barras", "Matrícula Paysandú (IAG)"], 
    fotos_saveiro, 
    "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20la%20Saveiro%20C.E.", 
    c1
)

# --- FILA 1: SUZUKI VITARA GL (2016) ---
mostrar_tarjeta(
    "🚗 SUZUKI VITARA GL (2016)", 
    "USD 14.800.-", 
    ["150.000 km | Servicio al día", "4 cubiertas nuevas", "Muy sana, sin detalles", "Mecánica impecable"], 
    fotos_vitara, 
    "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20la%20Vitara%20GL", 
    c2
)

# --- FILA 2: SMA C81 FULL 1.8 (2009) ---
c3, c4 = st.columns(2)
# USANDO LOS NUEVOS NOMBRES sma1.jpg, sma2.jpg etc., para que cargue toda la galería
mostrar_tarjeta(
    "🚗 SMA C81 Full 1.8 (2009)", 
    "USD 3.500.-", 
    ["Motor 1.8 Nafta Inyección", "Versión Full equipada", "Muy bien cuidado", "Paysandú, Uruguay"], 
    fotos_sma, 
    "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20SMA%20C81", 
    c3
)

# --- FILA 2: HYUNDAI ACCENT 1.5 (1995) ---
# USANDO LOS NUEVOS NOMBRES hyundaiaccentX.jpg/hyunudaiaccent1.jpg para que cargue toda la galería
mostrar_tarjeta(
    "🚗 HYUNDAI ACCENT 1.5 (1995)", 
    "¡Consulte!", 
    ["Motor 1.5 Nafta", "Súper Económico", "Documentación al día", "Listo para circular"], 
    fotos_hyundai, 
    "https://wa.me/59899417716?text=Hola%20Leo,%20estoy%20interesado%20en%20el%20Hyundai%20Accent", 
    c4
)

# Pie de página profesional
st.markdown("<p style='text-align: center; color: gray; margin-top: 50px;'>© 2026 Litoral Automotores | Contacto: 099 417 716 | Paysandú, Uruguay</p>", unsafe_allow_html=True)
