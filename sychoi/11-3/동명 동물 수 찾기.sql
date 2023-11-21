SELECT name, count(name)
FROM animal_ins
GROUP BY name
HAVING count(name) >= 2
ORDER BY name;