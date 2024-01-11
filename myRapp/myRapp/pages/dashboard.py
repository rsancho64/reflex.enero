"""The dashboard page."""
from myRapp.templates import template

import reflex as rx


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Dashboard", font_size="3em"),
        rx.text("Welcome to Reflex!"), ## <br> doesn't work ! (not that way)
        rx.text("Welcome to"),         ## new
        rx.text("Reflex!"),            ## new
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/dashboard.py"),
            "editada!. vamos a duplicarla..."         ## new
        ),
        rx.text("editada!. vamos a duplicarla..."),   ## new
    )
