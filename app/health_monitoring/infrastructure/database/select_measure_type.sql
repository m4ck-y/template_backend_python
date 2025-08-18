SELECT 
    mt.id AS measure_type_id,
    mt.name AS measure_type_name,
    u.id  AS unit_id,
    u.symbol AS unit_symbol,
    u.name AS unit_name,
    mg.id AS id_measure_group,
    mg.name AS measure_group_name
FROM 
    health_measure_type mt
JOIN 
    health_measure_type_group mtg ON mt.id = mtg.id_measure_type
JOIN 
    health_measure_group mg ON mtg.id_measure_group = mg.id
JOIN 
    health_unit u ON mt.id_unit = u.id;