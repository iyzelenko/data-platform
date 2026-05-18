SELECT faculty, AVG(grade) as avg_grade
FROM students
GROUP BY faculty;