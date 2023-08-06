--depends: 017__notifications

create table EventFramesStaging (
    id string primary key,
    type_id integer not null,
    start_date datetime not null,
    end_date datetime,
    event_frame_references text,
    data_service_view_id integer not null

);

CREATE INDEX event_frames_staging_data_service_views_id on EventFramesStaging(data_service_view_id);

