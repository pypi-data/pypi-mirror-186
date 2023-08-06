-- depends: 001__create

create table DataServiceContributions (
    id integer primary key autoincrement,
    data_service_id integer not null,
    flow_id integer not null,
    block_evaluation_id integer not null,

    unique(data_service_id, flow_id, block_evaluation_id),
    foreign key (data_service_id) references DataServices(id) on delete cascade
);