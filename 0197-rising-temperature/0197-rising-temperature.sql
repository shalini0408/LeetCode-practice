-- # Write your MySQL query statement below
-- Select id from Weather As current_day 
-- where exists(
--     select 1 from Weather As yesterday 
--     where yesterday.temperature < current_day.temperature and current_day.recordDate = yesterday.recordDate+1 order by recordDate 
-- )

SELECT current_day.id
FROM Weather AS current_day
WHERE EXISTS (
    SELECT 1
    FROM Weather AS yesterday
    WHERE current_day.temperature > yesterday.temperature
    AND current_day.recordDate = yesterday.recordDate + INTERVAL 1 DAY
);
