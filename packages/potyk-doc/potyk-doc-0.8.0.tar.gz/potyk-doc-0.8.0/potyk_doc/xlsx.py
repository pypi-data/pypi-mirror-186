import io
from openpyxl import Workbook, load_workbook
from jinja2xlsx import render_xlsx


def render_xlsx_from_html(html) -> io.BytesIO:
    workbook: Workbook = render_xlsx(html)
    workbook.save(stream := io.BytesIO())
    return stream


def xlsx_values(xlsx_stream: io.BytesIO):
    return tuple(load_workbook(xlsx_stream).active.values)

