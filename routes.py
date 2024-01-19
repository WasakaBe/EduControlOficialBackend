from database import db, TBL_USERS, TBL_ROLS_USER, TBL_SEXS, TBL_PARENTAL
from flask import Blueprint, jsonify, request
from flask import session
import secrets
# Crear un blueprint para las rutas
user_routes = Blueprint('user_routes', __name__)
# Ruta para obtener todos los usuarios
@user_routes.route('/users/view', methods=['GET'])
def get_all_users():
    users = TBL_USERS.query.all()
    result = []
    for tbl_users in users:
        result.append({
            'id_users': tbl_users.id_users,
            'name_users': tbl_users.name_users,
            'app_users': tbl_users.app_users,
            'apm_users': tbl_users.apm_users,
            'age_users': tbl_users.age_users,
            'fecha_nacimiento_users': str(tbl_users.fecha_nacimiento_users),
            'correo_users': tbl_users.correo_users,
            'pwd_users': tbl_users.pwd_users,
            'foto_users': tbl_users.foto_users.decode('utf-8') if tbl_users.foto_users else None,
            'no_control_users': tbl_users.no_control_users,
            'phone_users': tbl_users.phone_users,
            'seguro_social_users': tbl_users.seguro_social_users,
            'curp_users': tbl_users.curp_users,
            'idRol': tbl_users.idRol,
            'idSexo': tbl_users.idSexo,
            'idParental': tbl_users.idParental
        })
    return jsonify({'users': result})
  # Ruta para obtener un usuario por ID
@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    tbl_users = TBL_USERS.query.get(user_id)
    if tbl_users:
        result = {
            'id_users': tbl_users.id_users,
            'name_users': tbl_users.name_users,
            'app_users': tbl_users.app_users,
            'apm_users': tbl_users.apm_users,
            'age_users': tbl_users.age_users,
            'fecha_nacimiento_users': str(tbl_users.fecha_nacimiento_users),
            'correo_users': tbl_users.correo_users,
            'pwd_users': tbl_users.pwd_users,
            'foto_users': tbl_users.foto_users.decode('utf-8') if tbl_users.foto_users else None,
            'no_control_users': tbl_users.no_control_users,
            'phone_users': tbl_users.phone_users,
            'seguro_social_users': tbl_users.seguro_social_users,
            'curp_users': tbl_users.curp_users,
            'idRol': tbl_users.idRol,
            'idSexo': tbl_users.idSexo,
            'idParental': tbl_users.idParental
        }
        return jsonify({'tbl_users': result})
    return jsonify({'message': 'Usuario no encontrado'}), 404
# Ruta para crear un nuevo usuario
@user_routes.route('/users/insert', methods=['POST'])
def create_user():
    data = request.json
    new_user = TBL_USERS(
        name_users=data['name_users'],
        app_users=data['app_users'],
        apm_users=data.get('apm_users'),
        age_users=data.get('age_users'),
        fecha_nacimiento_users=data.get('fecha_nacimiento_users'),
        correo_users=data['correo_users'],
        pwd_users=data['pwd_users'],
        foto_users=data.get('foto_users').encode('utf-8') if data.get('foto_users') else None,
        no_control_users=data['no_control_users'],
        phone_users=data.get('phone_users'),
        seguro_social_users=data.get('seguro_social_users'),
        curp_users=data.get('curp_users'),
        idRol=data['idRol'],
        idSexo=data['idSexo'],
        idParental=data['idParental']
    )
    db.session.add(new_user)
    db.session.commit()
    print(f"Nuevo usuario: {request.json['name_users']}")
    return jsonify({'message': 'Usuario creado exitosamente'}), 201
      
# Ruta para actualizar un usuario por ID
@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    tbl_users = TBL_USERS.query.get(user_id)
    if tbl_users:
        data = request.json
        tbl_users.name_users = data['name_users']
        tbl_users.app_users = data['app_users']
        tbl_users.apm_users = data.get('apm_users')
        tbl_users.age_users = data.get('age_users')
        tbl_users.fecha_nacimiento_users = data.get('fecha_nacimiento_users')
        tbl_users.correo_users = data['correo_users']
        tbl_users.pwd_users = data['pwd_users']
        tbl_users.foto_users = data.get('foto_users').encode('utf-8') if data.get('foto_users') else None
        tbl_users.no_control_users = data['no_control_users']
        tbl_users.phone_users = data.get('phone_users')
        tbl_users.seguro_social_users = data.get('seguro_social_users')
        tbl_users.curp_users = data.get('curp_users')
        tbl_users.idRol = data['idRol']
        tbl_users.idSexo = data['idSexo']
        tbl_users.idParental = data['idParental']
        db.session.commit()
        return jsonify({'message': 'Usuario actualizado exitosamente'})
    return jsonify({'message': 'Usuario no encontrado'}), 404

# Ruta para eliminar un usuario por ID
@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    tbl_users = TBL_USERS.query.get(user_id)
    if tbl_users:
        db.session.delete(tbl_users)
        db.session.commit()
        print(f"Elimino usuario: {request.json['name_users']}")
        return jsonify({'message': 'Usuario eliminado exitosamente'})
    return jsonify({'message': 'Usuario no encontrado'}), 404

# Ruta para el proceso de inicio de sesión
@user_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    tbl_users = TBL_USERS.query.filter_by(correo_users=data['correo_users'], pwd_users=data['pwd_users']).first()
    if tbl_users:
        result = {
            'id_users': tbl_users.id_users,
            'name_users': tbl_users.name_users,
            'app_users': tbl_users.app_users,
            'apm_users': tbl_users.apm_users,
            'age_users': tbl_users.age_users,
            'fecha_nacimiento_users': str(tbl_users.fecha_nacimiento_users),
            'correo_users': tbl_users.correo_users,
            'pwd_users': tbl_users.pwd_users,
            'foto_users': tbl_users.foto_users.decode('utf-8') if tbl_users.foto_users else None,
            'no_control_users': tbl_users.no_control_users,
            'phone_users': tbl_users.phone_users,
            'seguro_social_users': tbl_users.seguro_social_users,
            'curp_users': tbl_users.curp_users,
            'idRol': tbl_users.idRol,
            'idSexo': tbl_users.idSexo,
            'idParental': tbl_users.idParental
        }
        return jsonify({'tbl_users': result})
    return jsonify({'message': 'Credenciales incorrectas'}), 401

# Ruta para obtener todos los roles de usuario
@user_routes.route('/rols_user/view', methods=['GET'])
def get_all_rols_user():
    rols_user = TBL_ROLS_USER.query.all()
    result = []
    for rol_user in rols_user:
        result.append({
            'id_rols_user': rol_user.id_rols_user,
            'name_rols_user': rol_user.name_rols_user,
        })
    return jsonify({'rols_user': result})
# Ruta para obtener un rol de usuario por ID
@user_routes.route('/rols_user/<int:rol_user_id>', methods=['GET'])
def get_rol_user_by_id(rol_user_id):
    rol_user = TBL_ROLS_USER.query.get(rol_user_id)
    if rol_user:
        result = {
            'id_rols_user': rol_user.id_rols_user,
            'name_rols_user': rol_user.name_rols_user,
        }
        return jsonify({'rols_user': result})
    return jsonify({'message': 'Rol de usuario no encontrado'}), 404

# Ruta para verificar la disponibilidad del correo
@user_routes.route('/check-email', methods=['POST'])
def check_email_availability():
    try:
        data = request.json
        existing_user = TBL_USERS.query.filter_by(correo_users=data['correo_users']).first()
        if existing_user:
            return jsonify({'exists': True}), 200
        return jsonify({'exists': False}), 200
    except SQLAlchemyError as e:
        print('Error en la verificación de correo:', str(e))
        return jsonify({'error': 'Error en la verificación de correo'}), 500
    
# Ruta para recuperar contraseña por correo electrónico
@user_routes.route('/recover-password', methods=['POST'])
def recover_password():
    data = request.json
    user = TBL_USERS.query.filter_by(correo_users=data['correo_users']).first()
    if user:
        # Genera un token temporal para la recuperación de contraseña
        recovery_token = secrets.token_urlsafe(32)

        # Almacena el token en la sesión del usuario (en un entorno de producción, utiliza una solución más segura)
        session['recovery_token'] = recovery_token
        session['recovery_user_id'] = user.id_users

        # Devuelve un mensaje con el token (para fines de prueba)
        return jsonify({'message': 'Token de recuperación de contraseña generado:', 'recovery_token': recovery_token}), 200
    else:
        return jsonify({'message': 'Correo electrónico no encontrado'}), 404

# Ruta para cambiar la contraseña con el token temporal
@user_routes.route('/change-password', methods=['POST'])
def change_password():
    data = request.json
    user_id = session.get('recovery_user_id')
    recovery_token = session.get('recovery_token')

    if user_id and recovery_token and data.get('new_password') and data.get('token') == recovery_token:
        # Recupera el usuario y cambia la contraseña
        user = TBL_USERS.query.get(user_id)
        user.set_password(data['new_password'])
        db.session.commit()

        # Limpia la sesión después de cambiar la contraseña
        session.pop('recovery_user_id', None)
        session.pop('recovery_token', None)

        return jsonify({'message': 'Contraseña cambiada exitosamente'}), 200

    return jsonify({'message': 'Token no válido o información faltante'}), 400
@user_routes.route('/')
def hello_world():
    return 'API CORRIENDO EDU CONTROL CBTA5 2'
