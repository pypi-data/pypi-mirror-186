--depends: 021__statistics

create table AnalyzedFrameTypes (
    id text primary key,
    data_service_id integer not null,
    series_reference string not null,
    event_frame_type text not null,
    start_date datetime not null,
    end_date datetime,

    foreign key (data_service_id) references DataServices(id) on delete cascade
)
