from flask import Flask, jsonify

app = Flask(__name__)

# Definir tus datos de ciudades aquí
ciudades_data = [
    {"id": 1, 
     "nombre": "Ensenadaoficial", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://ensenadahoy.com/", 
     "descripcion": "Ciudad costera con hermosas playas y paisajes impresionantes."},

    {"id": 2, "nombre": "Tecate", "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", "redes": "https://ensenadahoy.com/", "descripcion": "Ciudad costera con hermosas playas y paisajes impresionantes."},

    {"id": 3, "nombre": "Tijuana", "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", "redes": "https://ensenadahoy.com/", "descripcion": "Ciudad costera con hermosas playas y paisajes impresionantes."},

    {"id": 4, 
     "nombre": "Rosarito", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://ensenadahoy.com/", 
     "descripcion": "Ciudad costera con hermosas playas y paisajes impresionantes."},

    {"id": 5, 
     "nombre": "Mexicali", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://ensenadahoy.com/", 
     "descripcion": "Ciudad costera con hermosas playas y paisajes impresionantes."},

    {"id": 6, 
     "nombre": "San Quintin", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://ensenadahoy.com/", 
     "descripcion": "Ciudad costera con hermosas playas y paisajes impresionantes."},
    # ... Agrega datos para otras ciudades aquí ...
]

@app.route('/ciudades', methods=['GET'])
def obtener_ciudades():
    return jsonify(ciudades_data)

if __name__ == '__main__':
    app.run(debug=True)
