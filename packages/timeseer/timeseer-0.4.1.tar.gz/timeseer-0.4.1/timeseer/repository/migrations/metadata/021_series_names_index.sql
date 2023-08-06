-- depends: 020_series_search_index

create index if not exists sn_series_source_removed on SeriesNames(series_source, removed);
