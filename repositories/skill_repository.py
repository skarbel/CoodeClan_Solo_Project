from db.run_sql import run_sql
from models.champion import Champion
from models.skill import Skill

def save(skill):
    sql = "INSERT INTO skills( skill_Q, skill_W, skill_E, skill_R ) VALUES (%s, %s , %s, %s) RETURNING id"
    values = [skill.skill_Q, skill.skill_W, skill.skill_E, skill.skill_R]
    results = run_sql( sql, values )
    skill.id = results[0]['id']
    return skill