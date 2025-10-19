# Old
# import folium
# import json

# new 
from scipy.spatial import Delaunay
import numpy as np
import folium, json

def generate_map_old():
    with open("./data/soils.json", "r", encoding="utf-8") as f:
        soils = json.load(f)

    # Mapa centralizado no Paraná
    map_center = [-24.0, -53.0]
    m = folium.Map(
        location=map_center,
        zoom_start=7,
        min_zoom=6,
        max_bounds=True,
        tiles="cartodb positron"
    )

    # Polígono da região Oeste do Paraná
    west_parana_coords = [
        [-23.0, -54.0],
        [-26.0, -54.0],
        [-26.0, -51.0],
        [-23.0, -51.0]
    ]
    folium.Polygon(
        locations=west_parana_coords,
        color="blue",
        weight=2,
        fill=True,
        fill_color="blue",
        fill_opacity=0.1,
        popup="Região Oeste do Paraná"
    ).add_to(m)

    # Função para filtrar solos na região Oeste
    def is_in_west_parana(lat, lon):
        return -26.0 <= lat <= -23.0 and -54.0 <= lon <= -51.0

    # Adiciona os marcadores dos solos apenas na região Oeste
    for s in soils:
        lat, lon = s["coords"]
        if is_in_west_parana(lat, lon):
            html = f"""
            <div style='width:420px;'>
              <h4 style='margin-bottom:6px; font-family:sans-serif;'>{s["name"]}</h4>
              <div style='display:flex; gap:10px;'>
                <div style='flex:0 0 45%;'>
                  <img src='{s["img"]}' alt='{s["name"]}' style='width:100%; border-radius:6px;'/>
                </div>
                <div style='flex:1; font-size:13px; text-align:justify;'>
                  {s["description"]}
                </div>
              </div>
            </div>
            """
            iframe = folium.IFrame(html=html, width=420, height=200)
            folium.Marker(
                location=[lat, lon],
                tooltip=s["name"],
                popup=folium.Popup(iframe)
            ).add_to(m)

    m.save("static/map.html")
    return "Mapa gerado com sucesso!"

def generate_map():
  with open("./data/soils.json", "r", encoding="utf-8") as f:
    soils = json.load(f)

  # Extrai coordenadas (lat, lon)
  points = np.array([s["coords"] for s in soils])

  # Calcula centroide (média das coordenadas)
  center_lat, center_lon = np.mean(points, axis=0)

  # Centraliza no Paraná onde a triangulação
  m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=7,
    min_zoom=6,
    max_bounds=True,
    tiles="OpenStreetMap"
  )

  # Cria triangulação Delaunay
  tri = Delaunay(points)

  # Adiciona cada triângulo ao mapa
  for simplex in tri.simplices:
    triangle = [points[i].tolist() for i in simplex]
    folium.Polygon(
      locations=triangle,
      color="orange",
      weight=2,
      fill=True,
      fill_color="orange",
      fill_opacity=0.2
    ).add_to(m)

  # Adiciona marcadores com popup interativo (como antes)
  for s in soils:
    lat, lon = s["coords"]
    html = f"""
    <div style='width:500px;'>
      <h4 style='margin-bottom:6px; font-family:sans-serif;'>{s["name"]}</h4>
      <div style='display:flex; gap:10px;'>
        <div style='flex:0 0 45%;'>
          <img src='{s["img"]}' alt='{s["name"]}' style='width:100%; border-radius:6px;'/>
        </div>
        <div style='flex:1; font-size:13px; text-align:justify; padding: 5px; background:magenta'>
          {s["description"]}
        </div>
      </div>
    </div>
    """
    iframe = folium.IFrame(html=html, width=500, height=300)
    popup = folium.Popup(iframe)

    # Círculo decorativo
    folium.Circle(
        location=[lat, lon],
        radius=1500,  # raio em metros
        color="blue",
        fill=True,
        fill_opacity=0.2
    ).add_to(m)

    # Cria marcador com ícone azul
    folium.Marker(
        location=[lat, lon],
        tooltip=s["name"],
        popup=popup,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

  # Ajuste automático de enquadramento (zoom e posição)
  min_lat, min_lon = np.min(points, axis=0)
  max_lat, max_lon = np.max(points, axis=0)
  m.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])

  m.save("static/map.html")
  return "Mapa gerado com sucesso!"
