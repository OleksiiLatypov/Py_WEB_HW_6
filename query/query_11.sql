SELECT ROUND(AVG(grades.grade), 2), students.fullname as student, teachers.fullname as teacher
FROM grades
JOIN students ON students.id = grades.student_id
JOIN disciplines ON disciplines.id = grades.discipline_id
JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE teachers.id = 1 AND students.id = 1;