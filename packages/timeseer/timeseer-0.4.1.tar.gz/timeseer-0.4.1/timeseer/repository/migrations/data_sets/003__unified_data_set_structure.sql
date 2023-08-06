-- depends: 002__create_dataset_tables

-- alter table DataSets rename to ManagedDataSets;
alter table UploadDataSetSeries rename to TempUploadDataSetSeries;

alter table DataSets add type text not null default "managed";

insert into DataSets (name, help_text, start_date, end_date, type, origin)
select name, "", start_date, end_date, "uploaded", "ui" from UploadDataSets;

create table UploadDataSetSeries(
    id integer primary key autoincrement,
    data_set_id integer not null,
    series_id text not null,
    start_date datetime,
    end_date datetime,

    foreign key (data_set_id) references DataSets(id) on delete cascade,
    unique (data_set_id, series_id)
);

insert into UploadDataSetSeries (data_set_id, series_id, start_date, end_date)
select d.id, ts.series_id, ts.start_date, ts.end_date from TempUploadDataSetSeries ts inner join UploadDataSets u on u.id = ts.upload_data_set_id inner join DataSets d on d.name = u.name;

drop table TempUploadDataSetSeries;
drop table UploadDataSets;
