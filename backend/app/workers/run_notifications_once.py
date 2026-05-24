from app.core.database import SessionLocal
from app.integrations.highlight_resolver import HighlightResolver
from app.integrations.sports_client import SportsClient
from app.integrations.whatsapp_client import WhatsAppClient
from app.services.notifications import process_due_jobs


def main() -> None:
    with SessionLocal() as db:
        result = process_due_jobs(db, HighlightResolver(), SportsClient(), WhatsAppClient())
        print(result)


if __name__ == "__main__":
    main()
