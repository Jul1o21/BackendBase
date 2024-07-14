from src import init_app
from src.database.db import db
from flask_cors import CORS

app = init_app()

db.init_app(app)

app.app_context().push()

CORS(app)

if __name__ == '__main__':
    app.run(debug = True)