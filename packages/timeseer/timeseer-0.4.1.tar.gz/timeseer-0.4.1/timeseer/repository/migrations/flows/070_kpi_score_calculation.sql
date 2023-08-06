--depends: 069_add_bad_actors_per_kpi

alter table UnivariateScores add column kpi_name text;

create table Subscores(
    id integer primary key autoincrement,
    block_evaluation_id integer not null,
    series_id text,
    subscore_name text not null,
    subscore_result real not null,
    kpi_name text,

    foreign key (block_evaluation_id) references BlockEvaluations(id) on delete cascade
);
