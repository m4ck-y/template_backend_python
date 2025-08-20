from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class BaseORMModel(BaseModel):

    """
    Modelo base para objetos ORM que extiende `BaseModel` de Pydantic, diseñado para facilitar la conversión de 
    objetos ORM a modelos de Pydantic.
    """

    model_config = ConfigDict(from_attributes=True)
    """
    📄 Descripción:
    Configuración de Pydantic para mapear atributos del objeto ORM de forma automática. La opción 
    `from_attributes=True` permite que los atributos del ORM sean convertidos correctamente a 
    atributos de Pydantic.

    🧩 Ejemplo:
    Este ajuste facilita la conversión de objetos SQLAlchemy a objetos Pydantic para validación 
    y serialización.
    """

class BaseORMTimeSeries(BaseORMModel):
    """
    Base para cualquier evento con marca de tiempo.
    """
    event_at: datetime  # Fecha y hora real del evento (no cuándo fue creado el registro)

class BaseAuditModel(BaseORMModel):
    """
    🧩 Campos de auditoría:
    - `created_at`: Fecha de creación.
    - `updated_at`: Fecha de la última actualización.
    - `deleted_at`: Fecha de eliminación (soft delete).
    - `created_by_id_employee_role`: ID del usuario o rol que creó el registro.
    - `updated_by_id_employee_role`: ID del usuario o rol que actualizó el registro.
    - `deleted_by_id_employee_role`: ID del usuario o rol que eliminó el registro."""

    created_at: datetime = None
    """
    📄 Descripción:
    Fecha y hora en que el registro fue creado. Este campo es obligatorio y se establece 
    automáticamente al momento de la creación.

    🧩 Ejemplo:
    2025-05-09T12:00:00Z
    """

    updated_at: Optional[datetime] = None
    """
    📄 Descripción:
    Fecha y hora de la última actualización del registro. Este campo se actualiza automáticamente 
    cada vez que el registro es modificado.

    🧩 Ejemplo:
    2025-05-10T15:30:00Z
    """

    deleted_at: Optional[datetime] = None
    """
    📄 Descripción:
    Fecha y hora en que el registro fue marcado como eliminado. Este es un campo opcional que se 
    establece cuando el registro ha sido "eliminado" (soft delete), pero no se elimina físicamente.

    🧩 Ejemplo:
    2025-05-11T10:00:00Z
    """

    #created_by_id_employee_role: Optional[int] = None
    """
    📄 Descripción:
    ID del usuario o rol (vía la relación `employee_role`) que creó el registro. Este campo es 
    opcional y puede ser `None` si no se dispone de esta información.

    🧩 Ejemplo:
    101 (ID de un rol de empleado)
    """

    #updated_by_id_employee_role: Optional[int] = None
    """
    📄 Descripción:
    ID del usuario o rol (vía la relación `employee_role`) que realizó la última actualización 
    del registro. Este campo es opcional y puede ser `None` si no se dispone de esta información.

    🧩 Ejemplo:
    102 (ID de un rol de empleado)
    """

    #deleted_by_id_employee_role: Optional[int] = None
    """
    📄 Descripción:
    ID del usuario o rol (vía la relación `employee_role`) que marcó el registro como eliminado. 
    Este campo es opcional y puede ser `None` si no se dispone de esta información.

    🧩 Ejemplo:
    103 (ID de un rol de empleado)
    """

class BaseAuditModelWithTimeSeries(BaseAuditModel, BaseORMTimeSeries):
    """
    Modelo de auditoría que incluye una serie temporal.
    """
    pass