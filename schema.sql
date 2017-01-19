drop table if exists city_code; 
create table city_code(
	id bigint(20) not null auto_increment, 
	code varchar(32) not null, 
	name varchar(64) not null,
	gmt_create datetime not null, 
	gmt_modified datetime not null,
	primary key(id),
	UNIQUE KEY code_uniq (code)
);