import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores", page_icon="🚗", layout="wide")

# 2. Enlaces Directos de Imágenes (Para asegurar que carguen siempre)
base = "https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/"
logo = base + "601396473_3654982237974663_5290087789832669203_n.jpg"

# Portadas
img_sav = base + "savblack1.jpg"
img_vit = base + "suzukivitara13.jpg"
img_sma = base + "655872262_3758670767605809_6449769683858621609_n.jpg"
img_hyu = base + "656015569_1109062323719001_1833132791485600122_n.jpg"

# 3. Diseño HTML/CSS
html_diseno = f"""
<style>
    .block-container {{ padding: 0rem !important; margin: 0rem !important; }}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .header-azul {{
        background-color: #1d3557; color: white; padding: 40px;
        display: flex; align-items: center; border-radius: 0 0 30px 30px; margin-top: -50px;
    }}
    .logo-img {{ width: 180px; height: 180px; border-radius: 50%; border: 4px solid white; object-fit: cover; }}
    .header-texto {{ margin-left: 30px; font-family: sans-serif; }}
    
    .grid-autos {{
        display: flex; flex-wrap: wrap; gap: 20px; padding: 20px; justify-content: center;
        font-family: sans-serif;
    }}
    .tarjeta {{
        background: white; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        padding: 20px; width: 300px; text-align: center; margin-bottom: 10px;
    }}
    .img-car {{ width: 100%; border-radius: 10px; height: 200px; object-fit: cover; background: #eee; }}
    .precio {{ color: #e63946; font-size: 24px; font-weight: bold; margin: 10px 0; }}
    .btn {{
        display: block; padding: 12px; margin: 5px 0; border-radius: 8px;
        text-decoration: none; font-weight: bold; color: white !important;
    }}
</style>

<div class="header-azul">
    <img src="{logo}" class="logo-img">
    <div class="header-texto">
        <h1 style="margin:0; font-size: 3em;">LITORAL AUTOMOTORES</h1>
        <p style="margin:5px 0; color: #a8dadc; font-size: 1.2em;">Expertos en <b>CONSIGNACIONES</b>. Paysandú, Uruguay.</p>
    </div>
</div>

<div class="grid-autos">
    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3>VW Saveiro (2011)</h3>
        <img src="{img_sav}" class="img-car">
        <div class="precio">USD 8.000</div>
        <p>Motor 1.6 | Cabina Extendida</p>
        <a href="https://wa.me/59899417716?text=Saveiro" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Saveiro" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3>Suzuki Vitara (2016)</h3>
        <img src="{img_vit}" class="img-car">
        <div class="precio">USD 14.800</div>
        <p>150k km | Impecable estado</p>
        <a href="https://wa.me/59899417716?text=Vitara" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Vitara" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3>SMA C81 (2009)</h3>
        <img src="{img_sma}" class="img-car">
        <div class="precio">USD 3.500</div>
        <p>Motor 1.8 | Full Full</p>
        <a href="https://wa.me/59899417716?text=SMA" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=SMA" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3>Hyundai Accent (95)</h3>
        <img src="{img_hyu}" class="img-car">
        <div class="precio">¡CONSULTE!</div>
        <p>Muy económico | Al día</p>
        <a href="https://wa.me/59899417716?text=Hyundai" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Hyundai" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>
</div>

<p style="text-align: center; color: gray; font-family: sans-serif; padding-bottom: 30px;">© 2026 Litoral Automotores | Paysandú</p>
"""

st.write(html_diseno, unsafe_allow_html=True)
