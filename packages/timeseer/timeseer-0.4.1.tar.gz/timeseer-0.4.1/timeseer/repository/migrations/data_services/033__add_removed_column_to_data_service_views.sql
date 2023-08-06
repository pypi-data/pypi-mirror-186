-- depends: 032__add_series_id_to_statistics

alter table DataServiceViews add column removed integer not null default 0; 
