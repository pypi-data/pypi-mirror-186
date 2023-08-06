--depends: 019__index_foreign_keys

drop index event_frame_fe_id;

drop table EventFrames;
delete from DataServiceViews;

create table  EventFrames (
    id text primary key,
    data_service_id integer not null,
    type_id integer not null,
    start_date datetime not null,
    end_date datetime,
    explanation text,
    status text,

    foreign key (data_service_id) references DataServices(id) on delete cascade,
    foreign key (type_id) references EventFrameTypes(id) on delete cascade
);

alter table EventFramesStaging add column data_service_id integer;


