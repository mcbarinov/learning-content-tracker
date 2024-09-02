from fastapi import APIRouter
from mm_base1.jinja import Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse

from app.app import App


def init(app: App, templates: Templates) -> APIRouter:
    router = APIRouter()

    @router.get("/", response_class=HTMLResponse)
    def index_page(req: Request):
        return templates.render(req, "index.j2")

    @router.get("/contents", response_class=HTMLResponse)
    def contents_page(req: Request):
        contents = app.db.content.find({})
        return templates.render(req, "contents.j2", {"contents": contents})

    return router
