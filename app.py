import streamlit as st
import os

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores", page_icon="🚗", layout="wide")

# 2. Lógica para encontrar tus fotos en GitHub
archivos = [f for f in os.listdir('.') if f.lower().endswith('.jpg')]
f_sav = next((f for f in archivos if 'savblack1' in f.lower()), "")
f_vit = next((f for f in archivos if 'vitara' in f.lower()), "")
f_sma = next((f for f in archivos if f.startswith('657') or f.startswith('655')), "")
f_hyu = next((f for f in archivos if f.startswith('656') and '65615' not in f), "")

# 3. El diseño (HTML y CSS)
logo_url = "https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg"

html_final = f"""
<style>
    /* Forzar eliminación de márgenes */
    .block-container {{ padding: 0rem !important; margin: 0rem !important; }}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .header-azul {{
        background-color: #1d3557;
        color: white;
        padding: 40px;
        display: flex;
        align-items: center;
        border-radius: 0 0 30px 30px;
        margin-top: -50px;
    }}
    .logo-img {{
        width: 180px; height: 180px; border-radius: 50%; border: 4px solid white; object-fit: cover;
    }}
    .header-texto {{ margin-left: 30px; font-family: sans-serif; }}
    
    .grid-autos {{
        display: flex; flex-wrap: wrap; gap: 20px; padding: 20px; justify-content: center;
        font-family: sans-serif;
    }}
    .tarjeta {{
        background: white; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        padding: 20px; width: 300px; text-align: center;
    }}
    .img-car {{ width: 100%; border-radius: 10px; height: 200px; object-fit: cover; }}
    .precio {{ color: #e63946; font-size: 24px; font-weight: bold; margin: 10px 0; }}
    .btn {{
        display: block; padding: 12px; margin: 5px 0; border-radius: 8px;
        text-decoration: none; font-weight: bold; color: white !important;
    }}
</style>

<div class="header-azul">
    <img src="{logo_url}" class="logo-img">
    <div class="header-texto">
        <h1 style="margin:0; font-size: 3em;">LITORAL AUTOMOTORES</h1>
        <p style="margin:5px 0; color: #a8dadc;">Expertos en <b>CONSIGNACIONES</b>. Paysandú, Uruguay.</p>
    </div>
</div>

<div class="grid-autos">
    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3>VW Saveiro (2011)</h3>
        <img src="{f_sav}" class="img-car">
        <div class="precio">USD 8.000</div>
        <p>Motor 1.6 | Cabina Extendida</p>
        <a href="https://wa.me/59899417716?text=Saveiro" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Saveiro" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3>Suzuki Vitara (2016)</h3>
        <img src="{f_vit}" class="img-car">
        <div class="precio">USD 14.800</div>
        <p>150k km | Impecable estado</p>
        <a href="https://wa.me/59899417716?text=Vitara" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Vitara" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3>SMA C81 (2009)</h3>
        <img src="{f_sma}" class="img-car">
        <div class="precio">USD 3.500</div>
        <p>Motor 1.8 | Full Full</p>
        <a href="https://wa.me/59899417716?text=SMA" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=SMA" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3>Hyundai Accent (95)</h3>
        <img src="{f_hyu}" class="img-car">
        <div class="precio">¡CONSULTE!</div>
        <p>Muy económico | Al día</p>
        <a href="https://wa.me/59899417716?text=Hyundai" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Hyundai" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>
</div>
"""

# ESTA ES LA ÚNICA FORMA DE QUE SE VEA EL DISEÑO
st.write(html_final, unsafe_allow_html=True)
