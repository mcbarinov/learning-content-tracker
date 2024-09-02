from fastapi import APIRouter

from app.app import App


def init(app: App) -> APIRouter:
    router = APIRouter()

    @router.get("/contents/{pk}")
    def get_content(pk: str):
        return app.db.content.get(pk)

    return router
