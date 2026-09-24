-- Write your query below
--lets first write query to find the global average call duration
--SELECT AVG(duration)
--FROM calls
--now I see we can join person & calls on caller&callee id
--& person and country on country code
SELECT country.name AS country
FROM person
JOIN country ON SUBSTRING(person.phone_number,1,3)=country.country_code
JOIN calls ON person.id=calls.caller_id OR person.id=calls.callee_id
--now question is asking to return those countries jinka avg duration is more than global duration
GROUP BY country.name
HAVING AVG(calls.duration)>(SELECT AVG(duration)
FROM calls);