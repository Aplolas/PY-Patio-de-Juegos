from patio_de_juegos import app
from patio_de_juegos.controllers import controlers

(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

if __name__ == '__main__':
    app.run(debug= True)