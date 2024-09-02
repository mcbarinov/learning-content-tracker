from fastapi import APIRouter
from mm_base1.jinja import Templates
from mm_base1.utils import depends_form
from starlette.datastructures import FormData
from starlette.requests import Request
from starlette.responses import HTMLResponse
from wtforms import Form
from wtforms.fields.simple import StringField
from wtforms.validators import URL, DataRequired

from app.app import App


class AddContentForm(Form):  # type: ignore
    title = StringField()
    link = StringField(validators=[DataRequired(), URL()])
    content_tags = StringField()
    system_tags = StringField()


def init(app: App, templates: Templates) -> APIRouter:
    router = APIRouter()

    @router.get("/", response_class=HTMLResponse)
    def index_page(req: Request):
        return templates.render(req, "index.j2")

    @router.get("/contents", response_class=HTMLResponse)
    def contents_page(req: Request):
        contents = app.db.content.find({})
        return templates.render(req, "contents.j2", {"contents": contents})

    @router.get("/add", response_class=HTMLResponse)
    def add_page(req: Request):
        form = AddContentForm()
        return templates.render(req, "add.j2", {"form": form})

    @router.post("/add")
    def add_content(form_data: FormData = depends_form):
        form = AddContentForm(form_data)
        if not form.validate():
            return {"errors": form.errors}

        new_content = app.main_service.create_content(
            form.data["title"], form.data["link"], form.data["content_tags"], form.data["system_tags"]
        )

        return new_content

    return router
