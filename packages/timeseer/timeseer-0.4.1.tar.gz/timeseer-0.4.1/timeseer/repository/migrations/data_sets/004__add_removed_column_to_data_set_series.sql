-- depends: 003__unified_data_set_structure

alter table DataSetSeries add removed integer not null default 0;  
alter table UploadDataSetSeries add removed integer not null default 0;  
