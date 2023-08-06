--depends: 007__remove_constraints

create table EventFrameTypes (

    id integer primary key autoincrement,
    name string not null,
    class string not null,

    unique(name, class)

);

create table EventFrameReferences (

    id integer primary key autoincrement,
    event_frame_id string not null,
    reference string not null,

    unique(event_frame_id, reference),

    foreign key (event_frame_id) references EventFrames(id) on delete cascade

);

create table EventFrames (

    id string primary key,
    data_service_view_id integer not null,
    type_id integer not null,
    start_date datetime not null,
    end_date datetime,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade,
    foreign key (type_id) references EventFrameTypes(id) on delete cascade
);

