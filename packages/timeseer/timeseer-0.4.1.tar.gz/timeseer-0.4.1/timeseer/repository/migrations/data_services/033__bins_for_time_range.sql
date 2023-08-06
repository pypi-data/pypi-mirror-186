-- depends: 032__add_series_id_to_statistics

alter table DataServices add column number_of_bins integer;

update DataServices set number_of_bins = 24 where unit = 'minutes' and relative_type = 'Most recent results';
update DataServices set number_of_bins = 30 where unit = 'hours' and relative_type = 'Most recent results';
update DataServices set number_of_bins = 52 where unit = 'days' and relative_type = 'Most recent results' and window < 30;
update DataServices set number_of_bins = 156 where unit = 'days' and relative_type = 'Most recent results' and window >= 30;


update DataServices set number_of_bins = 24 where unit = 'hours' and relative_type = 'Last calendar';
update DataServices set number_of_bins = 30 where unit = 'days' and relative_type = 'Last calendar';
update DataServices set number_of_bins = 52 where unit = 'weeks' and relative_type = 'Last calendar';
update DataServices set number_of_bins = 156 where unit = 'months' and relative_type = 'Last calendar';
