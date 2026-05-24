create extension if not exists "uuid-ossp";

create table if not exists users (
    id uuid primary key default uuid_generate_v4(),
    phone_e164 varchar(20) not null unique,
    display_name varchar(120),
    whatsapp_status varchar(30) not null default 'pending_opt_in',
    consent_source varchar(40),
    consented_at timestamptz,
    unsubscribed_at timestamptz,
    last_inbound_at timestamptz,
    last_outbound_at timestamptz,
    preferred_language varchar(8) not null default 'he',
    notes text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    check (whatsapp_status in ('pending_opt_in', 'active', 'paused', 'unsubscribed', 'blocked'))
);

create index if not exists idx_users_whatsapp_status on users (whatsapp_status);
