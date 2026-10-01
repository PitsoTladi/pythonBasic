--select all users from the dataset
SELECT * FROM titanic;


-- select all passanger younger than 20 who did not survive
SELECT Name,age,survived,sex FROM titanic WHERE age <20 ;

-- SO all passengers by name and age
SELECT Name,age,survived FROM titanic ORDER BY name,age ASC;

--group numbers of survivers and non survivers 
SELECT survived, COUNT(*) AS total FROM titanic GROUP by survived;

-- group survivers and non survivers by age and gender
SELECT survived, age, sex, COUNT(*) AS total FROM titanic GROUP BY survived, age, sex ORDER BY age, sex, survived;


--combine passengerid,name and age with passenger class
SELECT t.PassengerId,Name,age FROM titanic AS t JOIN passenger_classes AS pc ON t.PassengerId = pc.PassengerId;

--aggregate survivors by avarage age
SELECT ROUND(AVG(age)) AS average_age FROM titanic WHERE survived = 1;

--aggregate non-survivor by avarage age
SELECT ROUND(AVG(age)) AS average_age FROM titanic WHERE survived = 0;
--findthe age of  oldest and youngest passengers 
SELECT MAX(age) AS oldest_age, MIN(age) AS youngest_age FROM titanic;