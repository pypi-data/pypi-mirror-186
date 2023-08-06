-- depends: 009__fix_kpis_resource_origin

alter table KPIWeights add column event_frame_duration text;
