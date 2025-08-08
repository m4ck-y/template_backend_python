acount{
    user
}

profile{
    profile{
        wbesite
    },
    education,
    experience,
    skill,
    social_network
}

company{
    type_service[id_instry]
    industry
    services
    service_module
    service_role
}

security{
    role,
    role_permission
    permission,
    module
}


employee{
    employee,
    employee_role,
    employee_mexican,
}


health{

}
health_faiclity{
    health_facility
    attention_level (by hospital)
    servive_attention_level(by service)
}
person{

}


CREATE SCHEMA telemedicine;

CREATE TABLE liberstreaming.sessions (
    id SERIAL PRIMARY KEY,
    id_patient INT NOT NULL REFERENCES patients(id),
    id_doctor INT NOT NULL REFERENCES doctors(id),
    id_socket_patient TEXT NOT NULL,
    id_socket_doctor TEXT NOT NULL,
    start_timestamp TIMESTAMP NOT NULL,
    end_timestamp TIMESTAMP
);


{
    "key": "ENCUESTA123",
    "name": "Encuesta de Satisfacción",
    "description": "Formulario para evaluar el servicio ofrecido",
    "list_questions": [
        {
            "type": "MULTIPLE_CHOICE",
            "text": "¿Cómo calificarías nuestro servicio?",
            "list_answers": [
                {
                    "text": "Excelente",
                    "value": 5,
                    "url": "http://wwww.pinterest.com/image.png",
                    "url_type": "LINK"
                }
            ],
            "conditional_logic": {
                "triggered_by_question_id": 1,
                "formula": "A1 || A2",
                "description": "Habilitar esta pregunta si la respuesta a la Pregunta 1 es 'Excelente' o 'Bueno'"
            }
        }
    ]
}