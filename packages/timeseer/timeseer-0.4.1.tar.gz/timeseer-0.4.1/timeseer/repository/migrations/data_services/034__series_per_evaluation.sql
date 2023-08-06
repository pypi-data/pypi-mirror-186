-- depends: 033__bins_for_time_range

create table Series (
    id integer primary key autoincrement,
    series_id text no null,

    unique (series_id)
);

create index idx_series_series_id on Series(series_id);

create table DataServiceViewSeries (
    id integer primary key autoincrement,
    data_service_view_id integer not null,
    series_id integer not null,

    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade,
    foreign key (series_id) references Series(id)
);

create index idx_view_series_view on DataServiceViewSeries(data_service_view_id);
