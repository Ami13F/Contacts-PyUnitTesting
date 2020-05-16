from controller.agendaController import AgendaController
from repository.contactRepository import ContactRepository
from ui.console import Console
import os

__author__ = 'Team0'

path = os.path.abspath("src/contacte.txt")
repo = ContactRepository(path)
ctr = AgendaController(repo)

csl = Console(ctr)
csl.run_ui()
