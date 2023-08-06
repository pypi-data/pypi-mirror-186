-- depends: 080__add_blob_reference_to_exports

update Flows set relative_date = NULL where id not in (select flow_id from DataSetReferences) and relative_date = 'data_set';

