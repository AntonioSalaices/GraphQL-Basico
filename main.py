from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_wtf import CSRFProtect
from flask import json, jsonify
from config import DevelopmentConfig
from models import db, Solicitud
import os
from flask_marshmallow import Marshmallow

app = Flask(__name__)


app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
ma = Marshmallow()

# Creación de Esquema
class SolicitudSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_empleado', 'sucursal','proveedor', 'insumo_nombre', 'descripcion', 'marca', 'cantidad_solicitada','cantidad_recibida', 'precio_unidad', 'estado_solicitud', 'total', 'observacion', 'fecha_emision')

# Inicializando esquema
solicitud_schema = SolicitudSchema()
solicitudes_schema = SolicitudSchema(many=True)


#Agregando una solicitud
@app.route('/agregar/solicitud/', methods=['POST'])
def post_solicitud():
    nombre_empleado = request.json['nombre_empleado']
    sucursal = request.json['sucursal']
    proveedor = request.json['proveedor']
    insumo_nombre = request.json['insumo_nombre']
    descripcion = request.json['descripcion']
    marca = request.json['marca']
    cantidad_solicitada = request.json['cantidad_solicitada']
    precio_unidad = request.json['precio_unidad']
    total = request.json['total']

    new_solicitud = Solicitud(nombre_empleado, sucursal, proveedor,insumo_nombre, descripcion, marca, cantidad_solicitada, precio_unidad, total)
    db.session.add(new_solicitud)
    db.session.commit()

    return solicitud_schema.jsonify(new_solicitud), 201

#Obteniendo todas las solicitudes
@app.route('/solicitudes', methods=['GET'])
def get_all_solicitudes():
    all_solicitudes = Solicitud.query.all()
    result = solicitudes_schema.dump(all_solicitudes)
    return jsonify(result)

# Obten solo una solicitud
@app.route('/solicitudes/<id>', methods=['GET'])
def get_solicitud(id):
    solicitud = Solicitud.query.get(id)
    return solicitud_schema.jsonify(solicitud),200

# Elimina una solicitud
@app.route('/solicitudes/<id>', methods=['DELETE'])
def delete_solicitud(id):
    solicitud = Solicitud.query.get(id)
    db.session.delete(solicitud)
    db.session.commit()
    return solicitud_schema.jsonify(solicitud),200

#Actualizar solicitud
@app.route('/solicitudes/<id>', methods=['PUT'])
def update_solicitud(id):
    solicitud = Solicitud.query.get(id)
    nombre_empleado = request.json['nombre_empleado']
    sucursal = request.json['sucursal']
    proveedor = request.json['proveedor']
    insumo_nombre = request.json['insumo_nombre']
    descripcion = request.json['descripcion']
    marca = request.json['marca']
    cantidad_solicitada = request.json['cantidad_solicitada']
    cantidad_recibida = request.json['cantidad_recibida']
    precio_unidad = request.json['precio_unidad']
    estado_solicitud = request.json['estado_solicitud']
    total = request.json['total']
    observacion = request.json['observacion']

    solicitud.nombre_empleado =nombre_empleado
    solicitud.sucursal = sucursal
    solicitud.proveedor = proveedor
    solicitud.insumo_nombre =insumo_nombre
    solicitud.descripcion = descripcion
    solicitud.marca = marca
    solicitud.cantidad_solicitada =cantidad_solicitada
    solicitud.cantidad_recibida =cantidad_recibida
    solicitud.precio_unidad = precio_unidad
    solicitud.estado_solicitud = estado_solicitud
    solicitud.total = total
    solicitud.observacion = observacion

    db.session.commit()

    return solicitud_schema.jsonify(solicitud),200

@app.route('/solicitudes/<id>', methods=['PATCH'])
def update_envio(id):
    solicitud = Solicitud.query.get(id)
    estado_solicitud = request.json['estado_solicitud']

    solicitud.estado_solicitud = estado_solicitud

    db.session.commit()

    return solicitud_schema.jsonify(solicitud),200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
  
@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT, PATCH'
    return response

@app.route('/', methods=['GET'])
def index():
    titulo= "Súper Ávila"
    return render_template('index.html', titulo=titulo)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)