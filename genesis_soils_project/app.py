from flask import Flask, render_template
from maps_soils import generate_map

app = Flask(__name__)

@app.route("/")
def index():
    generate_map()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8050)
