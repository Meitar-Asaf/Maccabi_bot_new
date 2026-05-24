create table if not exists message_deliveries (
    id uuid primary key default uuid_generate_v4(),
    notification_job_id uuid not null references notification_jobs(id) on delete cascade,
    user_id uuid not null references users(id) on delete cascade,
    provider_message_id varchar(120),
    status varchar(30) not null default 'pending',
    error_text text,
    sent_at timestamptz,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    unique(notification_job_id, user_id)
);

create index if not exists idx_message_deliveries_notification_job_id on message_deliveries (notification_job_id);
create index if not exists idx_message_deliveries_status on message_deliveries (status);
