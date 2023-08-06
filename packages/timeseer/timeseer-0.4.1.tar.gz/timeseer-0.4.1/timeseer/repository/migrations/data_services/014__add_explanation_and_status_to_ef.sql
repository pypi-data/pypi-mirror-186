--depends: 013_add_kpi_name_to_scores

alter table EventFrames add column explanation text;
alter table EventFrames add column status text;
