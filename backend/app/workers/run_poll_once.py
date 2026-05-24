from app.core.database import SessionLocal
from app.integrations.sports_client import SportsClient
from app.services.live_matches import poll_live_matches


def main() -> None:
    with SessionLocal() as db:
        created_jobs = poll_live_matches(db, SportsClient())
        print({"created_jobs": created_jobs})


if __name__ == "__main__":
    main()
