-- depends: 008__event_frames

CREATE TABLE ExcelExports (
    id integer primary key autoincrement,
    view_evaluation_id integer not null,
    series_id text not null,
    filename text,
    file blob,
    date datetime,
    type text,
    start_date datetime,
    end_date datetime,

    foreign key (view_evaluation_id) references DataServiceViewEvaluations(id) on delete cascade
);

CREATE TABLE ExcelExport_EventFrames (
    id integer primary key autoincrement,
    excel_export_id int not null,
    frame_type text not null,

    foreign key (excel_export_id) references ExcelExports(id) on delete cascade
);
