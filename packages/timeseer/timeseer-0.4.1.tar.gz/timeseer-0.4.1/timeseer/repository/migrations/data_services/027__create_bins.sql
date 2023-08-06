--depends: 025__analyzed_frame_types_view

create table DataServiceBins(
    id integer primary key autoincrement,
    data_service_view_id integer not null,
    start_date datetime not null,
    end_date datetime not null,

    unique(data_service_view_id, start_date, end_date)
    foreign key (data_service_view_id) references DataServiceViews(id) on delete cascade
);

drop table FavoriteKPIScores;
drop table Scores;
drop table DataServiceBadActorScores;
drop table Subscores;
drop table DataServiceBadActorKpiScore;

CREATE TABLE IF NOT EXISTS FavoriteKPIScores(
    id integer primary key autoincrement,
    bin_id integer not null,
    name integer not null,
    score real,

    unique(bin_id, name, score),
    foreign key (bin_id) references DataServiceBins(id) on delete cascade
);
CREATE TABLE IF NOT EXISTS Scores(
    id integer primary key autoincrement,
    bin_id integer not null,
    series_id text,
    score_name text not null,
    score real not null,
    kpi_name text,

    foreign key (bin_id) references DataServiceBins(id) on delete cascade
);
CREATE TABLE IF NOT EXISTS DataServiceBadActorScores(
    id integer primary key autoincrement,
    bin_id integer not null,
    series_id text,
    start_date datetime not null,
    end_date datetime not null,
    state text not null,
    score real not null,

    foreign key (bin_id) references DataServiceBins(id) on delete cascade
);

CREATE TABLE IF NOT EXISTS Subscores(
    id integer primary key autoincrement,
    bin_id integer not null,
    series_id text,
    subscore_name text not null,
    subscore_result real not null, kpi_name text,

    foreign key (bin_id) references DataServiceBins(id) on delete cascade
);

CREATE TABLE IF NOT EXISTS DataServiceBadActorKPIScore(
    id integer primary key autoincrement,
    bin_id integer not null,
    series_id text not null,
    start_date datetime not null,
    end_date datetime not null,
    kpi_name text not null,
    state text not null,
    score real not null,

    foreign key (bin_id) references DataServiceBins(id) on delete cascade
);


CREATE INDEX scores_bin_id on Scores(bin_id);
CREATE INDEX subscores_bin_id on Subscores(bin_id);
CREATE INDEX event_frame_reference_reference on EventFrameReferences(reference);
