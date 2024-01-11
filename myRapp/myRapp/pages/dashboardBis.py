"""The dashboard page."""
from myRapp.templates import template

import reflex as rx


@template(route="/dashboardBis", title="DashboardBis")
def dashboard() -> rx.Component:
    """The dashboard BIS page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Dashboard BIS", font_size="3em"),
        rx.text("Welcome BIS to Reflex!"), 
        rx.text("Welcome BIS to"),         
        rx.text("Reflex!"), 
        rx.text(
            "You can edit this BISpage in ",
            rx.code("{your_app}/pages/dashboard.py"),
            "duplicada!. " 
        ),
        rx.text("editada!. ya no vamos a duplicarla mas."),   
    )
