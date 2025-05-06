from app.health.infrastructure.database.model.health_info import HealthInfo
from app.health.infrastructure.database.model.measure_group import MeasureGroup
from app.health.infrastructure.database.model.unit import Unit
from app.health.infrastructure.database.model.measure_type import MeasureType
from app.health.infrastructure.database.model.measure_type_group import MeasureTypeGroup
from app.health.infrastructure.database.model.measurement import Measurement

from app.config.db import Session, engine, TSession
"""
medidas generales{
	peso
	altura
	imc medido
	peso habitual
	fuerza de agarre brazo izquierdo
	fuerza de agarre brazo derecho
	presion arterial sistolica
	presion arterial diastolica
	insulina
	Volumen urinario de 24h
	respiraciones por minuto
}
temperatura{
	bucal
	axilar
	inguinal
	anal
}
pulso{
	carotideo
	radial
	axilar
	braquial
	femoral
	popliteo
	pedio
	tibial posterior
}
pliegues{
	pectoral
	axiliar medial/ Medio axiliar
	triceps / bicipital
	suprailiaco / lleocrestal
	supraespinal
	muslo frontal
	pantorrilla medial
	sumatoria
}

circunferencias{
	cefalico
	cuello
	brazo relajado
	brazo contraido
	antebrazo
	muñeca
	mesoesternal
	abdomen
	umbilical
	cintura
	cadera
	muslo medio
	muslo
	pantorrilla
	tobillo
}
diametros{
	biacromial
	bi lleocrestideo
	Transverso del torax
	humero
	femur
	muñeca
	bimaleolar
	pie
	transverso del pie
	mano
	transverso de la mano
}
longitudes{
	acromial - radial
	radial - estiliode
	medioestiloidea - dactiliodea
	llioespinal
	trocanterea
	trocanterea - tibial lateral
	tibial medial - maleolar medial
	envergadura de brazos
}
"""


#Unidades de medida
unit_kilogram: Unit = None
unit_meter: Unit = None
unit_celsius: Unit = None
unit_liter: Unit = None
unit_second: Unit = None
unit_ampere: Unit = None
unit_mmHg: Unit = None



def seeder_units(session:TSession):
    print("---- Count unit return", session.query(Unit).count())

    # Crear y agregar las unidades de medida
    global unit_kilogram, unit_meter, unit_celsius, unit_liter, unit_second, unit_ampere, unit_mmHg
    unit_kilogram = Unit(name="Kilogram", symbol="kg")
    unit_meter = Unit(name="Meter", symbol="m")
    unit_celsius = Unit(name="Celsius", symbol="°C")
    unit_liter = Unit(name="Liter", symbol="L")
    unit_second = Unit(name="Second", symbol="s")
    unit_ampere = Unit(name="Ampere", symbol="A")
    unit_mmHg = Unit(name="Millimeters of Mercury", symbol="mmHg")  # Para la presión arterial


    # Agregar las unidades si no existen en la base de datos
    u = session.query(Unit).first()

    print("---- First unit",u)
    print("list", session.query(Unit).count())
    if u:
        print("Las unidades de medida ya existen en la base de datos.", u.name, u.symbol)
        return
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
        raise Exception("Las unidades de medida ya existen en la base de datos.")




def init():
    print("init >>> health")

def Seeder():
    session = Session()

    try:
        seeder_units(session)
    except Exception as e:
        print("Error al insertar las unidades de medida:", e)
        return
   

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


    try:
        Seeder_measure_general(measure_group_general, session)
    except Exception as e:
        print("Error al insertar las medidas generales:", e)
        return

    

    try:
        Seeder_measure_temperature(measure_group_temperature, session)
    except Exception as e:
        print("Error al insertar las medidas de temperatura:", e)
        return
    

    try:
        Seeder_measure_pulse(measure_group_pulse, session)
    except Exception as e:
        print("Error al insertar las medidas de pulso:", e)
        return
    
    try:
        Seeder_measure_pliegues(measure_group_skinfold, session)
    except Exception as e:
        print("Error al insertar las medidas de pliegues:", e)
        return

    try:
        Seeder_measure_circumference(measure_group_circumference, session)
    except Exception as e:
        print("Error al insertar las medidas de circunferencias:", e)
        return
    
    try:
        Seeder_measure_diameter(measure_group_diameter, session)
    except Exception as e:
        print("Error al insertar las medidas de diametros:", e)
        return

    
    try:
        Seeder_measure_length(measure_group_length, session)
    except Exception as e:
        print("Error al insertar las medidas de longitud:", e)
        return



def Seeder_measure_general(measure_group_general: MeasureGroup, session: TSession):
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
        raise Exception("Los tipos de medición para 'Generales' ya existen en la base de datos.")

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

def Seeder_measure_temperature(measure_group_temperature: MeasureGroup, session: TSession):
    # Crear y agregar los tipos de medición para el grupo 'Temperatura'
    measure_type_buccal_temperature = MeasureType(name="Bucal", id_unit=unit_celsius.id)
    measure_type_axillary_temperature = MeasureType(name="Axilar", id_unit=unit_celsius.id)
    measure_type_inguinal_temperature = MeasureType(name="Inguinal", id_unit=unit_celsius.id)
    measure_type_anal_temperature = MeasureType(name="Anal", id_unit=unit_celsius.id)

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

def Seeder_measure_pulse(measure_group_pulse: MeasureGroup, session: TSession):
 # Crear y agregar los tipos de medición para el grupo 'Pulso'
    pulse_carotideo = MeasureType(name="Carotídeo", id_unit=unit_second.id)
    pulse_radial = MeasureType(name="Radial", id_unit=unit_second.id)
    pulse_axilar = MeasureType(name="Axilar", id_unit=unit_second.id)
    pulse_braquial = MeasureType(name="Braquial", id_unit=unit_second.id)
    pulse_femoral = MeasureType(name="Femoral", id_unit=unit_second.id)
    pulse_popliteo = MeasureType(name="Popliteo", id_unit=unit_second.id)
    pulse_pedio = MeasureType(name="Pedio", id_unit=unit_second.id)
    pulse_tibial_posterior = MeasureType(name="Tibial Posterior", id_unit=unit_second.id)

    # Agregar los tipos de medición para 'Pulso'
    session.add_all([pulse_carotideo, pulse_radial, pulse_axilar, pulse_braquial, pulse_femoral, pulse_popliteo, pulse_pedio, pulse_tibial_posterior])
    session.commit()
    print("Tipos de medición para 'Pulso' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de pulso
    session.refresh(pulse_carotideo)
    session.refresh(pulse_radial)
    session.refresh(pulse_axilar)
    session.refresh(pulse_braquial)
    session.refresh(pulse_femoral)
    session.refresh(pulse_popliteo)
    session.refresh(pulse_pedio)
    session.refresh(pulse_tibial_posterior)

    # Crear relaciones entre los tipos de medición y el grupo 'Pulso'
    #session.add(MeasureTypeGroup(measure_type=pulse_carotideo, id_measure_group=measure_group_pulse.id))
    session.add_all([
        MeasureTypeGroup(measure_type=pulse_carotideo, id_measure_group=measure_group_pulse.id),
        MeasureTypeGroup(measure_type=pulse_radial, id_measure_group=measure_group_pulse.id),
        MeasureTypeGroup(measure_type=pulse_axilar, id_measure_group=measure_group_pulse.id),
        MeasureTypeGroup(measure_type=pulse_braquial, id_measure_group=measure_group_pulse.id),
        MeasureTypeGroup(measure_type=pulse_femoral, id_measure_group=measure_group_pulse.id),
        MeasureTypeGroup(measure_type=pulse_popliteo, id_measure_group=measure_group_pulse.id),
        MeasureTypeGroup(measure_type=pulse_pedio, id_measure_group=measure_group_pulse.id),
        MeasureTypeGroup(measure_type=pulse_tibial_posterior, id_measure_group=measure_group_pulse.id)
    ])
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Pulso' insertadas correctamente.")

def Seeder_measure_pliegues(measure_group_skinfold: MeasureGroup, session: TSession):
    # Crear y agregar los tipos de medición para el grupo 'Pliegues'
    pliegue_pectoral = MeasureType(name="Pectoral", id_unit=unit_meter.id)
    pliegue_axilar = MeasureType(name="Axilar medial / Medio axilar", id_unit=unit_meter.id)
    pliegue_triceps = MeasureType(name="Triceps / Tricipital", id_unit=unit_meter.id)
    pliegue_subescapular = MeasureType(name="Subescapular", id_unit=unit_meter.id)
    pliegue_biceps = MeasureType(name="Biceps / Bicipital", id_unit=unit_meter.id)
    pliegue_suprailiaco = MeasureType(name="Suprailiaco / ileocrestal", id_unit=unit_meter.id)
    pliegue_supraespinal = MeasureType(name="Supraespinal", id_unit=unit_meter.id)
    pliegue_abdominal = MeasureType(name="Abdominal", id_unit=unit_meter.id)
    pliegue_muslo = MeasureType(name="Muslo frontal", id_unit=unit_meter.id)
    pliegue_pantorrilla = MeasureType(name="Pantorrilla medial", id_unit=unit_meter.id)
    pliegue_sumatoria = MeasureType(name="Sumatoria", id_unit=unit_meter.id)

    # Agregar los tipos de medición para 'Pliegues'
    session.add_all([pliegue_pectoral, pliegue_axilar, pliegue_triceps, pliegue_subescapular, pliegue_biceps, pliegue_suprailiaco, pliegue_supraespinal, pliegue_abdominal, pliegue_muslo, pliegue_pantorrilla, pliegue_sumatoria])
    session.commit()
    print("Tipos de medición para 'Pliegues' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de pliegues
    session.refresh(pliegue_pectoral)
    session.refresh(pliegue_axilar)
    session.refresh(pliegue_triceps)
    session.refresh(pliegue_subescapular)
    session.refresh(pliegue_biceps)
    session.refresh(pliegue_suprailiaco)
    session.refresh(pliegue_supraespinal)
    session.refresh(pliegue_abdominal)
    session.refresh(pliegue_muslo)
    session.refresh(pliegue_pantorrilla)
    session.refresh(pliegue_sumatoria)

    # Crear relaciones entre los tipos de medición y el grupo 'Pliegues'
    session.add_all([
        MeasureTypeGroup(measure_type=pliegue_pectoral, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_axilar, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_triceps, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_subescapular, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_biceps, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_suprailiaco, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_supraespinal, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_abdominal, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_muslo, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_pantorrilla, id_measure_group=measure_group_skinfold.id),
        MeasureTypeGroup(measure_type=pliegue_sumatoria, id_measure_group=measure_group_skinfold.id)
    ])
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Pliegues' insertadas correctamente.")

def Seeder_measure_circumference(measure_group_circumference: MeasureGroup, session: TSession):
    # Crear y agregar los tipos de medición para el grupo 'Circunferencias'
    circumference_cefalico = MeasureType(name="Cafalico", id_unit=unit_meter.id)
    circumference_cuello = MeasureType(name="Cuello", id_unit=unit_meter.id)
    circumference_brazo_relajado = MeasureType(name="Brazo relajado", id_unit=unit_meter.id)
    circumference_brazo_contraido = MeasureType(name="Brazo contraído", id_unit=unit_meter.id)
    circumference_antebrazo = MeasureType(name="Antebrazo", id_unit=unit_meter.id)
    circumference_muneca = MeasureType(name="Muñeca", id_unit=unit_meter.id)
    circumference_mesoestemal = MeasureType(name="Mesoestémal", id_unit=unit_meter.id)
    circumference_abdomen = MeasureType(name="Abdomen", id_unit=unit_meter.id)
    circumference_umbilical = MeasureType(name="Umbilical", id_unit=unit_meter.id)
    circumference_cintura = MeasureType(name="Cintura", id_unit=unit_meter.id)
    circumference_cadera = MeasureType(name="Cadera", id_unit=unit_meter.id)
    circumference_muslo_medio = MeasureType(name="Muslo medio", id_unit=unit_meter.id)
    circumference_muslo = MeasureType(name="Muslo", id_unit=unit_meter.id)
    circumference_pantorrilla = MeasureType(name="Pantorrilla", id_unit=unit_meter.id)
    circumference_tobillo = MeasureType(name="Tobillo", id_unit=unit_meter.id)


    # Agregar los tipos de medición para 'Circunferencias'
    session.add_all([
        circumference_cefalico,
        circumference_cuello,
        circumference_brazo_relajado,
        circumference_brazo_contraido,
        circumference_antebrazo,
        circumference_muneca,
        circumference_mesoestemal,
        circumference_abdomen,
        circumference_umbilical,
        circumference_cintura,
        circumference_cadera,
        circumference_muslo_medio,
        circumference_muslo,
        circumference_pantorrilla,
        circumference_tobillo
    ])
    session.commit()
    print("Tipos de medición para 'Circunferencias' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de circunferencia
    session.refresh(circumference_cefalico)
    session.refresh(circumference_cuello)
    session.refresh(circumference_brazo_relajado)
    session.refresh(circumference_brazo_contraido)
    session.refresh(circumference_antebrazo)
    session.refresh(circumference_muneca)
    session.refresh(circumference_mesoestemal)
    session.refresh(circumference_abdomen)
    session.refresh(circumference_umbilical)
    session.refresh(circumference_cintura)
    session.refresh(circumference_cadera)
    session.refresh(circumference_muslo_medio)
    session.refresh(circumference_muslo)
    session.refresh(circumference_pantorrilla)
    session.refresh(circumference_tobillo)

    # Crear relaciones entre los tipos de medición y el grupo 'Circunferencias'
    session.add(MeasureTypeGroup(measure_type=circumference_cefalico, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_cuello, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_brazo_relajado, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_brazo_contraido, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_antebrazo, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_muneca, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_mesoestemal, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_abdomen, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_umbilical, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_cintura, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_cadera, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_muslo_medio, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_muslo, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_pantorrilla, id_measure_group=measure_group_circumference.id))
    session.add(MeasureTypeGroup(measure_type=circumference_tobillo, id_measure_group=measure_group_circumference.id))
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Circunferencias' insertadas correctamente.")

def Seeder_measure_diameter(measure_group_diameter: MeasureGroup, session: TSession):
    # Crear y agregar los tipos de medición para el grupo 'Diámetros'
    diameter_biacromial = MeasureType(name="Biacromial", id_unit=unit_meter.id)
    diameter_biiliocrestideo = MeasureType(name="Bi iliocrestídeo", id_unit=unit_meter.id)
    diameter_transverso_torax = MeasureType(name="Transverso del torax", id_unit=unit_meter.id)
    diameter_anteposterior_torax = MeasureType(name="Anteposterior del torax", id_unit=unit_meter.id)
    diameter_humero = MeasureType(name="Humero", id_unit=unit_meter.id)
    diameter_femur = MeasureType(name="Femur", id_unit=unit_meter.id)
    diameter_muneca = MeasureType(name="Muñeca", id_unit=unit_meter.id)
    diameter_bimaleolar = MeasureType(name="Bimaleolar", id_unit=unit_meter.id)
    diameter_pie = MeasureType(name="Pie", id_unit=unit_meter.id)
    diameter_transverso_pie = MeasureType(name="Transverso del pie", id_unit=unit_meter.id)
    diameter_mano = MeasureType(name="Mano", id_unit=unit_meter.id)
    diameter_transverso_mano = MeasureType(name="Transverso de la mano", id_unit=unit_meter.id)


    # Agregar los tipos de medición para 'Diámetros'
    session.add_all([
        diameter_biacromial,
        diameter_biiliocrestideo,
        diameter_transverso_torax,
        diameter_anteposterior_torax,
        diameter_humero,
        diameter_femur,
        diameter_muneca,
        diameter_bimaleolar,
        diameter_pie,
        diameter_transverso_pie,
        diameter_mano,
        diameter_transverso_mano
    ])
    session.commit()
    print("Tipos de medición para 'Diámetros' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de diámetro
    session.refresh(diameter_biacromial)
    session.refresh(diameter_biiliocrestideo)
    session.refresh(diameter_transverso_torax)
    session.refresh(diameter_anteposterior_torax)
    session.refresh(diameter_humero)
    session.refresh(diameter_femur)
    session.refresh(diameter_muneca)
    session.refresh(diameter_bimaleolar)
    session.refresh(diameter_pie)
    session.refresh(diameter_transverso_pie)
    session.refresh(diameter_mano)
    session.refresh(diameter_transverso_mano)

    # Crear relaciones entre los tipos de medición y el grupo 'Diámetros'
    session.add(MeasureTypeGroup(measure_type=diameter_biacromial, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_biiliocrestideo, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_transverso_torax, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_anteposterior_torax, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_humero, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_femur, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_muneca, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_bimaleolar, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_pie, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_transverso_pie, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_mano, id_measure_group=measure_group_diameter.id))
    session.add(MeasureTypeGroup(measure_type=diameter_transverso_mano, id_measure_group=measure_group_diameter.id))
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Diámetros' insertadas correctamente.")


def Seeder_measure_length(measure_group_length: MeasureGroup, session: TSession):
    # Crear y agregar los tipos de medición para el grupo 'Longitudes'
    lenght_acromial = MeasureType(name="Acromial - Radial", id_unit=unit_meter.id)
    lenght_radial_estiloidea = MeasureType(name="Radial - Estiloide", id_unit=unit_meter.id)
    lenght_mediostiloidea = MeasureType(name="Medioestiloidea - Dactiloidea", id_unit=unit_meter.id)
    lenght_ilioespinal = MeasureType(name="Ilioespinal", id_unit=unit_meter.id)
    lenght_trocanterea = MeasureType(name="Trocanterea", id_unit=unit_meter.id)
    lenght_trocanterea_tibial = MeasureType(name="Trocanterea - Tibial lateral", id_unit=unit_meter.id)
    lenght_tibial_lateral = MeasureType(name="Tibial lateral", id_unit=unit_meter.id)
    lenght_tibial_medial = MeasureType(name="Tibial medial - Maleolar medial", id_unit=unit_meter.id)
    lenght_envergadura = MeasureType(name="Envergadura de brazos", id_unit=unit_meter.id)

    # Agregar los tipos de medición para 'Longitudes'
    session.add_all([
        lenght_acromial,
        lenght_radial_estiloidea,
        lenght_mediostiloidea,
        lenght_ilioespinal,
        lenght_trocanterea,
        lenght_trocanterea_tibial,
        lenght_tibial_lateral,
        lenght_tibial_medial,
        lenght_envergadura
    ])
    session.commit()
    print("Tipos de medición para 'Longitudes' insertados correctamente.")

    # Refrescar para obtener el ID de los tipos de medición de longitudes
    session.refresh(lenght_acromial)
    session.refresh(lenght_radial_estiloidea)
    session.refresh(lenght_mediostiloidea)
    session.refresh(lenght_ilioespinal)
    session.refresh(lenght_trocanterea)
    session.refresh(lenght_trocanterea_tibial)
    session.refresh(lenght_tibial_lateral)
    session.refresh(lenght_tibial_medial)
    session.refresh(lenght_envergadura)

    # Crear relaciones entre los tipos de medición y el grupo 'Longitudes'
    session.add(MeasureTypeGroup(measure_type=lenght_acromial, id_measure_group=measure_group_length.id))
    session.add(MeasureTypeGroup(measure_type=lenght_radial_estiloidea, id_measure_group=measure_group_length.id))
    session.add(MeasureTypeGroup(measure_type=lenght_mediostiloidea, id_measure_group=measure_group_length.id))
    session.add(MeasureTypeGroup(measure_type=lenght_ilioespinal, id_measure_group=measure_group_length.id))
    session.add(MeasureTypeGroup(measure_type=lenght_trocanterea, id_measure_group=measure_group_length.id))
    session.add(MeasureTypeGroup(measure_type=lenght_trocanterea_tibial, id_measure_group=measure_group_length.id))
    session.add(MeasureTypeGroup(measure_type=lenght_tibial_lateral, id_measure_group=measure_group_length.id))
    session.add(MeasureTypeGroup(measure_type=lenght_tibial_medial, id_measure_group=measure_group_length.id))
    session.add(MeasureTypeGroup(measure_type=lenght_envergadura, id_measure_group=measure_group_length.id))
    session.commit()
    print("Relaciones entre tipos de medición y grupo 'Longitudes' insertadas correctamente.")