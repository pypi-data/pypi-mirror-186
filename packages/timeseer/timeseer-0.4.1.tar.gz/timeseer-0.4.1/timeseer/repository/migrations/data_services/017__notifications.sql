--depends: 016__data_service_help_text

alter table DataServices add column notify text default '[]';
