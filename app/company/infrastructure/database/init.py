from app.company.domain.enum.organization_size import EOrganizationSize
from app.company.domain.enum.type_organization import EOrganizationType
from app.company.infrastructure.database.model.industry import Industry
from app.company.infrastructure.database.model.company import Company
from app.company.infrastructure.database.model.type_service import TypeService
from app.company.infrastructure.database.model.location import Location
from app.config.db import Session, engine, TSession

def init():
    print("init >>> company")

def Seeder() -> int:

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

    company = Company(
        name="Liber Salus",
        legal_name="LIBER SALUS S. A. DE C. V.",
        commercial_name="LIBER SALUS",
        fiscal_id="LSA120511F20",

        url_website="https://libersalus.com",
        url_logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5mug1kZAbRtSexOlAnCSRDudlfe-GKxYfQA&s",
        tagline="Inspirando a vivir con salud",

        industry=health_care,

        organization_size=EOrganizationSize.EMPLOYEES_51_200,
        type_organization=EOrganizationType.PRIVATELY_HELD,

        id_parent_company=None,

        location = Location(
            key_country=None,
            key_state=None,
            key_city=None,
            key_municipality=None,
            key_neighborhood=None,
            address="Eugenia 191, Narvarte Poniente, Benito Juárez, 03020 Ciudad de México, CDMX",
            address_complement="Piso 9",
            postal_code="03020",
            latitude="19.3845555",
            longitude="-99.1488064",
        )
    )

    type_services = [TypeService(
        name="Salud bucal",
        industry=health_care
    ),
    TypeService(
        name="Consulta externa",
        industry=health_care
    ) 
    ]

    session.add_all([list_tech, health_care, company, *type_services])
    session.refresh(health_care)
    session.commit()

    return health_care.id