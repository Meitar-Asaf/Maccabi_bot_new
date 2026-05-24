from fastapi import APIRouter

from app.api.routes import admin, players, subscriptions, webhooks

api_router = APIRouter()
api_router.include_router(subscriptions.router, tags=["subscriptions"])
api_router.include_router(players.router, tags=["players"])
api_router.include_router(admin.router, tags=["admin"])
api_router.include_router(webhooks.router, tags=["webhooks"])
