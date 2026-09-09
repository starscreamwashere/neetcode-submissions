-- Write your query below
WITH RankedResults AS(
    SELECT student_id,exam_id,score,ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC,exam_id ASC) As rn FROM exam_results
)

SELECT student_id,exam_id,score
FROM RankedResults
WHERE rn=1;