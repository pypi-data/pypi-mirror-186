import io
from openpyxl import Workbook, load_workbook
from jinja2xlsx import render_xlsx

from potyk_doc.models import FileData


def render_xlsx_from_html(html: str, **render_xlsx_kwargs) -> FileData:
    workbook: Workbook = render_xlsx(html, **render_xlsx_kwargs)
    workbook.save(stream := io.BytesIO())
    return stream.getvalue()


def xlsx_values(xlsx_bytes: bytes) -> tuple:
    return tuple(load_workbook(io.BytesIO(xlsx_bytes)).active.values)
