#Código para arrancar el programa

from app import create_app
import webbrowser

app = create_app()

if __name__ == "__main__":
    webbrowser.open("http://localhost:5000")
    app.run(debug=True)