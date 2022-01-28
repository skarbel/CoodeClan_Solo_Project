from db.run_sql import run_sql
from models.champion import Champion
from models.skill import Skill


def save(skill):
    sql = "INSERT INTO skills( champion_id, skill_name, skill_shortcut ) VALUES (%s, %s, %s) RETURNING *"
    values = [skill.champion.id, skill.skill_name, skill.skill_shortcut]
    results = run_sql( sql, values )
    skill.id = results[0]['id']
    return skill

