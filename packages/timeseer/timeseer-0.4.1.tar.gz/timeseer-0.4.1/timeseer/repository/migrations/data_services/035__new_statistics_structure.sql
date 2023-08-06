-- depends: 034__series_per_evaluation

alter table Statistics rename to CalculatedStatistics;

create table Statistics (
    id integer primary key autoincrement,
    data_service_id integer not null,
    series_id integer not null,
    name text not null,
    type text not null,
    value text not null,

    unique (series_id, data_service_id, name),

    foreign key (data_service_id) references DataServices(id) on delete cascade,
    foreign key (series_id) references Series(id) on delete cascade
)
