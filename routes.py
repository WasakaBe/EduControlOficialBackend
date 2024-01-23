from database import db, TBL_USERS, TBL_ROLS_USER, TBL_SEXS, TBL_PARENTAL
from flask import Blueprint, jsonify, request


# Crear un blueprint para las rutas
user_routes = Blueprint('user_routes', __name__)
#---------------------------------------------------------USUARIOS
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
            'token_users': tbl_users.token_users,
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
            'token_users': tbl_users.token_users,
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
    # Crear el nuevo usuario con el token generado
    new_user = TBL_USERS(
        name_users=data['name_users'],
        app_users=data['app_users'],
        apm_users=data.get('apm_users'),
        age_users=data.get('age_users'),
         token_users=data.get('token_users'),
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

    # Agregar el nuevo usuario a la sesión y confirmar la transacción
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
        tbl_users.token_users = data.get('token_users')
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
            'token_users':tbl_users.token_users,
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

# Ruta para obtener el token a partir del correo
@user_routes.route('/get-token', methods=['POST'])
def get_token_by_email():
    data = request.json
    tbl_users = TBL_USERS.query.filter_by(correo_users=data['correo_users']).first()
    if tbl_users:
        return jsonify({'token_users': tbl_users.token_users}), 200
    return jsonify({'message': 'Correo no encontrado'}), 404

@user_routes.route('/verify-token/<string:user_token>', methods=['GET'])
def verify_token(user_token):
    # Busca un usuario con el token proporcionado
    tbl_users = TBL_USERS.query.filter_by(token_users=user_token).first()

    # Verifica si se encontró un usuario con el token
    if tbl_users:
        return jsonify({'message': 'Token válido'}), 200
    else:
        return jsonify({'message': 'Token inválido'}), 401

# Ruta para actualizar la contraseña de un usuario por correo electrónico
@user_routes.route('/updates-password', methods=['POST'])
def updates_password():
    try:
        data = request.json
        correo = data.get('correo_users')
        new_password = data.get('new_password')

        # Buscar al usuario por correo electrónico
        tbl_users = TBL_USERS.query.filter_by(correo_users=correo).first()

        if tbl_users:
            # Actualizar la contraseña
            tbl_users.pwd_users = new_password
            db.session.commit()
            return jsonify({'message': 'Contraseña actualizada exitosamente'}), 200
        else:
            return jsonify({'message': 'Usuario no encontrado'}), 404

    except SQLAlchemyError as e:
        print('Error al actualizar la contraseña:', str(e))
        return jsonify({'error': 'Error al actualizar la contraseña'}), 500

#--------------------------------------------------------- SEXO
# Ruta para obtener todos los sexos
@user_routes.route('/sexs', methods=['GET'])
def get_all_sexs():
    sexs = TBL_SEXS.query.all()
    result = [{'id_sexs': sex.id_sexs, 'name_sexs': sex.name_sexs} for sex in sexs]
    return jsonify({'sexs': result})

# Ruta para obtener un sexo por ID
@user_routes.route('/sexs/<int:sex_id>', methods=['GET'])
def get_sex_by_id(sex_id):
    sex = TBL_SEXS.query.get(sex_id)
    if sex:
        result = {'id_sexs': sex.id_sexs, 'name_sexs': sex.name_sexs}
        return jsonify({'sex': result})
    return jsonify({'message': 'Sexo no encontrado'}), 404

# Ruta para crear un nuevo sexo
@user_routes.route('/sexs/insert', methods=['POST'])
def create_sex():
    data = request.json
    new_sex = TBL_SEXS(name_sexs=data['name_sexs'])
    db.session.add(new_sex)
    db.session.commit()
    print(f"Nuevo sexo: {request.json['name_sexs']}")
    return jsonify({'message': 'Sexo creado exitosamente'}), 201

# Ruta para actualizar un sexo por ID
@user_routes.route('/sexs/<int:sex_id>', methods=['PUT'])
def update_sex(sex_id):
    sex = TBL_SEXS.query.get(sex_id)
    if sex:
        data = request.json
        sex.name_sexs = data['name_sexs']
        db.session.commit()
        return jsonify({'message': 'Sexo actualizado exitosamente'})
    return jsonify({'message': 'Sexo no encontrado'}), 404

# Ruta para eliminar un sexo por ID
@user_routes.route('/sexs/<int:sex_id>', methods=['DELETE'])
def delete_sex(sex_id):
    sex = TBL_SEXS.query.get(sex_id)
    if sex:
        db.session.delete(sex)
        db.session.commit()
        print(f"Elimino sexo: {request.json['name_sexs']}")
        return jsonify({'message': 'Sexo eliminado exitosamente'})
    return jsonify({'message': 'Sexo no encontrado'}), 404
#--------------------------------------------------------- TBL PARENTAL
# Ruta para obtener todos los registros de TBL_PARENTAL
@user_routes.route('/parentals', methods=['GET'])
def get_all_parentals():
    parentals = TBL_PARENTAL.query.all()
    result = [{'id_parental': parental.id_parental, 'name_parental': parental.name_parental} for parental in parentals]
    return jsonify({'parentals': result})

# Ruta para obtener un registro de TBL_PARENTAL por ID
@user_routes.route('/parentals/<int:parental_id>', methods=['GET'])
def get_parental_by_id(parental_id):
    parental = TBL_PARENTAL.query.get(parental_id)
    if parental:
        result = {'id_parental': parental.id_parental, 'name_parental': parental.name_parental}
        return jsonify({'parental': result})
    return jsonify({'message': 'Registro parental no encontrado'}), 404

# Ruta para crear un nuevo registro en TBL_PARENTAL
@user_routes.route('/parentals/insert', methods=['POST'])
def create_parental():
    data = request.json
    new_parental = TBL_PARENTAL(name_parental=data['name_parental'])
    db.session.add(new_parental)
    db.session.commit()
    print(f"Nuevo registro parental: {request.json['name_parental']}")
    return jsonify({'message': 'Registro parental creado exitosamente'}), 201

# Ruta para actualizar un registro en TBL_PARENTAL por ID
@user_routes.route('/parentals/<int:parental_id>', methods=['PUT'])
def update_parental(parental_id):
    parental = TBL_PARENTAL.query.get(parental_id)
    if parental:
        data = request.json
        parental.name_parental = data['name_parental']
        db.session.commit()
        return jsonify({'message': 'Registro parental actualizado exitosamente'})
    return jsonify({'message': 'Registro parental no encontrado'}), 404

# Ruta para eliminar un registro en TBL_PARENTAL por ID
@user_routes.route('/parentals/<int:parental_id>', methods=['DELETE'])
def delete_parental(parental_id):
    parental = TBL_PARENTAL.query.get(parental_id)
    if parental:
        db.session.delete(parental)
        db.session.commit()
        print(f"Eliminado registro parental: {request.json['name_parental']}")
        return jsonify({'message': 'Registro parental eliminado exitosamente'})
    return jsonify({'message': 'Registro parental no encontrado'}), 404

#--------------------------------------------------------- TIPOS DE USUARIOS
# Ruta para obtener todos los roles de usuario
@user_routes.route('/roles', methods=['GET'])
def get_all_roles():
    roles = TBL_ROLS_USER.query.all()
    result = [{'id_rols_user': rol.id_rols_user, 'name_rols_user': rol.name_rols_user} for rol in roles]
    return jsonify({'roles': result})

# Ruta para obtener un rol de usuario por ID
@user_routes.route('/roles/<int:rol_id>', methods=['GET'])
def get_role_by_id(rol_id):
    rol = TBL_ROLS_USER.query.get(rol_id)
    if rol:
        result = {'id_rols_user': rol.id_rols_user, 'name_rols_user': rol.name_rols_user}
        return jsonify({'rol': result})
    return jsonify({'message': 'Rol de usuario no encontrado'}), 404

# Ruta para crear un nuevo rol de usuario
@user_routes.route('/roles/insert', methods=['POST'])
def create_role():
    data = request.json
    new_role = TBL_ROLS_USER(name_rols_user=data['name_rols_user'])
    db.session.add(new_role)
    db.session.commit()
    print(f"Nuevo rol de usuario: {request.json['name_rols_user']}")
    return jsonify({'message': 'Rol de usuario creado exitosamente'}), 201

# Ruta para actualizar un rol de usuario por ID
@user_routes.route('/roles/<int:rol_id>', methods=['PUT'])
def update_role(rol_id):
    rol = TBL_ROLS_USER.query.get(rol_id)
    if rol:
        data = request.json
        rol.name_rols_user = data['name_rols_user']
        db.session.commit()
        return jsonify({'message': 'Rol de usuario actualizado exitosamente'})
    return jsonify({'message': 'Rol de usuario no encontrado'}), 404

# Ruta para eliminar un rol de usuario por ID
@user_routes.route('/roles/<int:rol_id>', methods=['DELETE'])
def delete_role(rol_id):
    rol = TBL_ROLS_USER.query.get(rol_id)
    if rol:
        db.session.delete(rol)
        db.session.commit()
        print(f"Eliminado rol de usuario: {request.json['name_rols_user']}")
        return jsonify({'message': 'Rol de usuario eliminado exitosamente'})
    return jsonify({'message': 'Rol de usuario no encontrado'}), 404

@user_routes.route('/')
def hello_world():
    return 'API CORRIENDO EDU CONTROL CBTA5 3'
