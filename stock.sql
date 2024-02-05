--
-- Author: Cyril GENISSON
-- Created: 01/02/2024
-- Updated: 01/02/2024
--
-- filename: stock.sql
-- Description: 
--
DROP DATABASE IF EXISTS store;
CREATE DATABASE store;
USE store;

CREATE TABLE category(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
) ENGINE = InnoDB;

INSERT INTO category(name) VALUES ('UNCATEGORIZED');

CREATE TABLE product(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT DEFAULT '',
    price DECIMAL(6,2) DEFAULT 0.00,
    quantity INT UNSIGNED DEFAULT 0,
    id_category INT UNSIGNED DEFAULT 1,
    CONSTRAINT `fk_hook_category`
    FOREIGN KEY (id_category) REFERENCES category (id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) ENGINE = InnoDB;

