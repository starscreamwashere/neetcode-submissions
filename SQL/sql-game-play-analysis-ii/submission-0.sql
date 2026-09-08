-- Write your query below
WITH RankedActivity AS (
    SELECT 
        player_id, 
        device_id,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS rn
    FROM activity
)
SELECT player_id, device_id
FROM RankedActivity
WHERE rn = 1;