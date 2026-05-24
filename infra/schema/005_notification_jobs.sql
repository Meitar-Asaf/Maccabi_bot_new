create table if not exists notification_jobs (
    id uuid primary key default uuid_generate_v4(),
    match_event_id uuid not null unique references match_events(id) on delete cascade,
    job_type varchar(40) not null default 'goal_highlight',
    status varchar(30) not null default 'queued',
    run_after timestamptz not null,
    attempt_count int not null default 0,
    max_attempts int not null default 4,
    payload_json text,
    last_error text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    check (status in ('queued', 'processing', 'retry', 'sent', 'completed_without_highlight', 'failed'))
);

create index if not exists idx_notification_jobs_status on notification_jobs (status);
create index if not exists idx_notification_jobs_run_after on notification_jobs (run_after);
