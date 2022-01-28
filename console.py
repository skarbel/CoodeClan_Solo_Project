import pdb
from models.skill import Skill
from models.champion import Champion

import repositories.champion_repository as champion_repository
import repositories.skill_repository as skill_repository

#-----------------------------Champion Pool-----------------------------
champion1 = Champion("Zed", "the Master of Shadows", "Assassin", "13/11/2012")
champion_repository.save(champion1)

champion2 = Champion("Anivia", "the Cryophoenix", "Battle Mage", "10/07/2009")
champion_repository.save(champion2)

champion3 = Champion("Leona", "the Radiant Dawn", "Vanguard", "13/17/2011")
champion_repository.save(champion3)

champion4 = Champion("Ziggs", "the Hexplosives Expert", "Artillery", "01/02/2012")
champion_repository.save(champion4)

champion5 = Champion("Ashe", "the Frost Archer", "Marksman", "21/02/2009")
champion_repository.save(champion5)

champion6 = Champion("Renekton", "the Butcher of the Sands", "Diver", "18/01/2011")
champion_repository.save(champion6)

champion7 = Champion("Urgot", "the Dreadnought", "Juggernaut", "24/08/2010")
champion_repository.save(champion7)

champion8 = Champion("Shaco", "the Demon Jester", "Assassin", "10/10/2009")
champion_repository.save(champion8)


#-----------------------------Skill Pool-----------------------------
skill1 = Skill(champion1, "Razor Shuriken", "Q")
skill_repository.save(skill1)

skill2 = Skill(champion1, "Living Shadow", "W")
skill_repository.save(skill2)

skill3 = Skill(champion1, "Shadow Slash", "E")
skill_repository.save(skill3)

skill4 = Skill(champion1, "Death Mark", "R")
skill_repository.save(skill4)


skill5 = Skill(champion2, "Flash Frost", "Q")
skill_repository.save(skill5)

skill6 = Skill(champion2, "Crystallize", "W")
skill_repository.save(skill6)

skill7 = Skill(champion2, "Frostbite", "E")
skill_repository.save(skill7)

skill8 = Skill(champion2, "Glacial Storm", "R")
skill_repository.save(skill8)


skill9 = Skill(champion3, "Shield of Daybreak", "Q")
skill_repository.save(skill9)

skill10 = Skill(champion3, "Eclipse", "W")
skill_repository.save(skill10)

skill11 = Skill(champion3, "Zenith Blade", "E")
skill_repository.save(skill11)

skill12 = Skill(champion3, "Solar Flare", "R")
skill_repository.save(skill12)


skill13 = Skill(champion4, "Bouncing Bomb", "Q")
skill_repository.save(skill13)

skill14 = Skill(champion4, "Satchel Charge", "W")
skill_repository.save(skill14)

skill15 = Skill(champion4, "Hexplosive Minefield", "E")
skill_repository.save(skill15)

skill16 = Skill(champion4, "Mega Inferno Bomb", "R")
skill_repository.save(skill16)


skill17 = Skill(champion5, "Ranger's Focus", "Q")
skill_repository.save(skill17)

skill18 = Skill(champion5, "Volley", "W")
skill_repository.save(skill18)

skill19 = Skill(champion5, "Hawkshot", "E")
skill_repository.save(skill19)

skill20 = Skill(champion5, "Menchanted Crystal Arrow", "R")
skill_repository.save(skill20)


skill21 = Skill(champion6, "Cull the Meek", "Q")
skill_repository.save(skill21)

skill22 = Skill(champion6, "Ruthless Predator", "W")
skill_repository.save(skill22)

skill23 = Skill(champion6, "Slice & Dice", "E")
skill_repository.save(skill23)

skill24 = Skill(champion6, "Dominus", "R")
skill_repository.save(skill24)


skill25 = Skill(champion7, "Corrosive Charge", "Q")
skill_repository.save(skill25)

skill26 = Skill(champion7, "Purge", "W")
skill_repository.save(skill26)

skill27 = Skill(champion7, "Disdain", "E")
skill_repository.save(skill27)

skill28 = Skill(champion7, "Fear Beyond Death", "R")
skill_repository.save(skill28)


skill29 = Skill(champion8, "Deceive", "Q")
skill_repository.save(skill29)

skill30 = Skill(champion8, "Jack in the Box", "W")
skill_repository.save(skill30)

skill31 = Skill(champion8, "Two-Shiv Poison", "E")
skill_repository.save(skill31)

skill32 = Skill(champion8, "Hallucinate", "R")
skill_repository.save(skill32)



# pdb.set_trace()
