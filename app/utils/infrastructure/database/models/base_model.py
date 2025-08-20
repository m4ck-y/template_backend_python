from app.config.db import Base, datetime_now
from sqlalchemy import Column, DateTime, Integer

class BaseModel(Base):
    """
    Clase base abstracta para todas las entidades del modelo.

    Esta clase define los campos comunes que todas las entidades del modelo deben tener.
    Asegura que las entidades herederas cuenten con los siguientes campos:

    - id: Un identificador único (clave primaria) autoincremental para la entidad.
    - created_at: La fecha y hora en que se creó el registro.
    - updated_at: La fecha y hora de la última actualización del registro.
    - deleted_at: La fecha y hora en que se "eliminó" (soft delete) el registro. Si no está asignado, el registro no está marcado como eliminado.

    La clase `BaseModel` no debe ser usada directamente para crear tablas en la base de datos. 
    Las clases que hereden de ella generarán las tablas con estos campos comunes.

    Atributos:
        id (int): Clave primaria de la entidad, es autoincremental y único para cada registro.
        created_at (datetime): Fecha y hora de creación del registro, asignada automáticamente al momento de la creación.
        updated_at (datetime): Fecha y hora de la última actualización del registro, actualizada automáticamente.
        deleted_at (datetime, nullable): Fecha y hora de la eliminación lógica (soft delete), si se marca como eliminado.
    """

    __abstract__ = True  # Asegura que no se cree una tabla para esta clase base, solo para las clases que hereden de ella.

    # ID autoincremental que sirve como clave primaria para la tabla
    id = Column(Integer, primary_key=True, autoincrement=True)
    """
    Identificador único de la entidad. Es una columna de tipo entero, que se autoincrementa cada vez que se crea un nuevo registro.
    Este campo es necesario para cada entidad y actúa como clave primaria.
    """

    # Fecha y hora de creación del registro
    created_at = Column(DateTime, default=datetime_now, nullable=False)
    """
    Almacena la fecha y hora en la que se creó el registro. Se asigna automáticamente mediante `datetime_now` cuando se crea un nuevo registro.
    Este campo es obligatorio (nullable=False) y no puede estar vacío.
    """

    # Fecha y hora de la última actualización del registro
    updated_at = Column(DateTime, onupdate=datetime_now)
    """
    Almacena la fecha y hora de la última actualización del registro. Se actualiza automáticamente cada vez que el registro es modificado.
    Este campo puede ser `None` si el registro nunca ha sido actualizado después de su creación.
    """

    # Fecha y hora de eliminación del registro (soft delete)
    deleted_at = Column(DateTime, nullable=True)
    """
    Se utiliza para marcar el registro como eliminado sin eliminarlo físicamente de la base de datos.
    Este campo es opcional (nullable=True) y será `None` si el registro no ha sido marcado como eliminado.
    En caso de ser marcado como eliminado, contendrá la fecha y hora en que se realizó la eliminación lógica.
    """

    # Campos de auditoría de usuario y su rol o empleado (referencia a `employee_role`)
    #created_by_id_employee_role = Column(Integer, ForeignKey('employee_role.id_employee_role'), nullable=True)  # FK a `employee_role`
    #updated_by_id_employee_role = Column(Integer, ForeignKey('employee_role.id_employee_role'), nullable=True)
    #deleted_by_id_employee_role = Column(Integer, ForeignKey('employee_role.id_employee_role'), nullable=True)


class BaseModelTimeSeries(BaseModel):
    """
    Clase base para modelos de series temporales.

    Esta clase hereda de `BaseModel` y añade un campo adicional `event_at` que representa 
    la fecha y hora real del evento, no la fecha de creación del registro.
    """
    
    __abstract__ = True  # Asegura que no se cree una tabla para esta clase base, solo para las clases que hereden de ella.

    event_at = Column(DateTime, default=datetime_now, nullable=False)
    """
    Fecha y hora real del evento. Este campo es obligatorio y se establece automáticamente al momento de la creación.
    """