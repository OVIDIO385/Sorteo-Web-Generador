import reflex as rx
from app.states.raffle_state import RaffleState, Participant


def winner_card(participant: Participant) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span("🏆", class_name="text-4xl mb-2 animate-bounce"),
            rx.el.h3(
                participant["name"],
                class_name="text-xl font-bold text-gray-900 text-center",
            ),
            rx.cond(
                participant["contact"] != "",
                rx.el.p(
                    participant["contact"],
                    class_name="text-sm text-gray-500 text-center mt-1",
                ),
            ),
            class_name="flex flex-col items-center justify-center p-6 bg-white border-2 border-yellow-300 rounded-2xl shadow-xl transform hover:scale-105 transition-transform duration-300",
        ),
        class_name="w-full",
    )


def raffle_run() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.cond(
                ~RaffleState.is_drawing,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Ganadores",
                                class_name="text-xs font-bold text-violet-200 uppercase mb-1 block",
                            ),
                            rx.el.input(
                                type="number",
                                default_value=RaffleState.num_winners_to_draw.to_string(),
                                min="1",
                                on_change=RaffleState.set_num_winners,
                                class_name="w-full bg-white/10 border border-violet-400/30 rounded-lg px-3 py-2 text-white font-bold text-center focus:outline-none focus:ring-2 focus:ring-white/50",
                            ),
                            class_name="flex-1",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Cuenta Regresiva (s)",
                                class_name="text-xs font-bold text-violet-200 uppercase mb-1 block",
                            ),
                            rx.el.input(
                                type="number",
                                default_value=RaffleState.countdown_seconds.to_string(),
                                min="0",
                                on_change=RaffleState.set_countdown,
                                class_name="w-full bg-white/10 border border-violet-400/30 rounded-lg px-3 py-2 text-white font-bold text-center focus:outline-none focus:ring-2 focus:ring-white/50",
                            ),
                            class_name="flex-1",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Opciones",
                                class_name="text-xs font-bold text-violet-200 uppercase mb-1 block",
                            ),
                            rx.el.div(
                                rx.el.input(
                                    type="checkbox",
                                    default_checked=RaffleState.exclude_previous_winners,
                                    on_change=RaffleState.toggle_exclude_winners,
                                    class_name="w-4 h-4 rounded border-violet-300 text-violet-600 focus:ring-violet-500 mr-2",
                                ),
                                rx.el.span(
                                    "Excluir ganadores previos",
                                    class_name="text-sm text-violet-100",
                                ),
                                class_name="flex items-center h-10",
                            ),
                            class_name="flex-[2]",
                        ),
                        class_name="flex flex-col md:flex-row gap-4 mb-6",
                    ),
                    rx.el.button(
                        rx.icon("play", class_name="w-6 h-6 mr-2 fill-current"),
                        "¡COMENZAR SORTEO!",
                        on_click=RaffleState.start_raffle,
                        disabled=~RaffleState.has_participants,
                        class_name="w-full bg-yellow-400 hover:bg-yellow-300 text-yellow-900 font-black text-lg py-4 px-8 rounded-xl shadow-lg hover:shadow-xl transform hover:-translate-y-1 active:translate-y-0 transition-all duration-200 flex items-center justify-center disabled:opacity-50 disabled:cursor-not-allowed",
                    ),
                    class_name="animate-fade-in",
                ),
                rx.el.div(
                    rx.el.h2(
                        "¡Buscando Ganador!",
                        class_name="text-2xl font-bold text-white mb-6 animate-pulse",
                    ),
                    rx.el.div(
                        RaffleState.current_display_name,
                        class_name="text-4xl md:text-6xl font-black text-yellow-300 tracking-tight animate-bounce py-12",
                    ),
                    class_name="flex flex-col items-center justify-center text-center py-8",
                ),
            ),
            rx.cond(
                (RaffleState.current_winners.length() > 0) & ~RaffleState.is_drawing,
                rx.el.div(
                    rx.el.h2(
                        "🎉 ¡FELICIDADES! 🎉",
                        class_name="text-3xl font-black text-white text-center mb-8 animate-bounce",
                    ),
                    rx.el.div(
                        rx.foreach(RaffleState.current_winners, winner_card),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-full",
                    ),
                    class_name="mt-8 w-full animate-fade-in-up",
                ),
            ),
            class_name="max-w-5xl mx-auto px-6 py-8",
        ),
        class_name="w-full bg-gradient-to-br from-violet-600 to-purple-800 rounded-3xl shadow-2xl border border-violet-400/20 overflow-hidden mb-8",
    )