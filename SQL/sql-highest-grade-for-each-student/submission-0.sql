-- Write your query below
SELECT DISTINCT ON (student_id) student_id, exam_id, score
FROM exam_results e
WHERE score = 
(SELECT max(score)
FROM exam_results
WHERE student_id = e.student_id) 
ORDER BY student_id ASC, score DESC, exam_id ASC