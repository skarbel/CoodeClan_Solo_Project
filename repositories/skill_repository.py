from db.run_sql import run_sql
from models.champion import Champion
from models.skill import Skill
import repositories.champion_repository as champion_repository # WHY?

def save(skill):
    sql = "INSERT INTO skills ( champion_id, skill_name, skill_shortcut ) VALUES (%s, %s, %s) RETURNING *"
    values = [skill.champion.id, skill.skill_name, skill.skill_shortcut]
    results = run_sql( sql, values )
    skill.id = results[0]['id']
    return skill

def select(id):
    skill = None
    sql = "SELECT * FROM skills WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        champion = champion_repository.select(result['champion_id'])
        skill = Skill(champion, result['skill_name'], result['skill_shortcut'], result['id'] )
    return skill
    
def select_all():
    skills = []
    sql = "SELECT * FROM skills"
    results = run_sql(sql)
    for row in results:
        champion = champion_repository.select(row['champion_id'])
        skill = Skill(champion, row['skill_name'], row['skill_shortcut'], row['id'])
        skills.append(skill)
    return skills

def delete(id):
    sql = "DELETE  FROM skills WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE  FROM skills"
    run_sql(sql)

def update(skill):
    sql = "UPDATE skills SET (champion_id, skill_name, skill_shortcut) = (%s, %s, %s) WHERE id = %s"
    values = [skill.skill_name, skill.last_name, skill.id]
    run_sql(sql, values)