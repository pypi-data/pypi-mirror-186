--depends: 070_kpi_score_calculation

update Flows set schedule_interval = null;

alter table Flows add schedule_frequency integer;
