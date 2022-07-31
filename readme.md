
# Segunda Problematica

CREATE VIEW clientes_view as SELECT c.customer_id as Id,s.branch_number as Numero_sucursal,c.customer_name as Nombre,c.customer_surname as Apellido,c.customer_DNI as DNI,strftime('%Y','now') - strftime('%Y',c.dob) as Edad FROM cliente c LEFT JOIN sucursal s on c.branch_id = s.branch_id; 

SELECT * FROM clientes_view order by DNI asc; 

SELECT * FROM clientes_view WHERE Nombre = 'Anne' OR Nombre = 'Tyler'; 


INSERT INTO cliente
                      (customer_name, customer_surname, customer_DNI, branch_id, dob)
                      VALUES
                      ('Lois', 'Stout', 47730534, 80, '1984-07-07'),
                      ('Hall', 'Mcconnell', 52055464, 45, '1968-04-30'),
                      ('Hilel', 'Mclean', 43625213, 77, '1993-03-28'),
                      ('Jin', 'Cooley', 21207908, 96,  '1959-08-24'), 
                      ('Gabriel', 'Harmon', 57063950, 27,  '1976-04-01');

UPDATE cliente set branch_id = '10' WHERE customer_id >500; 

DELETE from cliente WHERE customer_name = 'Noel' and customer_surname = 'David'; 

SELECT max(loan_total) as Mayor_Importe FROM prestamo; 



# Tercera Problematica

SELECT * FROM cuenta WHERE balance < 0; 

SELECT customer_name, customer_surname, strftime('%Y','now') - strftime('%Y',dob) as Edad FROM cliente WHERE customer_surname like '%z%'; 

SELECT c.customer_name as Nombre,c.customer_surname as Apellido, strftime('%Y','now') - strftime('%Y',c.dob) as Edad, s.branch_name as Nombre_sucursal FROM cliente c LEFT JOIN sucursal s on  c.branch_id = s.branch_id WHERE c.customer_name = 'Brendan' ORDER by s.branch_name ASC; 

SELECT loan_type, loan_total FROM prestamo WHERE loan_type = 'PRENDARIO' OR loan_total > '8000000'; 

SELECT  * FROM prestamo WHERE loan_total > (SELECT AVG(loan_total) FROM prestamo); 

SELECT count(*) as Menores_50 FROM cliente WHERE strftime('%Y','now') - strftime('%Y',dob)<50; 

SELECT * FROM cuenta WHERE balance > 8000 LIMIT 5; 

SELECT *  FROM prestamo WHERE strftime('%m',loan_date) = '04' or strftime('%m',loan_date) = '06' or strftime('%m',loan_date) = '08' ORDER by loan_total ASC; 

SELECT  loan_type, sum(loan_total) as loan_total_accu FROM prestamo group by loan_type; 

 

# Cuarta Problematica


SELECT s.branch_name, count(c.branch_id) as Cantidad_de_clientes FROM sucursal s LEFT JOIN cliente c on s.branch_id = c.branch_id GROUP by s.branch_name ORDER By Cantidad_de_clientes DESC; 

SELECT s.branch_name, count(*) as Tarjetas FROM tipo_usuarios tp LEFT JOIN cliente c ON tp.customer_id = c.customer_id LEFT JOIN sucursal s ON c.branch_id = s.branch_id where tp.card_type = 'CREDIT' GROUP by s.branch_name 

 

SELECT s.branch_name,avg(p.loan_total) FROM prestamo p LEFT JOIN cliente c ON p.customer_id = c.customer_id LEFT JOIN sucursal s ON c.branch_id = s.branch_id GROUP by s.branch_name 