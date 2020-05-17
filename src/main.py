from controller.agendaController import AgendaController
from repository.contactRepository import ContactRepository
from ui.console import Console
import os

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""

path = os.path.abspath("contacts.txt")
repo = ContactRepository(path)
ctr = AgendaController(repo)

csl = Console(ctr)
csl.run_ui()
