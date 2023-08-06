-- depends: 008__series_set_template_tag_patterns

create table SeriesSetMetadataPatterns (
    id integer primary key autoincrement,
    series_set_pattern_id integer not null,
    field_name text not null,
    field_value text not null,

    unique(series_set_pattern_id, field_name, field_value),
    foreign key (series_set_pattern_id) references SeriesSetPattern(id) on delete cascade
);
