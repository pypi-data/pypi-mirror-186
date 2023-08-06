-- depends: 080__add_blob_reference_to_exports

create table SegmentKeys(
    id integer primary key autoincrement,
    segment_key text not null,

    unique (segment_key)
);

create index segment_keys_key on SegmentKeys(segment_key);

create table SegmentSeries (
    id integer primary key autoincrement,
    series_id text not null,

    unique (series_id)
);

create index segment_series_series on SegmentSeries(series_id);

create table Segments(
    id integer primary key autoincrement,
    block_evaluation_id integer not null,
    segment_key_id integer not null,
    start_date datetime not null,
    end_date datetime not null,

    foreign key (segment_key_id) references SegmentKeys(id),
    foreign key (block_evaluation_id) references BlockEvaluations(id) on delete cascade
);

create index segments_be_id on Segments(block_evaluation_id);

create table SegmentedSeries (
    id integer primary key autoincrement,
    flow_evaluation_series_id integer not null,
    segment_series_id integer not null,

    unique (flow_evaluation_series_id, segment_series_id),
    foreign key (flow_evaluation_series_id) references Series(id) on delete cascade,
    foreign key (segment_series_id) references SegmentSeries(id)
);

create index segmented_series_fe_series_id on SegmentedSeries(flow_evaluation_series_id);

create table Segmentations(
    id integer primary key autoincrement,
    flow_evaluation_id integer not null,
    block_evaluation_id integer not null,
    segment_key_id integer not null,

    unique (flow_evaluation_id),
    foreign key (flow_evaluation_id) references FlowEvaluations(id) on delete cascade,
    foreign key (block_evaluation_id) references BlockEvaluations(id) on delete cascade,
    foreign key (segment_key_id) references SegmentKeys(id)
);

create index segmentations_fe_id on Segmentations(flow_evaluation_id);
create index segmentations_be_id on Segmentations(block_evaluation_id);
