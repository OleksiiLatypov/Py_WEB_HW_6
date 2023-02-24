SELECT grades.date_of as date, grades.grade, [groups].name as [group], disciplines.name as discipline, students.fullname AS students
FROM grades
JOIN disciplines ON disciplines.id = grades.discipline_id
JOIN students ON students.id = grades.student_id 
JOIN [groups] ON [groups].id = students.group_id
WHERE [groups].id = 1 AND disciplines.id = 1 AND grades.date_of = '2023-06-15';
