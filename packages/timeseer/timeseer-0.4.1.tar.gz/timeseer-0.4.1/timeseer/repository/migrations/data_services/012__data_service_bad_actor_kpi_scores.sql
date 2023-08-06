-- depends: 011__event_frame_data_service_view

create table "DataServiceBadActorKPIScore" (
    id integer primary key autoincrement,
    data_service_view_evaluation_id integer not null,
    series_id text not null,
    start_date datetime not null,
    end_date datetime not null,
    kpi_name text not null,
    state text not null,
    score real not null,

    foreign key (data_service_view_evaluation_id) references DataServiceViewEvaluations(id) on delete cascade
);
