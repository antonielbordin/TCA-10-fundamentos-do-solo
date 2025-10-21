# 🌱 Interactive Pedological Map - Western Paraná

An open-source project for interactive visualization of soil distribution in the Western region of Paraná, Brazil, developed with Python, Flask, and Folium.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)

## 📋 About the Project

This project presents an interactive map that displays the spatial distribution of main soil types in Western Paraná, based on pedological data from Embrapa and other research institutions. The application uses Delaunay triangulation to represent study and sampling areas, providing a georeferenced view of the region's pedological characteristics.

### 🎯 Objectives

- Visualize spatial distribution of soils in Western Paraná
- Provide technical information about each soil type
- Facilitate the study of soil genesis and classification
- Serve as an educational tool for students and professionals

## 🗂️ Project Structure

```
pedology-project/
├── app.py               # Main Flask application
├── maps_soils.py        # Interactive map generation
├── requirements.txt     # Project dependencies
├── data/
│   └── soils.json       # Soil data (coordinates, descriptions, images)
├── static/
│   └── map.html         # Automatically generated map
└── templates/
    └── index.html       # Main application template
```

## 🚀 Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/antonielbordin/TCA-10-fundamentos-do-solo
   cd TCA-10-fundamentos-do-solo/genesis_soils_project
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access in your browser**
   ```
   http://localhost:8050
   ```

## 📊 Dependencies

The project uses the following Python libraries:

- **Flask** (2.0+): Web framework for the application
- **Folium** (0.14+): Interactive map generation
- **SciPy** (1.7+): Scientific calculations and Delaunay triangulation
- **NumPy** (1.21+): Numerical array manipulation

## 🗺️ Features

### Interactive Map
- **Spatial visualization** of sampling points
- **Delaunay triangulation** for area representation
- **Intuitive zoom and navigation**
- **Automatic bounds** based on coordinates

### Informative Popups
- **Soil profile images**
- **Summary and technical description**
- **Parent rock and source material**
- **Official bibliographic references**
- **Interactive button** for more details

### Included Soil Types
- Red Latosols (Latossolos Vermelhos)
- Red and Red-Yellow Argisols (Argissolos)
- Quartzipsamments (Neossolos Quartzarênicos)
- Haplustepts (Cambissolos Háplicos)
- Gleysols (Gleissolos)
- Planosols (Planossolos)
- Red Nitosols (Nitossolos Vermelhos)

## 🔧 Data Structure

The `data/soils.json` file contains the complete data structure:

```json
{
  "id": "unique_identifier",
  "name": "Soil Name - City",
  "coords": [latitude, longitude],
  "img_solo": "image_URL",
  "description": {
    "summary": "Summary description",
    "technical": "Detailed technical description"
  },
  "mother_rock": "Parent rock",
  "reference": [
    {
      "title": "Reference title",
      "url": "Reference URL"
    }
  ],
  "note": "Additional observations"
}
```

## 📚 Data Sources

### Official Institutions
- **Embrapa Soils**: Technical classification and images
- **IAPAR**: Regional data from Paraná
- **SEAB/DERAL**: Agricultural zoning
- **CPRM**: Geological data

### Scientific References
- Brazilian Soil Classification System (SiBCS)
- Paraná Soil Atlas
- Embrapa technical publications
- Peer-reviewed scientific articles

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Authors

- **Antoniel Bordin** - *Initial development* - [antonielbordin](https://github.com/antonielbordin)

---

**Developed with ❤️ for the scientific and educational community**