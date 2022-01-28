import pdb
from models.skill import Skill
from models.champion import Champion

import repositories.champion_repository as champion_repository
import repositories.skill_repository as skill_repository

champion1 = Champion("Zed the Master of Shadows", "Assassin", "13/11/2012")
champion_repository.save(champion1)

skill1 = Skill("Razor Shuriken", "Living Shadow", "Shadow Slash", "Death Mark")
skill_repository.save(skill1)








pdb.set_trace()
