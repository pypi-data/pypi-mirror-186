
create table DataServices(
    id integer primary key autoincrement,
    name text not null unique,
    kpi_set_id not null,
    origin integer not null default 0,
    removed integer not null default 0
);