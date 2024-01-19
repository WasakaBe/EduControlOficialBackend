from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db
from routes import user_routes
from waitress import serve
from sqlalchemy.exc import SQLAlchemyError
import secrets
app = Flask(__name__)
CORS(app)
app.secret_key = 'LaMisionEsNoRendirse1'
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/EDUCONTROLCBTA'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)
@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, SQLAlchemyError):
        return jsonify({'error': 'Error de la base de datos'}), 500
    return jsonify({'error': str(e)}), 500
# Registrar las rutas
app.register_blueprint(user_routes)

if __name__ == '__main__':
    serve(app,host='0.0.0.0', port=40009)
