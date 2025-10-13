from dash import Dash, html, dcc, Input, Output
import os
from maps_soils import generate_map

# Gera o mapa (só uma vez)
if not os.path.exists("map_soils.html"):
    generate_map()

app = Dash(__name__)
app.title = "Gênese dos Solos - Interativo 🌱"

# Layout da aplicação
app.layout = html.Div([
    html.H1("Gênese dos Solos - Mapa e Jogo Interativo", style={'textAlign': 'center'}),
    html.Hr(),

    html.H2("🗺️ Mapa Interativo dos Solos", style={'marginTop': '20px'}),
    html.Iframe(srcDoc=open('mapa_solos.html', 'r').read(),
                width='100%', height='500', style={'border': '2px solid #ccc'}),

    html.H2("🎮 Explore os Fatores de Formação dos Solos", style={'marginTop': '40px'}),
    html.P("Selecione um fator pedogenético para responder:", style={'fontSize': '18px'}),

    dcc.Dropdown(
        id="fator",
        options=[
            {"label": "Clima", "value": "clima"},
            {"label": "Organismos", "value": "organismos"},
            {"label": "Relevo", "value": "relevo"},
            {"label": "Tempo", "value": "tempo"},
            {"label": "Material de Origem", "value": "material"}
        ],
        placeholder="Escolha um fator para iniciar...",
        style={'width': '60%', 'margin': 'auto'}
    ),

    html.Div(id="quiz", style={'marginTop': '30px', 'textAlign': 'center', 'fontSize': '18px'}),
    html.Div(id="feedback", style={'marginTop': '20px', 'fontWeight': 'bold', 'fontSize': '20px', 'color': 'green'})
])

# Questões
quiz_data = {
    "clima": {
        "pergunta": "Como o clima influencia a formação do solo?",
        "opcoes": [
            "A) Aumenta a erosão e a lixiviação dos nutrientes.",
            "B) Não tem influência.",
            "C) Torna o solo mais impermeável."
        ],
        "resposta": "A"
    },
    "organismos": {
        "pergunta": "Qual o papel dos organismos na gênese do solo?",
        "opcoes": [
            "A) Compactam o solo, dificultando infiltração.",
            "B) Adicionam matéria orgânica e aceleram a decomposição.",
            "C) Reduzem a fertilidade natural."
        ],
        "resposta": "B"
    },
    "relevo": {
        "pergunta": "Como o relevo interfere na gênese dos solos?",
        "opcoes": [
            "A) Relevos planos acumulam materiais e favorecem solos mais profundos.",
            "B) Relevos íngremes formam solos mais espessos.",
            "C) O relevo não afeta o desenvolvimento do solo."
        ],
        "resposta": "A"
    },
    "tempo": {
        "pergunta": "Por que o tempo é um fator importante na formação dos solos?",
        "opcoes": [
            "A) Quanto mais tempo, mais desenvolvido e espesso o solo tende a ser.",
            "B) Solos antigos são sempre inférteis.",
            "C) O tempo não tem influência direta."
        ],
        "resposta": "A"
    },
    "material": {
        "pergunta": "O que caracteriza o material de origem do solo?",
        "opcoes": [
            "A) Rochas e sedimentos que deram origem ao solo.",
            "B) A quantidade de água presente no perfil.",
            "C) A matéria orgânica do horizonte superficial."
        ],
        "resposta": "A"
    }
}

# Callback para mostrar quiz
@app.callback(
    Output("quiz", "children"),
    Input("fator", "value")
)
def mostrar_quiz(fator):
    if not fator:
        return "Escolha um fator para começar o quiz."

    q = quiz_data[fator]
    return html.Div([
        html.H3(q["pergunta"]),
        html.Div([
            html.Button(opcao, id={'type': 'resposta', 'index': i}, n_clicks=0,
                        style={'margin': '5px', 'padding': '10px', 'fontSize': '16px'})
            for i, opcao in enumerate(q["opcoes"])
        ])
    ])


# Callback para verificar resposta (usando padrão de id dinâmico)
from dash.dependencies import ALL

@app.callback(
    Output("feedback", "children"),
    Input("fator", "value"),
    Input({'type': 'resposta', 'index': ALL}, 'n_clicks')
)
def verificar_resposta(fator, clicks):
    if not fator or not any(clicks):
        return ""

    idx = [i for i, c in enumerate(clicks) if c > 0]
    if not idx:
        return ""

    i = idx[-1]  # última clicada
    letra_clicada = ["A", "B", "C"][i]
    correta = quiz_data[fator]["resposta"]

    if letra_clicada == correta:
        return "✅ Resposta correta! Muito bem!"
    else:
        return "❌ Resposta incorreta. Tente novamente!"

if __name__ == "__main__":
    app.run(debug=True)

