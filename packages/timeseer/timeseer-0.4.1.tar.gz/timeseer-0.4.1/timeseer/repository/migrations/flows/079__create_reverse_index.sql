-- depends: 075__add_module_last_analyzed_point

create index FlowEvaluationGroups_idx_removed on FlowEvaluationGroups(removed);
create index FlowEvaluations_idx_group_id on FlowEvaluations(group_id);

create index block_evaluations_fe_id on BlockEvaluations(flow_evaluation_id);
create index block_evaluation_runs_be_id on BlockEvaluationRuns(block_evaluation_id);
create index CheckConditionMessages_idx_be_id on CheckConditionMessages(block_evaluation_id);
create index ExcelExports_idx_be_id on ExcelExports(block_evaluation_id);
create index FlowDataService_idx_be_id on FlowDataService(block_evaluation_id);
create index FlowSource_idx_be_id on FlowSource(block_evaluation_id);
create index Series_idx_fe_id on Series(flow_evaluation_id);
create index SeriesTags_idx_es_id on SeriesTags(evaluation_series_id);
create index Subscores_idx_be_id on Subscores(block_evaluation_id);
create index UnivariateBadActorScore_idx_be_id on UnivariateBadActorScore(block_evaluation_id);
