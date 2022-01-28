# class Skill:
#     def __init__(self, champion, skill_Q, skill_W, skill_E, skill_R, id = None):
#         self.champion = champion
#         self.skill_Q = skill_Q
#         self.skill_W = skill_W
#         self.skill_E = skill_E
#         self.skill_R = skill_R
#         self.id = id
        
class Skill:
    def __init__(self, champion, skill_name, skill_shortcut, id = None):
        self.champion = champion
        self.skill_name = skill_name
        self.skill_shortcut = skill_shortcut
        self.id = id
