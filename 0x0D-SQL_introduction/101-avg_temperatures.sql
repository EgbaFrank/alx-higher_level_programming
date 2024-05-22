-- Use mysql -u root -p my_database < /path/to/temperatures.sql for imports
-- displays the average temperature (Fahrenheit) by city ordered by temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
