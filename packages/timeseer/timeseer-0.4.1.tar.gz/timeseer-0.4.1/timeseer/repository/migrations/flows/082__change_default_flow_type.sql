-- depends: 081__fix_incorrect_data_set_relative_date_in_flow

update Flows set origin = 'ui' where origin = 'default';
