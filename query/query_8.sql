SELECT ROUND(AVG(g.grade), 2), d.name, t.fullname 
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 4;