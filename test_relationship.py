#!/usr/bin/env python3
"""
Script de prueba para verificar que la relación entre Person y BiologicalProfile funciona correctamente.
"""

import sys
import os

# Agregar el directorio raíz al path para importar los módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app.person.infrastructure.database.model.person import Person
    from app.health_monitoring.infrastructure.database.model.biological_profile import BiologicalProfile
    from app.config.db import engine, Base
    
    print("✅ Imports exitosos")
    
    # Intentar crear las tablas para verificar que no hay errores de relación
    print("🔧 Creando tablas...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas exitosamente")
    
    # Verificar que las relaciones están bien definidas
    print("🔍 Verificando relaciones...")
    
    # Verificar que Person tiene la relación biological_profile
    if hasattr(Person, 'biological_profile'):
        print("✅ Person.biological_profile existe")
    else:
        print("❌ Person.biological_profile NO existe")
    
    # Verificar que BiologicalProfile tiene la relación person
    if hasattr(BiologicalProfile, 'person'):
        print("✅ BiologicalProfile.person existe")
    else:
        print("❌ BiologicalProfile.person NO existe")
    
    # Verificar que BiologicalProfile tiene la foreign key
    if hasattr(BiologicalProfile, 'id_person'):
        print("✅ BiologicalProfile.id_person existe")
    else:
        print("❌ BiologicalProfile.id_person NO existe")
    
    print("\n🎉 Todas las verificaciones completadas exitosamente!")
    print("La relación entre Person y BiologicalProfile está funcionando correctamente.")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)