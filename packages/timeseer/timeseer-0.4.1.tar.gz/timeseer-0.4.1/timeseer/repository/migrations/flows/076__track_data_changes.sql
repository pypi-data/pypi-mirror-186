-- depends: 075__add_module_last_analyzed_point

create table DataChanges(
    id integer primary key autoincrement,
    flow_evaluation_id integer not null,
    series_id integer not null,
    changed integer,

    unique(flow_evaluation_id, series_id),
    foreign key (flow_evaluation_id) references FlowEvaluations(id) on delete cascade
);

create index data_changes_be_id on DataChanges(flow_evaluation_id);

create index last_analyzed_points_be_id on ModuleLastAnalyzedPoints(block_evaluation_id);
