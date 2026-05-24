create table if not exists matches (
    id uuid primary key default uuid_generate_v4(),
    external_match_id varchar(64) not null unique,
    competition_name varchar(120),
    home_team varchar(120) not null,
    away_team varchar(120) not null,
    kickoff_at timestamptz,
    status varchar(30) not null,
    home_score int not null default 0,
    away_score int not null default 0,
    last_polled_at timestamptz,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists idx_matches_status on matches (status);
