create table if not exists match_events (
    id uuid primary key default uuid_generate_v4(),
    external_event_id varchar(80) not null unique,
    match_id uuid not null references matches(id) on delete cascade,
    event_type varchar(30) not null,
    team_name varchar(120),
    scorer_name varchar(120),
    minute int,
    payload_json text,
    event_time timestamptz,
    created_at timestamptz not null default now()
);

create index if not exists idx_match_events_match_id on match_events (match_id);
create index if not exists idx_match_events_event_type on match_events (event_type);
