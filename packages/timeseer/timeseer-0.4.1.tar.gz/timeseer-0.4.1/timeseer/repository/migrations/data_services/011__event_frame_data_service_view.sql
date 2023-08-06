-- depends: 010__drop_view_contributions

create table new_EventFrames(
    id string primary key,
    type_id integer not null,
    start_date datetime not null,
    end_date datetime,

    foreign key (type_id) references EventFrameTypes(id) on delete cascade
);

insert into new_EventFrames (id, type_id, start_date, end_date)
select id, type_id, start_date, end_date from EventFrames where true on conflict do nothing;

create table EventFrameDataServiceViews (
    id integer primary key autoincrement,
    event_frame_id text not null,
    data_service_view_id integer not null,

    unique(event_frame_id, data_service_view_id),
    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);

insert into EventFrameDataServiceViews (event_frame_id, data_service_view_id)
select id, data_service_view_id from EventFrames;

create table temp_EventFrameReferences (

    id integer primary key autoincrement,
    event_frame_id string not null,
    reference string not null,

    unique(event_frame_id, reference)
);

insert into temp_EventFrameReferences select * from EventFrameReferences;

drop table EventFrames;
drop table EventFrameReferences;

alter table new_EventFrames rename to EventFrames;

create table EventFrameReferences (

    id integer primary key autoincrement,
    event_frame_id string not null,
    reference string not null,

    unique(event_frame_id, reference),

    foreign key (event_frame_id) references EventFrames(id) on delete cascade

);

insert into EventFrameReferences select * from temp_EventFrameReferences where id in (select distinct id from EventFrames);

drop table temp_EventFrameReferences;




