from dataclasses import dataclass


@dataclass
class WhatsAppResult:
    ok: bool
    provider_message_id: str | None = None
    error: str | None = None


class WhatsAppClient:
    def send_goal_update(self, to_phone: str, text: str, highlight_url: str | None = None) -> WhatsAppResult:
        return WhatsAppResult(ok=True, provider_message_id=f"mock-{to_phone}")
