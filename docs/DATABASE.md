# Database Reference (PostgreSQL)

Schema SQL files are located in `infra/schema`.
Apply them in numeric order.

## Tables

## `users`
Subscriber records and WhatsApp state.

Key columns:
- `id` (uuid, PK)
- `phone_e164` (unique)
- `whatsapp_status` (`pending_opt_in|active|paused|unsubscribed|blocked`)
- `consent_source`, `consented_at`, `unsubscribed_at`
- `last_inbound_at`, `last_outbound_at`

Indexes:
- `phone_e164` unique
- `whatsapp_status`

## `players`
Player metadata and season statistics.

Key columns:
- `external_player_id` (unique)
- `full_name`, `position`, `photo_url`
- `is_active`, `is_loaned_out`
- `games_played`, `goals_scored`, `successful_tackles`, `successful_passes`

Filtering rule used by API:
- active page includes only `is_active = true AND is_loaned_out = false`.

## `matches`
Tracked fixtures and live state.

Key columns:
- `external_match_id` (unique)
- teams, kickoff, status, score, `last_polled_at`

## `match_events`
Per-event records from sports provider.

Key columns:
- `external_event_id` (unique, dedupe key)
- `match_id` FK -> `matches.id`
- `event_type`, `scorer_name`, `minute`, `event_time`

## `notification_jobs`
Delayed and retryable outbound notification jobs.

Key columns:
- `match_event_id` unique FK
- `status` (`queued|processing|retry|sent|completed_without_highlight|failed`)
- `run_after`, `attempt_count`, `max_attempts`

## `message_deliveries`
Per-user delivery log for each job.

Key columns:
- `notification_job_id` FK
- `user_id` FK
- `status`, `provider_message_id`, `error_text`, `sent_at`

Constraints:
- unique `(notification_job_id, user_id)` to prevent duplicate sends.

## Example Queries
### Active subscribers
```sql
select id, phone_e164
from users
where whatsapp_status = 'active';
```

### Due jobs
```sql
select id, match_event_id
from notification_jobs
where status in ('queued', 'retry')
  and run_after <= now();
```

### Active players for UI
```sql
select full_name, goals_scored, games_played, successful_tackles, successful_passes
from players
where is_active = true
  and is_loaned_out = false
order by full_name;
```
