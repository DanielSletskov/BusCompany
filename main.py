from app.ui import run_ui
from api.Flask import app as flask_app

if __name__ == "__main__":
    flask_app.run(debug=True, use_reloader=False) 
    run_ui()
