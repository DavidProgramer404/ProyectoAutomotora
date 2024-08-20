--crear base de datos AUTOMOTORA
create database db_automotora

-- CREAR TIPO USUARIO

create table tipo_usuarios(
	id_tipo_usuario serial not null primary key,
	tipo_usuario varchar(50) not null
);

create table regiones(
	id_region serial not null primary key,
	region varchar(200) not null
)

create table comunas(
	id_comuna serial not null primary key,
	comuna varchar(200) not null,
	id_region int, foreign key(id_region) references regiones(id_region)
);

create table tipo_autos(
	id_tipo_auto serial not null primary key,
	tipo_auto varchar(200) not null
)


