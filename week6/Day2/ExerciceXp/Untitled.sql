
SELECT * FROM items ORDER BY price ASC; 

SELECT * FROM items WHERE price >=80 ORDER BY price DESC; 

SELECT first_name,last_name FROM customers  ORDER BY first_name ASC LIMIT 3; 

SELECT last_name FROM customers  ORDER BY last_name DESC; 


-- Requête dans la base de données dvdrental
SELECT * FROM customer;

SELECT (first_name, last_name) as full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id,title,description,release_year,rental_rate FROM film ORDER BY rental_rate ASC;

SELECT address,phone FROM address WHERE district='Texas';

SELECT * FROM film WHERE film_id IN (15,150) ;

SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title='African Egg';
 
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title ILIKE 'Af%';

SELECT  film_id,title,description,film.length,rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;

SELECT  film_id,title,description,film.length,rental_rate FROM film  ORDER BY rental_rate ASC  OFFSET 10 FETCH FIRST 10 ROWS ONLY;

SELECT pa.amount, pa.payment_date FROM payment pa INNER JOIN customer cu ON pa.customer_id=cu.customer_id ORDER BY cu.customer_id ASC;

SELECT f.film_id,f.title,f.description,f.length,f.rental_rate FROM film f WHERE f.film_id NOT IN (SELECT film_id FROM inventory);

SELECT co.country, ci.city FROM country co INNER JOIN city ci ON ci.country_id=co.country_id;