-- depends: 003__contribution_evaluations

alter table DataServices add column start_date datetime;
alter table DataServices add column end_date datetime;
alter table DataServices add column relative_date text;