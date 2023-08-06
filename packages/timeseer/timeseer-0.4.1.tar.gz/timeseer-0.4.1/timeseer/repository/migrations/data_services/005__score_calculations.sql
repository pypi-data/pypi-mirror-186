-- depends: 004__time_ranges

create table FavoriteKPIScores(
    id integer primary key autoincrement,
    data_service_view_evaluation_id integer not null,
    name integer not null,
    score real,

    unique(data_service_view_evaluation_id, name, score),
    foreign key (data_service_view_evaluation_id) references DataServiceViewEvaluations(id) on delete cascade
);

create table DataServiceBadActorScore(
    id integer primary key autoincrement,
    data_service_view_evaluation_id integer not null,
    series_id text not null,
    start_date datetime not null,
    end_date datetime not null,
    state text not null,
    score real not null,

    foreign key (data_service_view_evaluation_id) references DataServiceViewEvaluations(id) on delete cascade
);

create table Subscores(
    id integer primary key autoincrement,
    data_service_view_evaluation_id integer not null,
    series_id text,
    subscore_name text not null,
    subscore_result real not null,

    foreign key (data_service_view_evaluation_id) references DataServiceViewEvaluations(id) on delete cascade
);

CREATE TABLE Scores(
    id integer primary key autoincrement,
    data_service_view_evaluation_id integer not null,
    series_id text not null,
    score_name text not null,
    score float not null,

    foreign key (data_service_view_evaluation_id) references DataServiceViewEvaluations(id) on delete cascade
);