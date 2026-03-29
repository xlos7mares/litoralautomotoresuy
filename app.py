import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Litoral Automotores", page_icon="🚗", layout="wide")

# 2. Definición del Contenido HTML
# He corregido el link del Hyundai y asegurado los demás
html_contenido = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; }
    .header-azul {
        background-color: #1d3557; color: white; padding: 40px;
        display: flex; align-items: center; border-radius: 0 0 30px 30px;
    }
    .logo-img { width: 180px; height: 180px; border-radius: 50%; border: 4px solid white; object-fit: cover; }
    .header-texto { margin-left: 30px; }
    .grid-autos {
        display: flex; flex-wrap: wrap; gap: 25px; padding: 30px; justify-content: center;
    }
    .tarjeta {
        background: white; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        padding: 20px; width: 300px; text-align: center;
    }
    .img-car { width: 100%; border-radius: 10px; height: 200px; object-fit: cover; background: #eee; }
    .precio { color: #e63946; font-size: 24px; font-weight: bold; margin: 15px 0; }
    .btn {
        display: block; padding: 12px; margin: 8px 0; border-radius: 8px;
        text-decoration: none; font-weight: bold; color: white !important; text-align: center;
    }
</style>
</head>
<body>

<div class="header-azul">
    <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/601396473_3654982237974663_5290087789832669203_n.jpg" class="logo-img">
    <div class="header-texto">
        <h1 style="margin:0; font-size: 3em;">LITORAL AUTOMOTORES</h1>
        <p style="margin:5px 0; color: #a8dadc; font-size: 1.2em;">Especialistas en <b>CONSIGNACIONES</b>. Paysandú, Uruguay.</p>
    </div>
</div>

<div class="grid-autos">
    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3 style="margin: 10px 0;">VW Saveiro (2011)</h3>
        <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/savblack1.jpg" class="img-car">
        <div class="precio">USD 8.000</div>
        <p>Motor 1.6 | Cabina Extendida</p>
        <a href="https://wa.me/59899417716?text=Interes-Saveiro" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Interes-Saveiro" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3 style="margin: 10px 0;">Suzuki Vitara (2016)</h3>
        <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/suzukivitara13.jpg" class="img-car">
        <div class="precio">USD 14.800</div>
        <p>150k km | Impecable estado</p>
        <a href="https://wa.me/59899417716?text=Interes-Vitara" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Interes-Vitara" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3 style="margin: 10px 0;">SMA C81 (2009)</h3>
        <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/655872262_3758670767605809_6449769683858621609_n.jpg" class="img-car">
        <div class="precio">USD 3.500</div>
        <p>Motor 1.8 | Full Full</p>
        <a href="https://wa.me/59899417716?text=Interes-SMA" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Interes-SMA" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>

    <div class="tarjeta">
        <b style="color: #28a745;">EN VENTA</b>
        <h3 style="margin: 10px 0;">Hyundai Accent (95)</h3>
        <img src="https://raw.githubusercontent.com/xlos7mares/litoralautomotoresuy/main/656015569_1109062323719001_1833132791485600122_n.jpg" class="img-car">
        <div class="precio">¡CONSULTE!</div>
        <p>Muy económico | Al día</p>
        <a href="https://wa.me/59899417716?text=Interes-Hyundai" class="btn" style="background:#007bff;">CONSULTAR</a>
        <a href="https://wa.me/59899417716?text=Interes-Hyundai" class="btn" style="background:#dc3545;">ME INTERESA</a>
    </div>
</div>

<p style="text-align: center; color: #888; font-family: sans-serif; padding: 20px;">© 2026 Litoral Automotores | Paysandú, Uruguay</p>

</body>
</html>
"""

# 3. Lanzamiento final
st.components.v1.html(html_contenido, height=1500, scrolling=True)
