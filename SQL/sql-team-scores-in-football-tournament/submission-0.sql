WITH team_points AS (
    -- Points earned when playing as HOST
    SELECT 
        host_team AS team_id,
        CASE 
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS points
    FROM matches

    UNION ALL

    -- Points earned when playing as GUEST
    SELECT 
        guest_team AS team_id,
        CASE 
            WHEN guest_goals > host_goals THEN 3
            WHEN guest_goals = host_goals THEN 1
            ELSE 0
        END AS points
    FROM matches
)

SELECT 
    t.team_id,
    t.team_name,
    COALESCE(SUM(tp.points), 0) AS num_points
FROM teams t
LEFT JOIN team_points tp 
    ON t.team_id = tp.team_id
GROUP BY 
    t.team_id, 
    t.team_name
ORDER BY 
    num_points DESC, 
    t.team_id ASC;