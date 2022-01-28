from db.run_sql import run_sql
from models.champion import Champion
from models.skill import Skill

def save(champion):
    sql = "INSERT INTO champions( champion_name, champion_title, champion_class, release_date) VALUES ( %s, %s , %s, %s) RETURNING *"
    values = [champion.champion_name, champion.champion_title, champion.champion_class, champion.release_date]
    results = run_sql( sql, values )
    champion.id = results[0]['id']
    return champion