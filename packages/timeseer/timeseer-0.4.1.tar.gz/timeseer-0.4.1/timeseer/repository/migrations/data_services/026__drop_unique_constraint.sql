-- depends: 025__analyzed_frame_types_view

create table new_SeriesSetReferences (
    id integer primary key autoincrement,
    data_service_view_id integer not null,
    series_set_id integer not null,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);

insert into new_SeriesSetReferences (id, data_service_view_id, series_set_id)
select id, data_service_view_id, series_set_id from SeriesSetReferences;

drop table SeriesSetReferences;

alter table new_SeriesSetReferences rename to SeriesSetReferences
