-- depends: 011__callback_url

alter table BackgroundJobs add column priority integer not null default 0;
