from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

#Tabla de Solicitudes
class Solicitud(db.Model):
    __tablename__ = 'solicitudes'
    id = db.Column(db.Integer, primary_key=True) 
    nombre_empleado = db.Column(db.String(100), nullable=False)
    sucursal  = db.Column(db.String(30))
    proveedor = db.Column(db.String(70))
    insumo_nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
    marca = db.Column(db.String(70))
    cantidad = db.Column(db.Integer)
    precio_unidad = db.Column(db.Float(precision=10)) 
    estado_solicitud = db.Column(db.String(50))
    fecha_emision = db.Column(db.DateTime, default= datetime.datetime.now)
    total = db.Column(db.Float(precision=10))
    observacion = db.Column(db.String(100))


    def __init__(self, nombre_empleado, sucursal, proveedor, insumo_nombre,descripcion, marca, cantidad, precio_unidad, estado_solicitud, fecha_emision, total, observacion):
            self.nombre_empleado = nombre
            self.sucursal = stock
            self.proveedor = descripcion
            self.insumo_nombre = insumo_nombre
            self.descripcion = descripcion
            self.marca = marca
            self.cantidad = cantidad
            self.precio_unidad = precio_unidad
            self.estado_solicitud = estado_solicitud
            self.fecha_emision = fecha_emision
            self.total = total
            self.observacion = observacion
    



