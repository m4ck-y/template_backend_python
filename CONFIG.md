# 📦 Proceso para Inicializar un Proyecto Python con `uv`

Este flujo es para proyectos ya existentes (clonados o descargados) que usan `uv` para manejar versiones de Python y dependencias. La idea es:

-   Estar dentro del **directorio raíz del proyecto** (donde está el archivo `pyproject.toml` y/o `.uv-python-version`).
    
-   Usar la versión de Python especificada (o instalarla si no está).
    
-   Crear y activar un entorno virtual.
    
-   Instalar dependencias (editable o no).
    

----------

## Pasos recomendados

### 0. Posicionarse en la raíz del proyecto


`cd /ruta/a/tu/proyecto` 

Asegúrate de que ahí estén:

-   El archivo `pyproject.toml`
    
-   El archivo `.uv-python-version` o `.python-version` (si aplica)
    

----------

### 1. Verificar versiones disponibles e instaladas

`uv python list` 

-   Muestra las versiones instaladas y las que se pueden descargar.
    
-   Te permite confirmar que la versión requerida por el proyecto esté instalada o disponible.
    

----------

### 2. Crear el entorno virtual


`uv venv` 

-   Usa la versión de Python fijada en `.uv-python-version` o `.python-version`.
    
-   Si la versión no está instalada, `uv` la descarga automáticamente.
    
-   Crea el entorno virtual `.venv` en la raíz del proyecto.
    

----------

### 3. Instalar el paquete local y dependencias

Para desarrollo y poder modificar el código en caliente:


`uv pip install -e .` 

-   Instala el paquete en modo editable.
    
-   Instala también las dependencias listadas en `pyproject.toml`.
    

Si solo quieres instalar dependencias sin modo editable:


`uv pip install` 

----------

### 4. Activar el entorno virtual (opcional, pero recomendado)

`source .venv/bin/activate` 

Para trabajar dentro del entorno aislado.

----------

# 💡 Ideas de nombres para este proceso (comando personalizado)

Si quieres crear un alias o función para este flujo (como `npm install`), aquí algunas sugerencias:

Nombre sugerido

Descripción breve

`uv init`

Inicializa el proyecto (versiones + venv + deps)

`uv setup`

Configura el entorno y dependencias

`uv bootstrap`

Prepara todo para empezar a trabajar

`uv prepare`

Prepara el entorno y paquetes

`uv install`

Equivalente a `npm install`

`uv env-setup`

Configura entorno virtual y dependencias

`uv deps-install`

Instala dependencias basadas en pyproject.toml

----------

# Ejemplo de alias para bash/zsh (usando `uv init`):

```sh
uv_init() 
{ 
    echo  "Posicionándose en la raíz del proyecto..."  
    # cd /ruta/a/tu/proyecto  # Opcional, si ya estás ahí no es necesario

    echo  "Listando versiones Python disponibles..."
    uv python list
    
    echo  "Creando entorno virtual..."
    uv venv
    
    echo  "Instalando paquete editable y dependencias..."
    uv pip install -e .
    
    echo  "Entorno listo. No olvides activar el virtualenv con:"
    echo  "source .venv/bin/activate" 
}
```

Luego ejecutas:

`uv_init`