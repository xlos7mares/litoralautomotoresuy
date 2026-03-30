import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores - Catálogo", page_icon="🚗", layout="wide")

# 2. Estilos CSS (Sin espacios blancos, logo redondo y diseño profesional)
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; }
    .stApp { background-color: #f8f9fa; }
    
    .header-box { 
        background-color: #1d3557; color: white; padding: 30px; 
        border-radius: 0px 0px 25px 25px; margin-top: -60px !important; 
        margin-bottom: 20px; text-align: center;
    }
    .header-logo { width: 180px; height: 180px; border-radius: 50%; border: 4px solid white; object-fit: cover; }
    
    .car-card { 
        background: white; padding: 20px; border-radius: 15px; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px; 
        height: 100%; text-align: center;
    }
    .price { color: #e63946; font-size: 26px; font-weight: bold; margin: 10px 0; }
    .badge-venta { background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.9em; }
    
    .info-seguro { background-color: #e9ecef; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 5px solid #004a99; font-size: 0.9em; text-align: left; }
    .info-patente { background-color: #fff3cd; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 5px solid #ffc107; font-size: 0.9em; text-align: left; }
    
    .btn-ws { 
        display: block; width: 100%; text-align: center; color: white !important; 
        padding: 12px; border-radius: 8px; font-weight: bold; 
        text-decoration: none; margin: 5px 0; font-size: 1.1em; 
    }
    .btn-info { background-color: #007bff; }
    .btn-interesa { background-color: #dc3545; }
    
    .info-text { font-size: 0.95em; line-height: 1.4; text-align: left; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Zoom (Mantenida)
if "foto" in st.query_params:
    foto_full = st.query_params["foto"]
    st.markdown("---")
    if st.button("⬅️ VOLVER AL CATÁLOGO"):
        st.query_params.clear()
        st.rerun()
    st.image(foto_full, use_container_width=True)
    st.stop()

# 4. Encabezado Profesional
st.markdown(f"""
    <div class="header-box">
        <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg" class="header-logo">
        <h1 style="margin:0; font-size: 2.8em;">LITORAL AUTOMOTORES</h1>
        <p style="font-size:1.2em; margin-top:10px;">
            RECIBIMOS Y COMERCIALIZAMOS TODO TIPO DE VEHÍCULOS DE TODAS LAS DÉCADAS.<br>
            Especialistas en gestionar <b>CONSIGNACIONES</b> con total transparencia y seguridad.<br>
            <b>ASESOR DE SEGUROS SAN CRISTÓBAL</b> - ¡Consulte su cotización!
        </p>
    </div>
    """, unsafe_allow_html=True)

# 5. Lógica de Archivos e Impuestos
archivos_en_github = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])

def mostrar_unidad(titulo, precio, detalles, prefijo, patente_cuota, patente_total, col):
    fotos_encontradas = [f for f in archivos_en_github if f.lower().startswith(prefijo.lower())]
    
    with col:
        st.markdown(f'<div class="car-card"><h3>{titulo}</h3>', unsafe_allow_html=True)
        st.markdown("<span class='badge-venta'>EN VENTA!</span>", unsafe_allow_html=True)
        
        if fotos_encontradas:
            if st.button(f"🔍 AMPLIAR PORTADA", key=f"z_main_{prefijo}"):
                st.query_params.update(foto=fotos_encontradas[0])
                st.rerun()
            st.image(fotos_encontradas[0], use_container_width=True)
            
            if len(fotos_encontradas) > 1:
                m_cols = st.columns(4)
                for i, f_gal in enumerate(fotos_encontradas[1:5]):
                    with m_cols[i % 4]:
                        if st.button("🔎", key=f"m_{f_gal}_{prefijo}"):
                            st.query_params.update(foto=f_gal)
                            st.rerun()
                        st.image(f_gal, use_container_width=True)
        
        st.markdown(f'<div class="price">{precio}</div>', unsafe_allow_html=True)
        
        # --- BLOQUE DE IMPUESTOS Y SEGURO ---
        st.markdown(f"""
            <div class="info-seguro">
                <b>🛡️ SEGURO SAN CRISTÓBAL:</b><br>
                $ 4.900 (RC + SOA + Auxilio Mecánico)
            </div>
            <div class="info-patente">
                <b>📋 PATENTE SUCIVE (Aprox.):</b><br>
                6 Cuotas de: {patente_cuota}<br>
                Total Anual: {patente_total}
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="info-text">', unsafe_allow_html=True)
        for d in detalles:
            st.write(f"✅ {d}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        msg = f"https://wa.me/59899417716?text=Hola%20Leo,%20me%20interesa:%20{titulo}"
        st.markdown(f'<a href="{msg}" class="btn-ws btn-info">💬 CONSULTAR</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{msg}" class="btn-ws btn-interesa">🔥 ME INTERESA</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Grilla de Vehículos
c1, c2 = st.columns(2)

mostrar_unidad(
    "VW SAVEIRO C.E (2011)", "USD 8.000.-",
    ["Motor 1.6 Nafta (Potente y confiable)", "Cabina extendida", "Incluye protector de caja y barras", "Matrícula Paysandú (IAG)"],
    "savblack", "$ 1.850", "$ 11.100", c1
)

mostrar_unidad(
    "SUZUKI VITARA GL (2016)", "USD 14.800.-",
    ["150.000 km | Servicio al día", "4 cubiertas nuevas", "Muy sana, sin detalles", "Matrícula Paysandú (IAG)"],
    "suzukivitara", "$ 3.450", "$ 20.700", c2
)

st.markdown("---")
c3, c4 = st.columns(2)

mostrar_unidad(
    "SMA C81 FULL 1.8 (2009)", "USD 3.500.-",
    ["Motor 1.8 Nafta Inyección", "Versión Full equipada", "Excelente estado, muy bien cuidado", "Espacioso y cómodo"],
    "sma", "$ 1.150", "$ 6.900", c3
)

mostrar_unidad(
    "HYUNDAI ACCENT 1.5 (1995)", "¡CONSULTE!",
    ["Motor 1.5 Nafta (Bajo consumo)", "Títulos y libreta al día", "Listo para rodar", "Ideal para el día a día"],
    "hyundaiaccent", "$ 750", "$ 4.500", c4
)

st.markdown("<p style='text-align:center; color:gray; padding:20px;'>© 2026 Litoral Automotores | Paysandú, Uruguay</p>", unsafe_allow_html=True)
