import reflex as rx


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("gift", class_name="w-8 h-8 text-white mr-3"),
                rx.el.h1(
                    "Sorteos Fondecom",
                    class_name="text-2xl md:text-3xl font-extrabold text-white tracking-tight",
                ),
                class_name="flex items-center justify-center md:justify-start",
            ),
            rx.el.p(
                "¡Organiza tus sorteos de manera fácil y divertida!",
                class_name="text-purple-100 mt-2 text-sm md:text-base text-center md:text-left font-medium",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6",
        ),
        class_name="w-full bg-gradient-to-r from-violet-600 via-purple-600 to-fuchsia-600 shadow-lg",
    )