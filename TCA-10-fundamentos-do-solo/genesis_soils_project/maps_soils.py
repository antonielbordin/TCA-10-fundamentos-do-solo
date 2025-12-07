from scipy.spatial import Delaunay
import numpy as np
import folium, json, html as htmlmod

def generate_map():
  with open("./data/soils.json", "r", encoding="utf-8") as f:
    soils = json.load(f)

  # Extract coordinates (lat, lon)
  points = np.array([s["coords"] for s in soils])

  # Calculates centroid (average of coordinates)
  center_lat, center_lon = np.mean(points, axis=0)

  # Centralized in Paraná where the triangulation
  m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=6,
    max_bounds=True,
    tiles="OpenStreetMap"
  )

  # Creates Delaunay triangulation
  tri = Delaunay(points)

  # Add each triangle to the map
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

  # Add bookmarks with interactive popup
  for s in soils:
    lat, lon = s["coords"]

    # Get summary and technique with fallback
    description = s.get("description", {})

    # If description is string (legacy), then summary = description
    if isinstance(description, str):
      summary = description
      technical = ""
    else:
      summary = description.get("summary", "")
      technical = description.get("technical", "")

    # Escapes text to avoid problems with 
    name_esc = htmlmod.escape(s.get("name", ""))
    summary_esc = htmlmod.escape(summary).replace("\n", "<br/>")
    technical_esc = htmlmod.escape(technical).replace("\n", "<br/>")
    img_src = s.get("img_solo", "")
    mother_rock = s.get("mother_rock")

    # Unique ids for the popup button/div — use the id provided in the JSON
    safe_id = htmlmod.escape(s.get("id", f"p{lat}_{lon}")).replace(" ", "_")

    # HTML of the popup with "More details" button that shows/hides the technical description
    html = f"""
    <div style='width:480px; font-family: sans-serif;'>
      <h4 style='margin:0 0 6px 0;'>{name_esc}</h4>
      <div style='display:flex; gap:10px;'>
        <div style='flex:0 0 40%;'>
          <img src="{img_src}" alt="{name_esc}" style='width:100%; border-radius:6px;'/>
        </div>
        <div style='flex:1; font-size:13px; text-align:justify;'>
          <div style='margin-bottom:6px;'>{summary_esc}</div>
          <button id="btn-{safe_id}" onclick="(function(btnId, divId){{
              var d=document.getElementById(divId);
              var b=document.getElementById(btnId);
              if(!d || !b) return;
              if(d.style.display === 'none' || d.style.display === ''){{ d.style.display='block'; b.textContent='Mostrar menos'; }}
              else {{ d.style.display='none'; b.textContent='Mais detalhes'; }}
          }})('btn-{safe_id}','div-{safe_id}')" style="cursor:pointer; padding:6px 8px; font-size:12px;">Mais detalhes</button>
          <div id="div-{safe_id}" style="display:none; margin-top:8px; border-top:1px solid #eee; padding-top:8px; font-size:13px; color:#333;">
            <p>{technical_esc}</p>
            <p><b>Rocha Mãe</b>: {mother_rock}</p>
          </div>
        </div>
      </div>
    </div>
    """

    iframe = folium.IFrame(html=html, width=500, height=300)
    popup = folium.Popup(iframe, max_width=520)

    # Decorative circle
    folium.Circle(
      location=[lat, lon],
      radius=1500,
      color="blue",
      fill=True,
      fill_opacity=0.2
    ).add_to(m)

    # Main marker (pin) with popup
    folium.Marker(
      location=[lat, lon],
      tooltip=s.get("name", ""),
      popup=popup,
      icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

  # Automatic framing adjustment (zoom and position)
  min_lat, min_lon = np.min(points, axis=0)
  max_lat, max_lon = np.max(points, axis=0)
  m.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])

  # Save the map
  m.save("static/map.html")
  return "Mapa gerado com sucesso!"