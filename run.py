from app import create_app
from app.db import db_init
from config import Config

app = create_app()

if __name__ == "__main__":
    db_init()
    app.run(debug=Config.DEBUG)