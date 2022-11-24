CREATE TABLE items (	
		id_items SERIAL PRIMARY KEY,
		elements VARCHAR (50) NOT NULL,
		prix INTEGER NOT NULL
	);

CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
 	first_name VARCHAR (50) NOT NULL,
 	last_name VARCHAR (60) NOT NULL
);
INSERT INTO items(elements,prix)
VALUES
	('Petit bureau',100),
	('Grand bureau',300),
	('Ventilateur',80);
    INSERT INTO customers(first_name,last_name)
VALUES
	('Greg','Jones'),
	('Sandra','Jones'),
	('Scott','Scott'),
	('Trevor','Vert'),
	('Mélanie','Johnson');
SELECT * FROM items;
SELECT * FROM items WHERE price >80;
SELECT * FROM items WHERE price <=300;
SELECT * FROM customers WHERE last_name='Smith';
SELECT * FROM customers WHERE last_name = 'Jones'
SELECT * FROM customers WHERE first_name !='Scott'; 