-- source: RISK_SF
-- cron: 1h
-- resolves: burrito
SELECT burritos_table.id AS id,
burritos_table.name AS name,
burritos_table.size AS size,
FROM burritos_table JOIN meat_table ON burritos_table.id = meat_table.burrito_id
WHERE meat_table.id = ${meat.id}
