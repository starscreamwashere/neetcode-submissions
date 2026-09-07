-- Write your query below
SELECT COALESCE(e.employee_id,s.employee_id) AS employee_id
FROM employees e
FULL JOIN salaries s ON e.employee_id=s.employee_id
WHERE e.name IS NULL or s.salary is NULL
ORDER BY employee_id ASC;