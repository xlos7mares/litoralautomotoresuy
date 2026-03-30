import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores", page_icon="🚗", layout="wide")

# 2. Estilos CSS
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

# 3. Lógica de Zoom (Galería)
if "foto" in st.query_params:
    foto_seleccionada = st.query_params["foto"]
    st.markdown("---")
    if st.button("⬅️ VOLVER AL CATÁLOGO"):
        st.query_params.clear()
        st.rerun()
    st.image(foto_seleccionada, use_container_width=True)
    st.stop()

# 4. Encabezado
st.markdown(f"""
    <div class="header-box">
        <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg" class="header-logo">
        <h1 style="margin:0;">LITORAL AUTOMOTORES - CALIDAD Y CONFIANZA</h1>
        <p style="font-size:1.2em; margin-top:10px;">
            RECIBIMOS Y COMERCIALIZAMOS TODO TIPO DE VEHÍCULOS DE TODAS LAS DÉCADAS.<br>
            Especialistas en gestionar <b>CONSIGNACIONES</b> con total transparencia y seguridad.<br>
            Autos, Camionetas, Motos, Trailers y Casas Rodantes. ¡CONSÚLTENOS!
        </p>
    </div>
    """, unsafe_allow_html=True)

# 5. Lista de archivos
archivos_jpg = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])

def crear_tarjeta(titulo, precio, detalles, lista_prefijos, columna):
    # Ahora buscamos fotos que empiecen con CUALQUIERA de los prefijos de la lista
    # Esto asegura que si el SMA tiene fotos con distintos números, las agarre todas
    fotos_unidad = []
    for prefijo in lista_prefijos:
        fotos_unidad.extend([f for f in archivos_jpg if f.startswith(prefijo)])
    
    # Eliminamos duplicados por las dudas
    fotos_unidad = sorted(list(set(fotos_unidad)))
    
    with columna:
        st.markdown(f'<div class="car-card"><h2 style="text-align:center;">{titulo}</h2>', unsafe_allow_html=True)
        
        if fotos_unidad:
            # Portada
            if st.button(f"🔍 AMPLIAR PORTADA", key=f"zoom_main_{titulo}"):
                st.query_params.update(foto=fotos_unidad[0])
                st.rerun()
            st.image(fotos_unidad[0], use_container_width=True)
            
            # Galería de miniaturas (Corregida para que se vea bien)
            if len(fotos_unidad) > 1:
                st.write("Más fotos del vehículo:")
                cols_mini = st.columns(4)
                for idx, foto_galeria in enumerate(fotos_unidad[1:9]): # Hasta 8 fotos extra
                    with cols_mini[idx % 4]:
                        if st.button("🔎", key=f"btn_{foto_galeria}_{idx}"):
                            st.query_params.update(foto=foto_galeria)
                            st.rerun()
                        st.image(foto_galeria, use_container_width=True)
        
        st.markdown(f'<div class="price" style="text-align:center;">{precio}</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-text">', unsafe_allow_html=True)
        for item in detalles:
            st.write(f"✅ {item}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        link_wa = f"https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa:%20{titulo}"
        st.markdown(f'<a href="{link_wa}" class="btn-ws" style="background:#007bff;">💬 CONSULTAR</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{link_wa}" class="btn-ws" style="background:#dc3545;">🔥 ME INTERESA</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Distribución (FILA 1)
c1, c2 = st.columns(2)
crear_tarjeta("VW SAVEIRO C.E (2011)", "USD 8.000.-", ["Motor 1.6 Nafta", "Cabina extendida", "Protector de caja y barras", "Matrícula Paysandú (IAG)"], ["savblack"], c1)
crear_tarjeta("SUZUKI VITARA GL (2016)", "USD 14.800.-", ["150.000 km | Servicio al día", "4 cubiertas nuevas", "Muy sana, sin detalles", "Matrícula Paysandú (IAG)"], ["suzukivitara"], c2)

st.markdown("---")

# 7. Distribución (FILA 2 - CORREGIDA)
c3, c4 = st.columns(2)

# SMA: Solo fotos que empiecen con 655 o 657 (que son los del pizarrón blanco y el auto blanco)
crear_tarjeta("SMA C81 FULL 1.8 (2009)", "USD 3.500.-", ["Motor 1.8 Nafta Inyección", "Versión Full", "Muy bien cuidado", "Interior espacioso"], ["65587", "65722"], c3)

# HYUNDAI: Solo fotos que empiecen con 656 (que son las del auto rojo)
crear_tarjeta("HYUNDAI ACCENT 1.5 (1995)", "¡CONSULTE!", ["Motor 1.5 Nafta", "Títulos al día", "Mecánica sencilla", "Listo para circular"], ["65601"], c4)

st.markdown("<p style='text-align:center; color:gray; padding:20px;'>© 2026 Litoral Automotores | Paysandú, Uruguay</p>", unsafe_allow_html=True)
