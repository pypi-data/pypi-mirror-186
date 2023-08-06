-- depends: 024__change_foreign_keys

drop table AnalyzedFrameTypes;

create table AnalyzedFrameTypes (
    id text primary key,
    data_service_view_id integer not null,
    series_reference string,
    event_frame_type text not null,
    start_date datetime not null,
    end_date datetime,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);
