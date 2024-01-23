from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class TBL_USERS(db.Model):
    id_users = db.Column(db.Integer, primary_key=True)
    name_users = db.Column(db.String(255), nullable=False)
    app_users = db.Column(db.String(255), nullable=False)
    apm_users = db.Column(db.String(255))
    age_users = db.Column(db.Integer)
    token_users = db.Column(db.String(20))
    correo_users = db.Column(db.String(255), unique=True, nullable=False)
    pwd_users = db.Column(db.String(255), nullable=False)
    foto_users = db.Column(db.LargeBinary)
    no_control_users = db.Column(db.BigInteger, unique=True)
    phone_users = db.Column(db.BigInteger)
    seguro_social_users = db.Column(db.BigInteger)
    curp_users = db.Column(db.String(18), unique=True)
    idRol = db.Column(db.Integer)
    idSexo = db.Column(db.Integer)
    idParental = db.Column(db.Integer)
class TBL_ROLS_USER(db.Model):
    id_rols_user = db.Column(db.Integer, primary_key=True)
    name_rols_user = db.Column(db.String(255), nullable=False)
class TBL_SEXS(db.Model):
    id_sexs = db.Column(db.Integer, primary_key=True)
    name_sexs = db.Column(db.String(10))

class TBL_PARENTAL(db.Model):
    id_parental = db.Column(db.Integer, primary_key=True)
    name_parental = db.Column(db.String(30))
