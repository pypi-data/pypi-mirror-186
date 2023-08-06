-- depends: 036__reverse_index

CREATE TABLE CalculatedMetadata (
    id integer primary key autoincrement,
    data_service_id integer not null,
    series_id integer not null,
    field_name text not null,
    field_result text,

    unique (series_id, data_service_id, field_name),

    foreign key (data_service_id) references DataServices(id) on delete cascade,
    foreign key (series_id) references Series(id) on delete cascade
);
