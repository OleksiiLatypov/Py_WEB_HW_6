SELECT d.name AS disciplines, gr.name AS [group], ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
JOIN [groups] gr ON gr.id = s.group_id
WHERE d.id = 1
GROUP BY gr.name
ORDER by average_grade DESC;