-- Write your query below
-- Write your query below
SELECT u.name AS name, SUM(t.amount) as balance
FROM users u
LEFT JOIN transactions t ON u.account=t.account
GROUP BY u.account
HAVING SUM(t.amount)>10000;