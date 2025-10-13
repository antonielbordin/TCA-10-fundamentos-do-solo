import folium

def generate_map():
    # Cria o mapa centralizado no Oeste do Paraná
    maps = folium.Map(location=[-24.5, -53.5], zoom_start=6, tiles="OpenStreetMap")

    # Exemplo de solos com origem em diferentes materiais
    soils = [
        {
            "nome": "Latossolo Vermelho",
            "origem": "Rochas basálticas (vulcânicas)",
            "local": [-24.55, -53.50]
        },
        {
            "nome": "Argissolo Vermelho-Amarelo",
            "origem": "Arenito Caiuá",
            "local": [-24.75, -52.90]
        },
        {
            "nome": "Neossolo Quartzarênico",
            "origem": "Sedimentos arenosos recentes",
            "local": [-25.10, -54.20]
        }
    ]

    # Adiciona marcadores ao mapa
    for soil in soils:
        folium.Marker(
            location=soil["local"],
            popup=f"<b>{soil['nome']}</b><br>Origem: {soil['origem']}",
            icon=folium.Icon(color="green", icon="leaf")
        ).add_to(maps)

    maps.save("map_soils.html")
    return maps
