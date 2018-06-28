-- SQL Exercises
-- --------------------
-- Use the nobel database from class to answer the following questions.

-- 1. Select the nobel database.

USE nobel;

-- 2. List the tables.

SHOW tables;

-- 3. Select the first ten records from the laureate table.

SELECT *
FROM laureate
LIMIT 10;

-- 4. Find the birth and death dates for Albert Einstein.

SELECT birth_date, death_date
FROM laureate
WHERE name = 'Albert Einstein';

-- 5. Find the Nobel Laureates who died in 2015 and whose name begins with 'Y'.

SELECT *
FROM laureate
WHERE death_date BETWEEN '2015-01-01' AND '2015-12-31' AND name LIKE 'Y%';

-- 6. Find the last three Nobel Laureates born in 1900.

SELECT *
FROM laureate
ORDER BY birth_date DESC
LIMIT 3;

-- 7. Find the number of Nobel Prizes awarded between 1950 and 1960.

SELECT COUNT(*)
FROM prize
WHERE year BETWEEN '1950-01-01' AND '1960-12-31';

-- 8. Find the number of Nobel Prizes awarded in each year.

SELECT year, COUNT(*)
FROM prize
GROUP BY year;

-- 9. In which year was the greatest number of Nobel Prizes awarded?

SELECT year, COUNT(*) AS maxprize
FROM prize
GROUP BY year
ORDER BY maxprize DESC
LIMIT 1;

-- 10. What is the average number of Nobel Prizes awarded per year? Do we know how to do this yet?

SELECT AVG(avgprize)
FROM (SELECT year, COUNT(*) AS avgprize 
	FROM prize
	GROUP BY year)
AS average;

-- 11. In which years were more than fifteen Nobel Prizes awarded?

SELECT year, COUNT(*) AS moreyear
FROM prize
GROUP BY year HAVING moreyear > 15
ORDER BY moreyear DESC;

-- 12. Who is the Nobel Laureate with the shortest name?

SELECT laureate.name, LENGTH(name)  
FROM laureate
ORDER BY LENGTH(name)
LIMIT 1;

-- 13. Which Nobel Laureate had the longest life? You might need to use IFNULL().

SELECT laureate.name, IFNULL(death_date - birth_date, 0)
FROM laureate
ORDER BY death_date - birth_date DESC 
LIMIT 1;

-- 14. Which year has the most women Nobel Laureates?

SELECT AVG(avgprize)
FROM (SELECT year, COUNT(*) AS avgprize 
	FROM prize
	WHERE sex = 'F'
	GROUP BY year)
AS average;

-- AND/OR

SELECT laureate.name, COUNT(*) AS morewomen
FROM laureate
JOIN prize
ON laureate.id = prize.laureate_id
WHERE sex = 'F'
GROUP BY `year`;

-- I think the answer is someting along these lines but can't figure out how to combine them.

-- 15. Which category has the most women Nobel Laureates?

SELECT year, category, COUNT(*)
FROM laureate
JOIN prize
ON laureate.id = prize.laureate_id
WHERE sex = 'F'
GROUP BY category; 

-- 16. What is the average number of Nobel Prizes awarded per year?

SELECT AVG(total)
FROM(SELECT year, COUNT(*) AS total
	FROM prize
	GROUP by year)
AS average;

