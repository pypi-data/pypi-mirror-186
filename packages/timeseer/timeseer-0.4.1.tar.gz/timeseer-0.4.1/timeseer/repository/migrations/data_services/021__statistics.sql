--depends: 020__add_data_service_reference

create table Statistics (
    id integer primary key autoincrement,
    data_service_view_evaluation_id integer not null,
    name text not null,
    type text not null,
    value text not null,

    foreign key (data_service_view_evaluation_id) references DataServiceViewEvaluations(id) on delete cascade
)
