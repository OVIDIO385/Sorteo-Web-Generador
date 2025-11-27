import reflex as rx
from app.states.raffle_state import RaffleState


def participant_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Agregar Participante",
                class_name="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Nombre Completo *",
                        class_name="text-xs font-semibold text-gray-500 uppercase mb-1 block",
                    ),
                    rx.el.input(
                        on_change=RaffleState.set_new_participant_name,
                        placeholder="Juan Pérez",
                        class_name="w-full px-4 py-2 rounded-lg border border-gray-200 focus:border-violet-500 focus:ring-2 focus:ring-violet-200 outline-none transition-all text-gray-700",
                        default_value=RaffleState.new_participant_name,
                    ),
                    class_name="flex-1",
                ),
                rx.el.div(
                    rx.el.label(
                        "Email / Contacto (Opcional)",
                        class_name="text-xs font-semibold text-gray-500 uppercase mb-1 block",
                    ),
                    rx.el.input(
                        on_change=RaffleState.set_new_participant_contact,
                        placeholder="juan@email.com",
                        class_name="w-full px-4 py-2 rounded-lg border border-gray-200 focus:border-violet-500 focus:ring-2 focus:ring-violet-200 outline-none transition-all text-gray-700",
                        default_value=RaffleState.new_participant_contact,
                    ),
                    class_name="flex-1",
                ),
                class_name="flex flex-col md:flex-row gap-4 mb-6",
            ),
            rx.el.button(
                rx.icon("plus", class_name="w-5 h-5 mr-2"),
                "Agregar a la Lista",
                on_click=RaffleState.add_participant,
                class_name="w-full bg-violet-600 hover:bg-violet-700 text-white font-bold py-3 px-6 rounded-xl transition-colors shadow-md hover:shadow-lg flex items-center justify-center active:scale-95 transform duration-100",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(class_name="w-full border-t border-gray-200"),
                    rx.el.span(
                        "O IMPORTAR EXCEL",
                        class_name="px-3 text-xs font-bold text-gray-400 uppercase bg-white whitespace-nowrap",
                    ),
                    rx.el.span(class_name="w-full border-t border-gray-200"),
                    class_name="flex items-center my-6",
                ),
                rx.upload.root(
                    rx.el.div(
                        rx.icon(
                            "cloud-upload", class_name="w-8 h-8 text-violet-400 mb-2"
                        ),
                        rx.el.p(
                            "Arrastra un archivo Excel o haz clic",
                            class_name="text-sm text-gray-600 font-medium",
                        ),
                        rx.el.p(
                            "Formatos: .xlsx, .xls (Col A: Nombre)",
                            class_name="text-xs text-gray-400 mt-1",
                        ),
                        class_name="flex flex-col items-center justify-center p-6 border-2 border-dashed border-violet-200 rounded-xl bg-violet-50/30 hover:bg-violet-50 transition-colors cursor-pointer text-center",
                    ),
                    id="upload_participants",
                    accept={
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [
                            ".xlsx"
                        ],
                        "application/vnd.ms-excel": [".xls"],
                    },
                    multiple=False,
                    class_name="w-full",
                ),
                rx.el.div(
                    rx.foreach(
                        rx.selected_files("upload_participants"),
                        lambda file: rx.el.div(
                            rx.icon(
                                "file-spreadsheet",
                                class_name="w-4 h-4 text-green-600 mr-2",
                            ),
                            rx.el.span(
                                file, class_name="text-sm text-gray-700 truncate"
                            ),
                            class_name="flex items-center p-2 bg-green-50 border border-green-100 rounded-lg mt-2",
                        ),
                    ),
                    class_name="w-full",
                ),
                rx.el.button(
                    rx.icon("upload", class_name="w-4 h-4 mr-2"),
                    "Cargar Archivo",
                    on_click=RaffleState.handle_upload(
                        rx.upload_files(upload_id="upload_participants")
                    ),
                    class_name="w-full mt-3 bg-white hover:bg-gray-50 text-gray-700 font-bold py-2 px-4 rounded-xl border border-gray-200 transition-colors shadow-sm text-sm flex items-center justify-center",
                ),
                class_name="mt-4",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 h-fit",
        ),
        class_name="w-full",
    )