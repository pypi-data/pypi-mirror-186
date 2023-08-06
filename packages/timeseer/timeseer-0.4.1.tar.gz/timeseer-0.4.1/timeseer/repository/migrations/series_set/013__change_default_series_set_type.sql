-- depends: 012__add_operator_to_tag_and_metadata_patterns

update SeriesSet set origin = 'ui' where origin = 'default';
