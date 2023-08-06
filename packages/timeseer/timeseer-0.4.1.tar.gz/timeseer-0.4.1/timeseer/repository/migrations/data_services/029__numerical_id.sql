-- depends: 028__change_relative_date

create table EventFrames2 (
    id integer primary key autoincrement,
    data_service_id integer not null,
    event_frame_id text not null,
    type_id integer not null,
    start_date datetime not null,
    end_date datetime,
    explanation text,
    status text,

    unique(event_frame_id),
    foreign key (data_service_id) references DataServices(id) on delete cascade,
    foreign key (type_id) references EventFrameTypes(id) on delete cascade
);

create table EventFrameReferences2 (
    id integer primary key autoincrement,
    event_frame_id integer not null,
    data_service_id integer not null,
    reference string,

    unique(event_frame_id, reference),
    foreign key (event_frame_id) references EventFrames2(id) on delete cascade
);

create table EventFrameDataServiceViews2 (
    id integer primary key autoincrement,
    event_frame_id integer not null,
    data_service_view_id integer not null,

    unique(event_frame_id, data_service_view_id),
    foreign key (event_frame_id) references EventFrames2(id) on delete cascade,
    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);

insert into EventFrames2 (data_service_id, event_frame_id, type_id, start_date, end_date)
select data_service_id, id, type_id, start_date, end_date
from EventFrames;

insert into EventFrameReferences2 (event_frame_id, data_service_id, reference)
select e.id, e.data_service_id, r.reference
from EventFrames2 e left join EventFrameReferences r on e.event_frame_id = r.event_frame_id;

insert into EventFrameDataServiceViews2 (event_frame_id, data_service_view_id)
select e.id, v.data_service_view_id
from EventFrameDataServiceViews v, EventFrames2 e
where v.event_frame_id = e.event_frame_id;

drop table EventFrameDataServiceViews;
drop table EventFrameReferences;
drop table EventFrames;

alter table EventFrames2 rename to EventFrames;
alter table EventFrameReferences2 rename to EventFrameReferences;
alter table EventFrameDataServiceViews2 rename to EventFrameDataServiceViews;

create index EventFrames_idx_event_frame_id on EventFrames(event_frame_id);
create index EventFrameReferences_idx_data_service_reference on EventFrameReferences(data_service_id, reference);
create index EventFrameDataServiceViews_idx_id on EventFrameDataServiceViews(data_service_view_id);

create index EventFrames_idx_data_service_id on EventFrames(data_service_id);
create index EventFrameReferences_idx_data_service_id on EventFrameReferences(data_service_id);
create index EventFrameDataServiceViews_idx_event_frame_id on EventFrameDataServiceViews(event_frame_id);
