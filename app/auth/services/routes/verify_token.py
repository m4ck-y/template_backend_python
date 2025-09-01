from fastapi import Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from app.utils.jwt import verify_token
from app.utils.log import log_info
def VerifyToken(value=Depends(verify_token)):
    """
    Verifica si el token JWT es válido, extraído ya sea de la cookie o del encabezado.
    """
    log_info(f"verify_token: {value}"), type(value)

    # Asegurarse de que el token esté presente y validado
    if value:
        return JSONResponse(content={"message": "Token is valid"})
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")