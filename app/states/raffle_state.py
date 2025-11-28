import reflex as rx
import logging
from typing import TypedDict
import uuid
import openpyxl
import asyncio
import random


class Participant(TypedDict):
    id: str
    name: str
    contact: str


class RaffleState(rx.State):
    raffle_name: str = "Escribe el nombre del sorteo aquí"
    participants: list[Participant] = []
    new_participant_name: str = ""
    new_participant_contact: str = ""
    num_winners_to_draw: int = 1
    countdown_seconds: int = 3
    exclude_previous_winners: bool = False
    is_drawing: bool = False
    current_display_name: str = "???"
    current_winners: list[Participant] = []
    all_winner_ids: list[str] = []

    @rx.var
    def participant_count(self) -> int:
        return len(self.participants)

    @rx.var
    def has_participants(self) -> bool:
        return len(self.participants) > 0

    @rx.var
    def eligible_count(self) -> int:
        if self.exclude_previous_winners:
            return len(
                [p for p in self.participants if p["id"] not in self.all_winner_ids]
            )
        return len(self.participants)

    @rx.event
    def set_raffle_name(self, name: str):
        self.raffle_name = name

    @rx.event
    def set_new_participant_name(self, name: str):
        self.new_participant_name = name

    @rx.event
    def set_new_participant_contact(self, contact: str):
        self.new_participant_contact = contact

    @rx.event
    def set_num_winners(self, num: str):
        try:
            val = int(num)
            if val > 0:
                self.num_winners_to_draw = val
        except ValueError as e:
            logging.exception(f"Error setting num winners: {e}")

    @rx.event
    def set_countdown(self, sec: str):
        try:
            val = int(sec)
            if val >= 0:
                self.countdown_seconds = val
        except ValueError as e:
            logging.exception(f"Error setting countdown: {e}")

    @rx.event
    def toggle_exclude_winners(self, checked: bool):
        self.exclude_previous_winners = checked

    @rx.event
    def add_participant(self):
        if self.new_participant_name.strip() == "":
            return rx.toast.error("El nombre del participante es obligatorio.")
        new_p: Participant = {
            "id": str(uuid.uuid4()),
            "name": self.new_participant_name,
            "contact": self.new_participant_contact,
        }
        self.participants.append(new_p)
        self.new_participant_name = ""
        self.new_participant_contact = ""
        return rx.toast.success("Participante agregado correctamente.")

    @rx.event
    def remove_participant(self, p_id: str):
        self.participants = [p for p in self.participants if p["id"] != p_id]
        return rx.toast.info("Participante eliminado.")

    @rx.event
    def clear_all_participants(self):
        self.participants = []
        self.all_winner_ids = []
        self.current_winners = []
        return rx.toast.info("Lista de participantes limpiada.")

    @rx.event(background=True)
    async def start_raffle(self):
        async with self:
            if len(self.participants) < 2:
                rx.toast.error("Necesitas al menos 2 participantes para sortear.")
                return
            eligible = self.participants
            if self.exclude_previous_winners:
                eligible = [
                    p for p in self.participants if p["id"] not in self.all_winner_ids
                ]
            if len(eligible) < self.num_winners_to_draw:
                rx.toast.error(
                    f"No hay suficientes participantes elegibles ({len(eligible)}) para {self.num_winners_to_draw} ganador(es)."
                )
                return
            self.is_drawing = True
            self.current_winners = []
        ticks = max(10, self.countdown_seconds * 10)
        for _ in range(ticks):
            async with self:
                if self.participants:
                    self.current_display_name = random.choice(self.participants)["name"]
            await asyncio.sleep(0.1)
        async with self:
            eligible_pool = self.participants
            if self.exclude_previous_winners:
                eligible_pool = [
                    p for p in self.participants if p["id"] not in self.all_winner_ids
                ]
            count = min(len(eligible_pool), self.num_winners_to_draw)
            if count > 0:
                winners = random.sample(eligible_pool, count)
                self.current_winners = winners
                for w in winners:
                    self.all_winner_ids.append(w["id"])
                yield rx.call_script(
                    "confetti({particleCount: 150, spread: 70, origin: { y: 0.6 }})"
                )
            else:
                rx.toast.error("Error al seleccionar ganadores.")
            self.is_drawing = False

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        upload_dir = rx.get_upload_dir()
        upload_dir.mkdir(parents=True, exist_ok=True)
        count_success = 0
        count_failed = 0
        for file in files:
            try:
                upload_data = await file.read()
                file_path = upload_dir / file.name
                with file_path.open("wb") as f:
                    f.write(upload_data)
                wb = openpyxl.load_workbook(file_path)
                sheet = wb.active
                is_first_row = True
                for row in sheet.iter_rows(values_only=True):
                    if not row or all((cell is None for cell in row)):
                        continue
                    name = str(row[0]).strip() if row[0] else ""
                    contact = str(row[1]).strip() if len(row) > 1 and row[1] else ""
                    if not name:
                        count_failed += 1
                        continue
                    if is_first_row:
                        if name.lower() in [
                            "nombre",
                            "name",
                            "nombres",
                            "participante",
                        ]:
                            is_first_row = False
                            continue
                        is_first_row = False
                    self.participants.append(
                        {"id": str(uuid.uuid4()), "name": name, "contact": contact}
                    )
                    count_success += 1
            except Exception as e:
                logging.exception(f"Error reading file {file.name}: {e}")
                return rx.toast.error(f"Error procesando {file.name}: {str(e)}")
        if count_success > 0:
            return rx.toast.success(f"Se importaron {count_success} participantes.")
        elif count_failed > 0:
            return rx.toast.warning(
                f"No se encontraron participantes válidos. {count_failed} filas ignoradas."
            )
        else:
            return rx.toast.info("No se procesaron datos.")