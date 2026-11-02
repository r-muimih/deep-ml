-- your query
SELECT id, email
FROM person p
WHERE id = (
    SELECT MIN(p2.id)
    FROM person p2
    WHERE p2.email = p.email
)
ORDER BY id ASC;