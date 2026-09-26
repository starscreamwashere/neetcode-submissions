SELECT 
    department.name AS department,
    employee.name AS employee,
    employee.salary
FROM employee
JOIN department 
    ON department.id = employee.department_id
WHERE employee.salary = (
    SELECT MAX(e2.salary)
    FROM employee e2
    WHERE e2.department_id = employee.department_id
);