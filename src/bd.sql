create database nomeDoDataBase;
use nomeDoDataBase;

create table Contato(
	email_contato varchar(70) not null,
    assunto_contato varchar(100) not null,
    descricao_contato varchar(500) not null,
    estado char(1) not null
);

select * from Contato;