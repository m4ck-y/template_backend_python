from app.company.domain.enum.organization_size import EOrganizationSize
from app.company.domain.enum.type_organization import EOrganizationType
from app.company.infrastructure.database.model.company import Company
from app.company.infrastructure.database.model.industry import Industry
from app.health_facility.infrastructure.database.model.heatlh_facility import HealthFacility
from app.company.infrastructure.database.model.location import Location
from app.config.db import Session

def init():
    print("init >>> health_facility")


def Seeder(id_health_industry: int):
    session = Session()

    count = session.query(HealthFacility).count()

    print("---- count health_facility: ", count)
    if count > 0:
        print("health_facility ya existen en la base de datos.", count)
        return
    
    print("""

        -----------------
          
""")

    health_facility = HealthFacility(
        company=Company(
            name="HOSPITAL DE PSIQUIATRÍA CON M.F. NO. 10",
            legal_name="INSTITUTO MEXICANO DEL SEGURO SOCIAL",
            commercial_name="HOSPITAL DE PSIQUIATRÍA CON M.F. NO. 10",
            fiscal_id = "IMS421231I45",

            url_website=None,
            url_logo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Logotipo_del_IMSS.svg/800px-Logotipo_del_IMSS.svg.png",
            tagline="Seguridad y solidaridad social",

            industry = Industry(
                id_parent_industry=id_health_industry,
                name="Hospitals",
                description="This industry includes entities that provide varied medical, diagnostic, and treatment services that include physician, nursing, and other health services to inpatients.",
            ),
            
            organization_size=EOrganizationSize.EMPLOYEES_51_200,
            type_organization=EOrganizationType.GOVERNMENT_AGENCY,

            id_parent_company=None,

            location = Location(
                key_country=None,
                key_state=None,
                key_city=None,
                key_municipality=None,
                key_neighborhood=None,
                address="CLZD. DE TLALPÁN NO. 931 NIÑOS HÉROES DE CHAPULTEPEC C. P. 03440 BENITO JUAREZ, CDMX",
                address_complement=None,
                postal_code="03440",
                latitude="19.4017",
                longitude="-99.1583",    
            )

        ),
        key="",
        key_institution="",
        key_establishment_type="",
        key_typology="",
        sanitary_license="",
        patient_nomenclature=""
    )

    session.add_all([health_facility])
    session.commit()

    print("""

        -----------------
          
""")