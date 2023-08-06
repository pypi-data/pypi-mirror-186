-- depends: 073__flow_help_text

create table DataSetReferences(
    id integer primary key autoincrement,
    flow_id integer not null,
    data_set_id integer not null,

    foreign key (flow_id) references Flows(id) on delete cascade,
    unique (flow_id, data_set_id)
);
