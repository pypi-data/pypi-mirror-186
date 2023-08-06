-- depends: 001__create

create table ProfileDefinitions(
    id integer primary key autoincrement,
    resource_type text not null,
    resource_id integer not null,
    profile_id text not null,

    unique (resource_type, resource_id)
);
