from db.run_sql import run_sql
from models.champion import Champion
from models.skill import Skill


def save(champion):
    sql = "INSERT INTO champions( champion_name, champion_title, champion_class, release_date) VALUES ( %s, %s , %s, %s ) RETURNING *"
    values = [champion.champion_name, champion.champion_title, champion.champion_class, champion.release_date]
    results = run_sql( sql, values )
    champion.id = results[0]['id']
    return champion

def select(id):
    champion = None
    sql = "SELECT * FROM champions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        champion = Champion(result['champion_name'], result['champion_title'], result['champion_class'], result['release_date'], result['id'])
        return champion

def select_all():
    champions = []
    sql = "SELECT * FROM champions"
    results = run_sql(sql)
    for row in results:
        champion = Champion(row['champion_name'], row['champion_title'], row['champion_class'], row['release_date'], row['id'])
        champions.append(champion)
    return champions

def delete(id):
    sql = "DELETE  FROM champions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE  FROM champions"
    run_sql(sql)

def update(champion):
    sql = "UPDATE champions SET (champion_name, champion_title, champion_class, release_date) = ( %s, %s , %s, %s ) WHERE id = %s"
    values = [champion.first_name, champion.last_name, champion.id]
    run_sql(sql, values)