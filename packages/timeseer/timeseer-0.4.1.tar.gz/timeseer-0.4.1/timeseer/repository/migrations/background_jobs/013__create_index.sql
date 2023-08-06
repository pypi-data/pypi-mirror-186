-- depends: 011__callback_url

create index BackgroundTasks_idx_job_id on BackgroundTasks(job_id);
create index BackgroundJobReferences_idx_job_id on BackgroundJobReferences(job_id);
create index BackgroundJobDependency_idx_job_id on BackgroundJobDependency(job_id);
create index BackgroundJobCallbacks_idx_job_id on BackgroundJobCallbacks(job_id);
create index BackgroundJobCallbacks_idx_callback_id on BackgroundJobCallbacks(callback_id);
