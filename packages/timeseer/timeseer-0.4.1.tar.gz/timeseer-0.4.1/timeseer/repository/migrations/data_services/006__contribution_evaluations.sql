-- depends: 005__score_calculations

create table DataServiceViewEvaluationContributions (
    id integer primary key autoincrement,
    data_service_view_evaluation_id integer not null,
    block_evaluation_id integer not null,

    foreign key (data_service_view_evaluation_id) references DataServiceViewEvaluations(id) on delete cascade
);



