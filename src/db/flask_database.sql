DROP DATABASE IF EXISTS pruebita_tienda;
CREATE DATABASE pruebita_tienda;
USE pruebita_tienda;

CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30),
    email VARCHAR(50) UNIQUE,
    PASSWORD VARCHAR(255)
);

CREATE TABLE productos(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20),
    precio decimal(10,2) UNSIGNED,
    categoria VARCHAR(20)
);

CREATE TABLE productos_users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_users int,
    id_productos
    FOREIGN KEY (id_productos) REFERENCES productos(id)
    FOREIGN KEY (id_users) REFERENCES users(ID)
);