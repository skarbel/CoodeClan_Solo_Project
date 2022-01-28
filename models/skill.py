class Skill:
    
    def __init__(self, champion, skill_name, skill_shortcut, id = None):
        self.champion = champion
        self.skill_name = skill_name
        self.skill_shortcut = skill_shortcut
        self.id = id