-- depends: 075__add_module_last_analyzed_point

CREATE TABLE temp_Exports (
    id integer primary key autoincrement,
    block_evaluation_id integer not null,
    filename text not null,
    file blob,
    date datetime not null,
    file_type text default 'excel',

    foreign key (block_evaluation_id) references BlockEvaluations(id) on delete cascade
);


insert into temp_Exports select * from Exports;

drop table Exports;

alter table temp_Exports rename to Exports;

CREATE INDEX exports_fe_id on Exports(block_evaluation_id);
