CREATE TABLE students(
	id_student SERIAL PRIMARY KEY,
	first_name VARCHAR(25) NOT NULL,
	last_name VARCHAR(60) NOT NULL,
	birth_date DATE NOT NULL
	);
    INSERT INTO students(
	first_name,last_name,birth_date
	) 
VALUES
	('Marc','Bénichou','02/11/1998'),
	('Yann','Cohen','03/12/2010'),
	('Léa','Bénichou','27/07/1987'),
	('Amélie','Dux','07/04/1996'),
	('David','Grez','14/06/2003'),
	('Omer','Simpson','03/10/1980');
INSERT INTO students(
	first_name,last_name,birth_date
	) 
VALUES
	('Malick','Lengani','01/05/1988');
SELECT * FROM students 
SELECT first_name,last_name FROM students;
SELECT first_name,last_name FROM students WHERE id_student = 2;
SELECT first_name,last_name FROM students WHERE last_name='Benichou' AND first_name='Marc';
SELECT first_name,last_name FROM students WHERE last_name='Benichou' OR first_name='Marc';
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a%';
SELECT first_name,last_name FROM students WHERE  first_name ILIKE 'a%';
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a-';
SELECT first_name,last_name FROM students WHERE  id_student = 1 AND id_student = 3;
SELECT * FROM students WHERE  birth_date >= '01/01/2000';