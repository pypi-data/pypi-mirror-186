-- depends: 002__contributions

drop table DataServiceContributions;

create table DataServiceViews (
    id integer primary key autoincrement,
    data_service_id integer not null,
    series_set_name text not null,

    unique(data_service_id, series_set_name),
    foreign key (data_service_id) references DataServices(id) on delete cascade
);

create table DataServiceViewContributions (
    id integer primary key autoincrement,
    data_service_view_id integer not null,
    flow_id integer not null,
    block_evaluation_id integer not null,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);

create table DataServiceViewEvaluations (
    id integer primary key autoincrement,
    data_service_view_id integer not null,
    evaluation_date datetime not null,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);


