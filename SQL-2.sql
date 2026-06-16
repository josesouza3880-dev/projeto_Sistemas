-- create database escola;
-- use escola;
-- drop table alunos;
/*
create table alunos (
id int auto_increment primary key,
nome varchar(100) not null,
data_nascimento date
);
*/

/*
create table Prefessores (
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

insert into Alunos (nome, data_nascimento) values
('Alice Silva', '2005-05-15'),
('Bruno Costa', '2006-08-25'),
('Carla Pereira', '2004-02-14');
