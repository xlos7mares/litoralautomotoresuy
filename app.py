import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores", page_icon="🚗", layout="wide")

# 2. LÓGICA DE IMÁGENES (Buscador automático en tu GitHub)
archivos = sorted([f for f in os.listdir('.') if f.lower().endswith('.jpg')])
f_sav = [f for f in archivos if 'savblack' in f.lower()]
f_vit = [f for f in archivos if 'vitara' in f.lower()]
f_sma = [f for f in archivos if f.startswith('657') or f.startswith('655') or f.startswith('65615')]
f_hyu = [f for f in archivos if f.startswith('656') and f not in f_sma]

# URLs de portadas (si no hay fotos, queda vacío)
img_sav = f_sav[0] if f_sav else ""
img_vit = f_vit[0] if f_vit else ""
img_sma = f_sma[0] if f_sma else ""
img_hyu = f_hyu[0] if f_hyu else ""

# 3. TODO EL DISEÑO EN UN SOLO BLOQUE (Para evitar espacios blancos)
logo_url = "https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg"

diseno_html = f"""
<style>
    /* Eliminar márgenes de Streamlit */
    .block-container {{ padding: 0rem !important; margin: 0rem !important; }}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .main-body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8f9fa; min-height: 100vh; }}
    
    /* Encabezado Azul */
    .header-blue {{
        background-color: #1d3557;
        color: white;
        padding: 40px 50px;
        display: flex;
        align-items: center;
        border-radius: 0 0 30px 30px;
    }}
    .logo-img {{
        width: 180px; height: 180px; border-radius: 50%; border: 4px solid white; object-fit: cover; flex-shrink: 0;
    }}
    .header-text {{ margin-left: 35px; }}
    .header-text h1 {{ font-size: 3.5em; margin: 0; line-height: 1; }}
    .header-text p {{ font-size: 1.2em; color: #a8dadc; margin-top: 10px; }}

    /* Grilla de Ventas */
    .grid-autos {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px;
        padding: 30px;
        margin-top: -30px;
    }}
    .card {{
        background: white; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); padding: 20px; text-align: center;
    }}
    .img-auto {{ width: 100%; border-radius: 10px; margin-bottom: 15px; height: 200px; object-fit: cover; }}
    .precio {{ color: #e63946; font-size: 24px; font-weight: bold; margin: 10px 0; }}
    .badge {{ background: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.8em; font-weight: bold; }}
    
    .btn {{
        display: block; padding: 12px; margin: 8px 0; border-radius: 8px; text-decoration: none; font-weight: bold; color: white !important;
    }}
    .btn-blue {{ background-color: #007bff; }}
    .btn-red {{ background-color: #dc3545; }}
</style>

<div class="main-body">
    <div class="header-blue">
        <img src="{logo_url}" class="logo-img">
        <div class="header-text">
            <h1>LITORAL AUTOMOTORES</h1>
            <p>Comercializamos vehículos de todas las décadas. Especialistas en gestionar <b>CONSIGNACIONES</b>.</p>
            <p>Autos, Camionetas, Motos, Trailers y Casas Rodantes. ¡CONSÚLTENOS!</p>
        </div>
    </div>

    <div class="grid-autos">
        <div class="card">
            <span class="badge">EN VENTA!</span>
            <h3>VW Saveiro C.E (2011)</h3>
            <img src="{img_sav}" class="img-auto">
            <div class="precio">USD 8.000</div>
            <p>• Motor 1.6 Nafta<br>• 230k km originales</p>
            <a href="https://wa.me/59899417716?text=Saveiro" class="btn btn-blue">💬 CONSULTAR</a>
            <a href="https://wa.me/59899417716?text=Saveiro" class="btn btn-red">🔥 LO QUIERO</a>
        </div>

        <div class="card">
            <span class="badge">EN VENTA!</span>
            <h3>Suzuki Vitara GL (2016)</h3>
            <img src="{img_vit}" class="img-auto">
            <div class="precio">USD 14.800</div>
            <p>• 150k km | Servicio al día<br>• Muy sana, sin detalles</p>
            <a href="https://wa.me/59899417716?text=Vitara" class="btn btn-blue">💬 CONSULTAR</a>
            <a href="https://wa.me/59899417716?text=Vitara" class="btn btn-red">🔥 LO QUIERO</a>
        </div>

        <div class="card">
            <span class="badge">EN VENTA!</span>
            <h3>SMA C81 Full (2009)</h3>
            <img src="{img_sma}" class="img-auto">
            <div class="precio">USD 3.500</div>
            <p>• Motor 1.8 Nafta Inyección<br>• Versión Full equipada</p>
            <a href="https://wa.me/59899417716?text=SMA" class="btn btn-blue">💬 CONSULTAR</a>
            <a href="https://wa.me/59899417716?text=SMA" class="btn btn-red">🔥 LO QUIERO</a>
        </div>

        <div class="card">
            <span class="badge">EN VENTA!</span>
            <h3>Hyundai Accent (1995)</h3>
            <img src="{img_hyu}" class="img-auto">
            <div class="precio">¡CONSULTE!</div>
            <p>• Motor 1.5 Nafta<br>• Documentación al día</p>
            <a href="https://wa.me/59899417716?text=Hyundai" class="btn btn-blue">💬 CONSULTAR</a>
            <a href="https://wa.me/59899417716?text=Hyundai" class="btn btn-red">🔥 LO QUIERO</a>
        </div>
    </div>
    
    <p style="text-align: center; color: gray; padding: 20px;">© 2026 Litoral Automotores | Paysandú, Uruguay</p>
</div>
"""

# ESTA LÍNEA ES LA QUE ACTIVA TODO EL DISEÑO
st.markdown(diseno_html, unsafe_allow_html=True)
