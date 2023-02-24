SELECT d.name as lesson, s.fullname as student, t.fullname as teacher
FROM disciplines d

JOIN students s ON g.student_id = s.id 
JOIN grades g ON g.discipline_id = d.id
JOIN teachers t ON d.teacher_id = t.id
WHERE s.id = 1 AND t.id = 1
GROUP BY d.name;

