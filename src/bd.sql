create database Unes;

create table Contato(
	email_contato varchar(70) not null,
    assunto_contato varchar(100) not null,
    descricao_contato varchar(500) not null
);

select * from Contato;