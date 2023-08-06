-- depends: 003__multitenant

create table ApiKeys_new (
    id integer primary key autoincrement,
    name text not null,
    api_key blob not null,
    salt blob not null,
    creation_date datetime not null,

    unique(name)
);

insert into ApiKeys_new (id, name, api_key, salt, creation_date)
select id, name, api_key, salt, creation_date
from ApiKeys;

drop table ApiKeys;

alter table ApiKeys_new rename to ApiKeys;
