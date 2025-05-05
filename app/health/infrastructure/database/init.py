from app.health.infrastructure.database.model.health_info import HealthInfo
from app.health.infrastructure.database.model.measure_group import MeasureGroup
from app.health.infrastructure.database.model.unit import Unit
from app.health.infrastructure.database.model.measure_type import MeasureType
from app.health.infrastructure.database.model.measure_type_group import MeasureTypeGroup
from app.health.infrastructure.database.model.measurement import Measurement

from app.config.db import Session, engine


def init():
    print("init >>> health")

def Seeder():
    session = Session()


    print("---- Count unit return", session.query(Unit).count())

    

    # Crear y agregar las unidades de medida
    unit_kilogram = Unit(name="Kilogram", symbol="kg")
    unit_meter = Unit(name="Meter", symbol="m")
    unit_celsius = Unit(name="Celsius", symbol="°C")
    unit_liter = Unit(name="Liter", symbol="L")
    unit_second = Unit(name="Second", symbol="s")
    unit_ampere = Unit(name="Ampere", symbol="A")
    unit_mmHg = Unit(name="Millimeters of Mercury", symbol="mmHg")  # Para la presión arterial


    print("unit_kilogram", unit_kilogram)
    print("unit_meter", unit_meter)
    print("unit_celsius", unit_celsius)
    print("unit_liter", unit_liter)
    print("unit_second", unit_second)
    print("unit_ampere", unit_ampere)
    print("unit_mmHg", unit_mmHg)

    # Agregar las unidades si no existen en la base de datos
    u = session.query(Unit).first()

    print("---- First unit",u)
    print("list", session.query(Unit).count())
    if u:
        print("Las unidades de medida ya existen en la base de datos.", u.name, u.symbol)
    if not session.query(Unit).first():
        session.add_all([unit_kilogram, unit_meter, unit_celsius, unit_liter, unit_second, unit_ampere, unit_mmHg])
        session.commit()
        session.refresh(unit_kilogram)
        session.refresh(unit_meter)
        session.refresh(unit_celsius)
        session.refresh(unit_liter)
        session.refresh(unit_second)
        session.refresh(unit_ampere)
        session.refresh(unit_mmHg)
        print("Unidades de medida insertadas correctamente.")
    else:
        print("Las unidades de medida ya existen en la base de datos.")

    # Crear y agregar los grupos de medición
    measure_group_general = MeasureGroup(name="Generales", description="Grupos de medidas generales.")
    measure_group_temperature = MeasureGroup(name="Temperatura", description="Grupos relacionados con unidades de temperatura como °C.")
    measure_group_pulse = MeasureGroup(name="Pulso", description="Grupos relacionados con la medición del pulso o ritmo cardíaco.")
    measure_group_skinfold = MeasureGroup(name="Pliegues", description="Grupos relacionados con la medición de pliegues de la piel.")
    measure_group_circumference = MeasureGroup(name="Circunferencias", description="Grupos relacionados con la medición de circunferencias de distintas partes del cuerpo.")
    measure_group_diameter = MeasureGroup(name="Diámetros", description="Grupos relacionados con la medición de diámetros de diversos objetos o partes del cuerpo.")
    measure_group_length = MeasureGroup(name="Longitudes", description="Grupos relacionados con la medición de longitudes como altura o longitud de extremidades.")

    # Agregar los grupos si no existen en la base de datos
    if not session.query(MeasureGroup).first():
        session.add_all([measure_group_general, measure_group_temperature, measure_group_pulse, measure_group_skinfold,
                         measure_group_circumference, measure_group_diameter, measure_group_length])
        session.commit()
        print("Grupos de medición insertados correctamente.")

        # Refrescar para obtener los IDs de los grupos recién creados
        session.refresh(measure_group_general)
        session.refresh(measure_group_temperature)
        session.refresh(measure_group_pulse)
        session.refresh(measure_group_skinfold)
        session.refresh(measure_group_circumference)
        session.refresh(measure_group_diameter)
        session.refresh(measure_group_length)
    else:
        print("Los grupos de medición ya existen en la base de datos.")

    # Crear y agregar los tipos de medición para el grupo 'Generales'
    measure_type_weight = MeasureType(name="Peso", id_unit=unit_kilogram.id)
    measure_type_height = MeasureType(name="Altura", id_unit=unit_meter.id)
    measure_type_bmi = MeasureType(name="IMC Medido", id_unit=unit_kilogram.id)  # Puede estar relacionado con "kg"
    measure_type_normal_weight = MeasureType(name="Peso Habitual", id_unit=unit_kilogram.id)
    measure_type_left_grip = MeasureType(name="Fuerza de Agarre Brazo Izquierdo", id_unit=unit_kilogram.id)  # Puede estar relacionado con "kg"
    measure_type_right_grip = MeasureType(name="Fuerza de Agarre Brazo Derecho", id_unit=unit_kilogram.id)
    measure_type_systolic_pressure = MeasureType(name="Presión Arterial Sistólica", id_unit=unit_mmHg.id)
    measure_type_diastolic_pressure = MeasureType(name="Presión Arterial Diastólica", id_unit=unit_mmHg.id)
    measure_type_insulin = MeasureType(name="Insulina", id_unit=unit_liter.id)  # Puede estar relacionado con "L"
    measure_type_urinary_volume = MeasureType(name="Volumen Urinario de 24h", id_unit=unit_liter.id)
    measure_type_respirations = MeasureType(name="Respiraciones por Minuto", id_unit=unit_second.id)  # En "s" (segundos)

    # Agregar los tipos de medición para 'Generales'
    t = session.query(MeasureType).first()
    print("----- --- --- --- --- -- --- -- MeasureType: ", type(t), t, not t)
    if t is not None:
        print(t.name, t.id_unit, unit_kilogram.id)

    if not session.query(MeasureType).first():
        session.add_all([measure_type_weight, measure_type_height, measure_type_bmi, measure_type_normal_weight,
                         measure_type_left_grip, measure_type_right_grip, measure_type_systolic_pressure,
                         measure_type_diastolic_pressure, measure_type_insulin, measure_type_urinary_volume, measure_type_respirations])
        session.commit()
        print("Tipos de medición para 'Generales' insertados correctamente.")
        # Refrescar para obtener los IDs de los tipos de medición recién creados
        session.refresh(measure_type_weight)
        print("----- --- --- --- --- -- --- -- MeasureType weight: ", measure_type_weight)
        print("----- --- --- --- --- -- --- -- id", measure_type_weight.id)
        session.refresh(measure_type_height)
        session.refresh(measure_type_bmi)
        session.refresh(measure_type_normal_weight)
        session.refresh(measure_type_left_grip)
        session.refresh(measure_type_right_grip)
        session.refresh(measure_type_systolic_pressure)
        session.refresh(measure_type_diastolic_pressure)
        session.refresh(measure_type_insulin)
        session.refresh(measure_type_urinary_volume)
        session.refresh(measure_type_respirations)
    else:
        print("Los tipos de medición para 'Generales' ya existen en la base de datos.")


    # Crear relaciones entre los tipos de medición y el grupo 'Generales'
    session.add_all([
        MeasureTypeGroup(measure_type=measure_type_weight, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_height, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_bmi, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_normal_weight, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_left_grip, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_right_grip, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_systolic_pressure, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_diastolic_pressure, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_insulin, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_urinary_volume, id_measure_group=measure_group_general.id),
        MeasureTypeGroup(measure_type=measure_type_respirations, id_measure_group=measure_group_general.id)
    ])
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Generales' insertadas correctamente.")

    # Crear y agregar los tipos de medición para el grupo 'Temperatura'
    measure_type_buccal_temperature = MeasureType(name="Temperatura Bucal", id_unit=unit_celsius.id)
    measure_type_axillary_temperature = MeasureType(name="Temperatura Axilar", id_unit=unit_celsius.id)
    measure_type_inguinal_temperature = MeasureType(name="Temperatura Inguinal", id_unit=unit_celsius.id)
    measure_type_anal_temperature = MeasureType(name="Temperatura Anal", id_unit=unit_celsius.id)

    # Agregar los tipos de medición para 'Temperatura'
    session.add_all([measure_type_buccal_temperature, measure_type_axillary_temperature, measure_type_inguinal_temperature, measure_type_anal_temperature])
    session.commit()
    print("Tipos de medición para 'Temperatura' insertados correctamente.")

    # Refrescar para obtener los IDs de los tipos de medición de temperatura
    session.refresh(measure_type_buccal_temperature)
    session.refresh(measure_type_axillary_temperature)
    session.refresh(measure_type_inguinal_temperature)
    session.refresh(measure_type_anal_temperature)

    # Crear relaciones entre los tipos de medición y el grupo 'Temperatura'
    session.add_all([
        MeasureTypeGroup(measure_type=measure_type_buccal_temperature, id_measure_group=measure_group_temperature.id),
        MeasureTypeGroup(measure_type=measure_type_axillary_temperature, id_measure_group=measure_group_temperature.id),
        MeasureTypeGroup(measure_type=measure_type_inguinal_temperature, id_measure_group=measure_group_temperature.id),
        MeasureTypeGroup(measure_type=measure_type_anal_temperature, id_measure_group=measure_group_temperature.id)
    ])
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Temperatura' insertadas correctamente.")

    # Crear y agregar los tipos de medición para el grupo 'Pulso'
    measure_type_pulse_rate = MeasureType(name="Ritmo Cardíaco", id_unit=unit_second.id)

    # Agregar los tipos de medición para 'Pulso'
    session.add(measure_type_pulse_rate)
    session.commit()
    print("Tipos de medición para 'Pulso' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de pulso
    session.refresh(measure_type_pulse_rate)

    # Crear relaciones entre los tipos de medición y el grupo 'Pulso'
    session.add(MeasureTypeGroup(measure_type=measure_type_pulse_rate, id_measure_group=measure_group_pulse.id))
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Pulso' insertadas correctamente.")

    # Crear y agregar los tipos de medición para el grupo 'Pliegues'
    measure_type_skinfold = MeasureType(name="Pliegue Cutáneo", id_unit=unit_meter.id)

    # Agregar los tipos de medición para 'Pliegues'
    session.add(measure_type_skinfold)
    session.commit()
    print("Tipos de medición para 'Pliegues' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de pliegues
    session.refresh(measure_type_skinfold)

    # Crear relaciones entre los tipos de medición y el grupo 'Pliegues'
    session.add(MeasureTypeGroup(measure_type=measure_type_skinfold, id_measure_group=measure_group_skinfold.id))
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Pliegues' insertadas correctamente.")

    # Crear y agregar los tipos de medición para el grupo 'Circunferencias'
    measure_type_circumference = MeasureType(name="Circunferencia", id_unit=unit_meter.id)

    # Agregar los tipos de medición para 'Circunferencias'
    session.add(measure_type_circumference)
    session.commit()
    print("Tipos de medición para 'Circunferencias' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de circunferencia
    session.refresh(measure_type_circumference)

    # Crear relaciones entre los tipos de medición y el grupo 'Circunferencias'
    session.add(MeasureTypeGroup(measure_type=measure_type_circumference, id_measure_group=measure_group_circumference.id))
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Circunferencias' insertadas correctamente.")

    # Crear y agregar los tipos de medición para el grupo 'Diámetros'
    measure_type_diameter = MeasureType(name="Diámetro", id_unit=unit_meter.id)

    # Agregar los tipos de medición para 'Diámetros'
    session.add(measure_type_diameter)
    session.commit()
    print("Tipos de medición para 'Diámetros' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de diámetro
    session.refresh(measure_type_diameter)

    # Crear relaciones entre los tipos de medición y el grupo 'Diámetros'
    session.add(MeasureTypeGroup(measure_type=measure_type_diameter, id_measure_group=measure_group_diameter.id))
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Diámetros' insertadas correctamente.")

    # Crear y agregar los tipos de medición para el grupo 'Longitudes'
    measure_type_length = MeasureType(name="Longitud", id_unit=unit_meter.id)

    # Agregar los tipos de medición para 'Longitudes'
    session.add(measure_type_length)
    session.commit()
    print("Tipos de medición para 'Longitudes' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de longitudes
    session.refresh(measure_type_length)

    # Crear relaciones entre los tipos de medición y el grupo 'Longitudes'
    session.add(MeasureTypeGroup(measure_type=measure_type_length, id_measure_group=measure_group_length.id))
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Longitudes' insertadas correctamente.")
