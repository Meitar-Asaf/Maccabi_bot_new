create table if not exists players (
    id uuid primary key default uuid_generate_v4(),
    external_player_id varchar(64) not null unique,
    full_name varchar(150) not null,
    short_name varchar(80),
    shirt_number int,
    position varchar(40) not null,
    photo_url varchar(500),
    team_name varchar(120) not null default 'Maccabi Tel Aviv',
    parent_club varchar(120),
    current_club varchar(120) not null default 'Maccabi Tel Aviv',
    is_active boolean not null default true,
    is_loaned_out boolean not null default false,
    season varchar(12) not null,
    games_played int not null default 0,
    goals_scored int not null default 0,
    successful_tackles int not null default 0,
    successful_passes int not null default 0,
    source_updated_at timestamptz,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists idx_players_active on players (is_active);
create index if not exists idx_players_loaned_out on players (is_loaned_out);
create index if not exists idx_players_season on players (season);
