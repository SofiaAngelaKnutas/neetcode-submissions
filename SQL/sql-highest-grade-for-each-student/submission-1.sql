-- Write your query below
SELECT student_id, MIN(exam_id) AS exam_id, score
FROM exam_results e
WHERE score = 
(SELECT max(score)
FROM exam_results
WHERE student_id = e.student_id) 
GROUP BY student_id, score
ORDER BY student_id ASC