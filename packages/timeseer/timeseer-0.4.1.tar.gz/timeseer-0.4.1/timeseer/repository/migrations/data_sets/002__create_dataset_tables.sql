-- depends: 001__create

create table DataSets(
    id integer primary key autoincrement,
    name text not null unique,
    help_text text,
    start_date datetime,
    end_date datetime,
    origin text,
    removed integer not null default 0
);

create table DataSetSeries(
    id integer primary key autoincrement,
    data_set_id integer not null,
    series_id text not null,

    foreign key (data_set_id) references DataSets(id) on delete cascade,
    unique (data_set_id, series_id)
)
