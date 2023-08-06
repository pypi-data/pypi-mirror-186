--depends: 068__add_foreign_keys

create table "UnivariateBadActorKPIScore" (
    id integer primary key autoincrement,
    block_evaluation_id integer not null,
    flow_evaluation_series_id integer not null,
    kpi_name text not null,
    start_date datetime not null,
    end_date datetime not null,
    score real not null, state text not null default 'smell',

    foreign key (block_evaluation_id) references BlockEvaluations(id) on delete cascade
    foreign key (flow_evaluation_series_id) references Series(id) on delete no action
);

create index univariate_bad_actor_kpi_score_fe_id on UnivariateBadActorKPIScore(block_evaluation_id);
