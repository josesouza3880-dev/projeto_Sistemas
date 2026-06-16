create database if not exists Escola_2;
use  Escola_2;
/*
CREATE TABLE Alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL
);
*/

/*
create table Professores (
id int auto_increment primary key,
nome varchar (100) not null,
disciplina varchar (100) not null
);
*/

/*
create table Disciplina (
id int auto_increment primary key,
nome varchar(100) not null
);
*/

/*
create table Notas (
id int auto_increment primary key,
aluno_id int,
disciplina_id int,
nota decimal(5,2),
foreign key (aluno_id) references Alunos(id),
foreign key (disciplina_id) references Disciplina(id)
);
*/
/*
INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Alice Silva', '2005-05-15');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Bruno Costa', '2006-08-25');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Carla Pereira', '2004-02-14');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Daniel Almeida', '2005-12-30');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Eduarda Santos', '2006-01-10');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Felipe Lima', '2005-03-22');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Gabriela Torres', '2005-07-19');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Henrique Mendes', '2004-11-05');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('Isabela Rocha', '2006-04-17');

INSERT INTO Alunos (nome, data_nascimento)  VALUES
('José luiz souza da Rocha', '2006-09-09');
*/
/*
select *from alunos
*/
/*
delete from alunos where id=10
*/
/*
INSERT INTO Professores (nome, disciplina) VALUES
('Prof. Ana', 'Matemática');

INSERT INTO Professores (nome, disciplina) VALUES
('Prof. Bruno', 'Português');

INSERT INTO Professores (nome, disciplina) VALUES
('Prof. Carlos', 'História');

INSERT INTO Professores (nome, disciplina) VALUES
('Prof. Daniela', 'Ciências');
*/ 
select *from Professores