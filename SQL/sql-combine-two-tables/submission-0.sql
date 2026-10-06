-- Write your query below
SELECT p.first_name, p.last_name, a.city, a.state
FROM address a
RIGHT JOIN person p  ON p.person_id = a.person_id