-- depends: 030__db_id_staging

alter table DataServices add column unit text;
alter table DataServices add column "window" integer;
alter table DataServices rename column relative_date to relative_type;
