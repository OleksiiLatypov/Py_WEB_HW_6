SELECT grades.grade, students.fullname, disciplines.name, [groups].name
FROM grades
JOIN students ON grades.student_id = students.id
JOIN disciplines ON disciplines.id = grades.discipline_id 
JOIN [groups] ON students.group_id = [groups].id
WHERE disciplines.id = 1 AND [groups].id = 1
ORDER BY students.fullname;