CREATE DATABASE login;
use login;

CREATE TABLE IF NOT EXISTS logininfo (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(22) CHARACTER SET utf8,
    `email` VARCHAR(50) CHARACTER SET utf8,
    `password` varchar(50),
    PRIMARY KEY (`id`)
);

INSERT INTO logininfo (name, email, password)   VALUES
                                 ('Alex' , 'Alex@xyz.com', 'abcde'),
                                 ('Bert' , 'Bert@xyz.com', 'abcde'),
                                 ('Fran' , 'Fran@xyz.com', 'abcde'),
                                 ('Jake' , 'Jake@xyz.com', 'abcde'),
                                 ('Gwen' , 'Gwen@xyz.com', 'abcde');
