import reflex as rx
from app.states.raffle_state import RaffleState


def raffle_info() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                "Nombre del Sorteo",
                class_name="block text-sm font-bold text-gray-700 mb-2",
            ),
            rx.el.div(
                rx.icon(
                    "trophy",
                    class_name="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5",
                ),
                rx.el.input(
                    on_change=RaffleState.set_raffle_name,
                    placeholder="Ej. Sorteo de Navidad 2024",
                    class_name="pl-10 w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-violet-500 focus:ring-2 focus:ring-violet-200 transition-all duration-200 outline-none text-gray-800 font-semibold text-lg shadow-sm",
                    default_value=RaffleState.raffle_name,
                ),
                class_name="relative",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-100",
        ),
        class_name="w-full mb-8 animate-fade-in-up",
    )