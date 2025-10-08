import os


app = Flask(__name__)

@app.route('/')
def home():
    return ("<h1>Materia: DevOps</h1>"
            "<p>Profesor: Nombre del Profesor</p>"
            "<p>Alumno: Tu Nombre</p>")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
