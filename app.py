import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores", page_icon="🚗", layout="wide")

# 2. Estilos CSS para mantener el diseño limpio y sin espacios blancos
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; }
    .header-box { background-color: #1d3557; color: white; padding: 30px; border-radius: 15px; margin-bottom: 20px; text-align: center; }
    .header-logo { width: 160px; border-radius: 50%; border: 4px solid white; margin-bottom: 10px; }
    .car-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px; height: 100%; }
    .price { color: #e63946; font-size: 26px; font-weight: bold; margin: 10px 0; }
    .btn-ws { display: block; width: 100%; text-align: center; color: white !important; padding: 12px; border-radius: 8px; font-weight: bold; text-decoration: none; margin: 5px 0; font-size: 1.1em; }
    .info-text { font-size: 0.95em; line-height: 1.4; text-align: left; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Galería (Zoom) - Esto permite ver la foto grande y volver
if "foto" in st.query_params:
    foto_seleccionada = st.query_params["foto"]
    st.markdown("---")
    if st.button("⬅️ VOLVER AL CATÁLOGO"):
        st.query_params.clear()
        st.rerun()
    st.image(foto_seleccionada, use_container_width=True)
    st.stop()

# 4. Encabezado con logo y descripción completa
st.markdown(f"""
    <div class="header-box">
        <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg" class="header-logo">
        <h1 style="margin:0;">LITORAL AUTOMOTORES - CALIDAD Y CONFIANZA</h1>
        <p style="font-size:1.2em; margin-top:10px;">
            RECIBIMOS Y COMERCIALIZAMOS TODO TIPO DE VEHÍCULOS DE TODAS LAS DÉCADAS.<br>
            Especialistas en gestionar <b>CONSIGNACIONES</b> con total transparencia y seguridad.<br>
            Autos, Camionetas, Motos (Cross, Carrera, Pollerita), Trailers y Casas Rodantes. ¡CONSÚLTENOS!
        </p>
    </div>
    """, unsafe_allow_html=True)

# 5. Obtener lista de archivos para las galerías
archivos_jpg = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])

def crear_tarjeta(titulo, precio, detalles, prefijo_fotos, columna):
    # Filtramos todas las fotos que empiecen con el nombre del vehículo
    fotos_unidad = [f for f in archivos_jpg if f.startswith(prefijo_fotos)]
    
    with columna:
        st.markdown(f'<div class="car-card"><h2 style="text-align:center;">{titulo}</h2>', unsafe_allow_html=True)
        
        if fotos_unidad:
            # Botón de Zoom para la foto principal
            if st.button(f"🔍 AMPLIAR FOTO", key=f"zoom_main_{prefijo_fotos}"):
                st.query_params.update(foto=fotos_unidad[0])
                st.rerun()
            st.image(fotos_unidad[0], use_container_width=True)
            
            # Galería de miniaturas (si hay más de una foto)
            if len(fotos_unidad) > 1:
                st.write("Más fotos (clic en la lupa):")
                # Usamos una fila simple de botones para evitar el error de columnas
                cols_mini = st.columns(4)
                for idx, foto_galeria in enumerate(fotos_unidad[1:5]): # Mostramos hasta 4 miniaturas
                    with cols_mini[idx]:
                        if st.button("🔎", key=f"btn_{foto_galeria}"):
                            st.query_params.update(foto=foto_galeria)
                            st.rerun()
                        st.image(foto_galeria, use_container_width=True)
        
        st.markdown(f'<div class="price" style="text-align:center;">{precio}</div>', unsafe_allow_html=True)
        
        # Descripción detallada
        st.markdown('<div class="info-text">', unsafe_allow_html=True)
        for item in detalles:
            st.write(f"✅ {item}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Botones de contacto
        link_wa = f"https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa%20el%20vehículo:%20{titulo}"
        st.markdown(f'<a href="{link_wa}" class="btn-ws" style="background:#007bff;">💬 CONSULTAR</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{link_wa}" class="btn-ws" style="background:#dc3545;">🔥 ME INTERESA</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Distribución del Catálogo en 2 columnas
c1, c2 = st.columns(2)

crear_tarjeta(
    "VW SAVEIRO C.E (2011)", "USD 8.000.-",
    ["Motor 1.6 Nafta (Potente y confiable)", "Cabina extendida: espacio extra interior", "Incluye protector de caja y barras de techo", "Radio instalada y tapizados firmes", "Matrícula Paysandú (IAG)"],
    "savblack", c1
)

crear_tarjeta(
    "SUZUKI VITARA GL (2016)", "USD 14.800.-",
    ["150.000 km | Servicio al día", "4 cubiertas nuevas", "Muy sana, sin detalles estéticos", "Excelente andar y confort", "Matrícula Paysandú (IAG)"],
    "suzukivitara", c2
)

st.markdown("---")
c3, c4 = st.columns(2)

crear_tarjeta(
    "SMA C81 FULL 1.8 (2009)", "USD 3.500.-",
    ["Motor 1.8 Nafta Inyección (Potente)", "Versión Full con equipamiento completo", "Excelente estado, muy bien cuidado", "Interior espacioso y cómodo"],
    "65587", c3
)

crear_tarjeta(
    "HYUNDAI ACCENT 1.5 (1995)", "¡CONSULTE PRECIO!",
    ["Motor 1.5 Nafta (Consumo muy bajo)", "Títulos y libreta al día", "Mecánica sencilla y confiable", "Listo para circular"],
    "65601", c4
)

# Pie de página
st.markdown("<p style='text-align:center; color:gray; padding:20px;'>© 2026 Litoral Automotores | Paysandú, Uruguay | Leonardo Olivera</p>", unsafe_allow_html=True)
