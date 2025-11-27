import reflex as rx
from app.states.raffle_state import RaffleState, Participant


def participant_item(participant: Participant) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    participant["name"][0].upper(),
                    class_name="w-10 h-10 rounded-full bg-violet-100 text-violet-600 flex items-center justify-center font-bold text-lg mr-4 shrink-0",
                ),
                rx.el.div(
                    rx.el.p(
                        participant["name"], class_name="font-semibold text-gray-800"
                    ),
                    rx.cond(
                        participant["contact"] != "",
                        rx.el.p(
                            participant["contact"], class_name="text-sm text-gray-500"
                        ),
                        rx.el.p(
                            "Sin contacto", class_name="text-xs text-gray-400 italic"
                        ),
                    ),
                    class_name="flex flex-col",
                ),
                class_name="flex items-center overflow-hidden",
            ),
            rx.el.button(
                rx.icon("trash-2", class_name="w-5 h-5"),
                on_click=lambda: RaffleState.remove_participant(participant["id"]),
                class_name="text-gray-400 hover:text-red-500 p-2 rounded-full hover:bg-red-50 transition-all ml-2 shrink-0",
            ),
            class_name="flex items-center justify-between w-full p-4 bg-white border border-gray-100 rounded-xl shadow-sm hover:shadow-md transition-shadow",
        ),
        class_name="mb-3 last:mb-0",
    )


def participant_list() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3("Participantes", class_name="text-lg font-bold text-gray-800"),
                rx.el.div(
                    rx.el.span(
                        rx.cond(
                            RaffleState.has_participants,
                            f"{RaffleState.participant_count} total",
                            "0 total",
                        ),
                        class_name="bg-violet-100 text-violet-700 text-xs font-bold px-2 py-1 rounded-full mr-2",
                    ),
                    rx.cond(
                        RaffleState.has_participants,
                        rx.el.button(
                            rx.icon("trash", class_name="w-4 h-4"),
                            "Limpiar",
                            on_click=RaffleState.clear_all_participants,
                            class_name="flex items-center gap-1 text-xs font-medium text-red-500 hover:text-red-700 hover:bg-red-50 px-2 py-1 rounded-lg transition-colors",
                        ),
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex items-center justify-between mb-4",
            ),
            rx.cond(
                RaffleState.has_participants,
                rx.el.ul(
                    rx.foreach(RaffleState.participants, participant_item),
                    class_name="max-h-[500px] overflow-y-auto pr-2 custom-scrollbar",
                ),
                rx.el.div(
                    rx.icon("users", class_name="w-16 h-16 text-gray-200 mb-4"),
                    rx.el.p(
                        "Aún no hay participantes",
                        class_name="text-gray-500 font-medium",
                    ),
                    rx.el.p(
                        "Agrega personas manualmente arriba.",
                        class_name="text-sm text-gray-400 mt-1 text-center",
                    ),
                    class_name="flex flex-col items-center justify-center py-12 border-2 border-dashed border-gray-200 rounded-xl bg-gray-50/50",
                ),
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 h-full",
        ),
        class_name="w-full h-full",
    )