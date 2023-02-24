SELECT d.name, s.fullname
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN disciplines d ON g.discipline_id = d.id
WHERE s.id = 1
GROUP BY d.name;