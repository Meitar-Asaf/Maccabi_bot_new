"""WhatsApp outbound adapter and send-result contract."""

from dataclasses import dataclass


@dataclass
class WhatsAppResult:
    """Normalized outbound message send result from provider adapters."""

    ok: bool
    provider_message_id: str | None = None
    error: str | None = None


class WhatsAppClient:
    """Stub WhatsApp client used for local and integration scaffolding."""

    def send_goal_update(self, to_phone: str, text: str, highlight_url: str | None = None) -> WhatsAppResult:
        """Send one goal-update message to a single subscriber."""

        return WhatsAppResult(ok=True, provider_message_id=f"mock-{to_phone}")
