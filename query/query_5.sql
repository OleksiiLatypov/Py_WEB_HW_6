SELECT d.name, t.fullname 
FROM disciplines d
LEFT JOIN teachers t ON d.teacher_id = t.id
WHERE t.id = 1
GROUP BY d.name;

