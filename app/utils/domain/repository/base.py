from sqlalchemy.orm.session import Session as TSession
from typing import Generator

# La función `GetSession` se debe definir en la capa de infraestructura, 
# ya que la gestión de sesiones depende de la base de datos utilizada 
# y no debe estar definida en el dominio.
#
# `Session` es importado aquí como un tipo para que pueda ser utilizado 
# en la interfaz genérica de repositorio para los métodos que requieren 
# el paso de una sesión de base de datos. Esto es solo para tipado, 
# y la implementación real de la sesión debe gestionarse en la capa 
# de infraestructura.
#
# **Importante**: Este archivo no gestiona la creación o cierre de la sesión, 
# solo proporciona el tipo `Session` para ser utilizado en la capa de dominio.

def GetSession() -> Generator[TSession, None, None]:
    pass