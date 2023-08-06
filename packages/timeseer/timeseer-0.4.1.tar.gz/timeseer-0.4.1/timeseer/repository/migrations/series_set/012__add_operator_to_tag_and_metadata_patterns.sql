-- depends: 011_series_set_template_help_text

alter table SeriesSetTagPatterns add column operator text not null default 'contains';
alter table SeriesSetMetadataPatterns add column operator text not null default 'contains';

update SeriesSetTagPatterns set operator = 'matches regex' from SeriesSetTagPatterns t
inner join SeriesSetPattern p on t.series_set_pattern_id = p.id where p.structured = 1;

update SeriesSetMetadataPatterns set operator = 'matches regex' from SeriesSetMetadataPatterns m
inner join SeriesSetPattern p on m.series_set_pattern_id = p.id where p.structured = 1;


create table new_SeriesSetPattern (
    id integer primary key autoincrement,
    series_set_id integer not null,
    source_name text not null,
    field_pattern text not null,

    foreign key (series_set_id) references SeriesSet(id) on delete cascade
);
insert into new_SeriesSetPattern (id, series_set_id, source_name, field_pattern) 
select id, series_set_id, source_name, field_pattern from SeriesSetPattern;


create table new_SeriesSetTagPatterns (
    id integer primary key autoincrement,
    series_set_pattern_id integer not null,
    pattern_key text not null,
    pattern_value text not null,
    operator text not null,

    unique(series_set_pattern_id, pattern_key, pattern_value),
    foreign key (series_set_pattern_id) references new_SeriesSetPattern(id) on delete cascade
);
insert into new_SeriesSetTagPatterns select * from SeriesSetTagPatterns;


create table new_SeriesSetMetadataPatterns (
    id integer primary key autoincrement,
    series_set_pattern_id integer not null,
    field_name text not null,
    field_value text not null,
    operator text not null,

    unique(series_set_pattern_id, field_name, field_value),
    foreign key (series_set_pattern_id) references new_SeriesSetPattern(id) on delete cascade
);
insert into new_SeriesSetMetadataPatterns select * from SeriesSetMetadataPatterns;


drop table SeriesSetPattern;
drop table SeriesSetTagPatterns;
drop table SeriesSetMetadataPatterns;

alter table new_SeriesSetPattern rename to SeriesSetPattern;
alter table new_SeriesSetTagPatterns rename to SeriesSetTagPatterns;
alter table new_SeriesSetMetadataPatterns rename to SeriesSetMetadataPatterns;