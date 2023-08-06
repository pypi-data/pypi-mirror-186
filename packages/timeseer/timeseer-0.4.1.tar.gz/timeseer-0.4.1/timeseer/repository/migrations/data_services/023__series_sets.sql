-- depends: 022__add_analyzed_frame_types
alter table DataServiceViews add column last_evaluation_date datetime;

create table SeriesSetReferences (
    id integer primary key autoincrement,
    data_service_view_id integer not null unique,
    series_set_id integer not null,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);

create table SeriesSetTemplateReferences (
    id integer primary key autoincrement,
    data_service_view_id integer not null unique,
    series_set_template_id integer not null,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);


create table DataSetReferences(
    id integer primary key autoincrement,
    data_service_view_id integer not null unique,
    data_set_id integer not null,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);

create table DataServiceViewContributions(
    id integer primary key autoincrement,
    data_service_view_id integer not null,
    block_evaluation_id integer not null,
    block_type text not null,

    unique(data_service_view_id, block_type),
    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);
