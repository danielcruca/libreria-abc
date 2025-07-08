from app import create_app

app = create_app()
# IMPORTANTE: recarga los cambios en el servidor
# Activa el modo debug.

if __name__ == "__main__":
    app.run(debug=True)
