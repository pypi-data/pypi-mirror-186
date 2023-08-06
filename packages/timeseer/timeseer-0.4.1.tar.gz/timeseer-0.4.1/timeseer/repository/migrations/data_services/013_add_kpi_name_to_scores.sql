--depends: 012__data_service_bad_actor_kpi_scores

alter table Scores add column kpi_name text;
alter table Subscores add column kpi_name text;
