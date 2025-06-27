from app.company.infrastructure.database.model.industry import Industry
from app.config.db import Session, engine, TSession

def init():
    print("init >>> company")

def Seeder():

    session = Session()

    count = session.query(Industry).count()

    print("---- count industries: ", count)
    if count > 0:
        print("Las industrias ya existen en la base de datos.", count)
        return

    list_tech = Industry(
    name="Tecnología",
    description="Sector de tecnología y medios digitales",
    list_subindustries=[
        Industry(
            name="Software",
            description="Empresas de desarrollo de software"
        ),
        Industry(
            name="Hardware",
            description="Fabricantes de componentes electrónicos"
        )
    ]
    )

    health_care = Industry(
        name="Hospitals and Health Care",
        description="This industry includes entities that provide health care and health-related social assistance for individuals. It includes entities that provide medical care exclusively, health care and social assistance, and only social assistance. These entities deliver services by trained professional health practitioners or social workers.",
        list_subindustries=[
            Industry(
                name="Hospitals",
                description="Entities that provide varied medical, diagnostic, and treatment services that include physician, nursing, and other health services to inpatients."
            ),
            Industry(
                name="Medical Practices",
                description="Individual medical practices that provide health care services directly or indirectly to ambulatory patients.",
                list_subindustries=[
                    Industry(
                        name="Medical and Diagnostic Laboratories",
                        description="Medical and diagnostic laboratories that provide analytic or diagnostic services."
                    )
                ]
            )
        ]
    )

    session.add_all([list_tech, health_care])
    session.commit()