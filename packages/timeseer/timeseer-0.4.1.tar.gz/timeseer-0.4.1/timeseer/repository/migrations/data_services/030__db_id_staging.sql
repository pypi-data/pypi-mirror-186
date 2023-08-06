--depends: 029__numerical_id

alter table EventFramesStaging add column db_id;

create index EventFrameDataServiceViews_idx_event_frame_id_data_service_view_id on EventFrameDataServiceViews(event_frame_id, data_service_view_id);
create index EventFrames_idx_type_id on EventFrames(type_id);
