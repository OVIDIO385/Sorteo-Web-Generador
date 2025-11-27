import reflex as rx
from app.components.header import header
from app.components.raffle_info import raffle_info
from app.components.participant_form import participant_form
from app.components.participant_list import participant_list
from app.components.raffle_run import raffle_run
from app.states.raffle_state import RaffleState


def index() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.main(
            rx.el.div(
                raffle_info(),
                raffle_run(),
                rx.el.div(
                    rx.el.div(participant_form(), class_name="w-full lg:w-5/12"),
                    rx.el.div(participant_list(), class_name="w-full lg:w-7/12"),
                    class_name="flex flex-col lg:flex-row gap-8 items-start",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
            ),
            class_name="flex-1 w-full",
        ),
        class_name="min-h-screen bg-gray-50 font-['Inter'] flex flex-col",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
    ],
    head_components=[
        rx.el.script(
            src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"
        )
    ],
)
app.add_page(index, route="/")