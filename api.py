from flask import Flask, jsonify

app = Flask(__name__)

# Definir tus datos de ciudades aquí
ciudades_data = [
    {
        "id": 1, 
     "nombre": "EnsenadaMarketing", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://ensenadahoy.com/", 
     "descripcion": "Ciudad costera con hermosas playas y paisajes impresionantes."},

    {
        "id": 2, 
     "nombre": "TecateMarketing", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://tecatehoy.com/", 
     "descripcion": "Ciudad del pan"
     },

    {
        "id": 3, 
        "nombre": "TijuanaMarketing", 
        "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
        "redes": "https://tijuanahoy.com/", 
        "descripcion": "Ciudad del hongkong y de las desapariciones"
        },

    {
        "id": 4, 
     "nombre": "RosaritoMarketing", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://rosaritohoy.com/", 
     "descripcion": "Ciudad de langostas"},

    {
        "id": 5, 
     "nombre": "MexicaliMarketing", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://mexicalihoy.com/", 
     "descripcion": "Ciudad calurosa."},

    {
        "id": 6, 
     "nombre": "San QuintinMarketing", 
     "logo": "https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png", 
     "redes": "https://mexicalihoy.com/", 
     "descripcion": "Ciudad de las fresas"},
    # ... Agrega datos para otras ciudades aquí ...
]

@app.route('/ciudades', methods=['GET'])
def encontrar_ciudad_por_id(ciudad_id):
    for ciudad in ciudades_data:
        if ciudad["id"] == ciudad_id:
            return ciudad
    return None  # Devuelve None si la ciudad con el ID dado no se encuentra

@app.route('/ciudades/<int:ciudad_id>', methods=['GET'])
def obtener_ciudad(ciudad_id):
    # Encuentra los detalles de la ciudad en base al ID proporcionado
    ciudad = encontrar_ciudad_por_id(ciudad_id)
    if ciudad is None:
        return jsonify({"error": "Ciudad no encontrada"}), 404
    return jsonify(ciudad)

if __name__ == '__main__':
    app.run(debug=True)