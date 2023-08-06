 create table SmartTaggings (
    id integer primary key autoincrement,
    series_set_id integer not null unique,
    state text
 );
