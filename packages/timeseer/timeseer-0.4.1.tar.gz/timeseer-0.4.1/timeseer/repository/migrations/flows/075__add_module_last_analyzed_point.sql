-- depends: 074__add_data_sets

create table ModuleLastAnalyzedPoints(
    id integer primary key autoincrement,
    block_evaluation_id integer not null,
    series_id integer,
    check_name text not null,
    last_analyzed_point datetime,

    unique(block_evaluation_id, series_id, check_name),
    foreign key (block_evaluation_id) references BlockEvaluations(id) on delete cascade
);
