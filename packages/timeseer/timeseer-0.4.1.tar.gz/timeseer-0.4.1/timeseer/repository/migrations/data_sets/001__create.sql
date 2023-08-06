
create table UploadDataSets(
    id integer primary key autoincrement,
    name text not null unique,
    start_date datetime,
    end_date datetime
);

create table UploadDataSetSeries(
    id integer primary key autoincrement,
    upload_data_set_id integer not null,
    series_id text not null,
    start_date datetime,
    end_date datetime,

    foreign key (upload_data_set_id) references UploadDataSets(id) on delete cascade,
    unique (upload_data_set_id, series_id)
)
