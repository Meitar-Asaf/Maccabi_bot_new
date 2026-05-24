"""Highlight discovery adapter for resolving clip URLs after goal events."""

class HighlightResolver:
    """Stub highlight resolver returning no clip until provider integration is implemented."""

    def find_highlight_url(self, match_external_id: str, scorer_name: str, minute: int) -> str | None:
        """Find a highlight URL for the event context, or return ``None``."""

        return None
