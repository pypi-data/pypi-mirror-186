-- depends: 035__new_statistics_structure


create index DataServiceBadActorKPIScore_idx_bin_id_series_id on DataServiceBadActorKPIScore(bin_id, series_id);
create index DataServiceBadActorScores_idx_bin_id_series_id on DataServiceBadActorScores(bin_id, series_id);
