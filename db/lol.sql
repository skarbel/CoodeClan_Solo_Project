DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS champions;

CREATE TABLE champions (
    id SERIAL PRIMARY KEY,
    champion_name VARCHAR(255),
    champion_title VARCHAR(255),
    champion_class VARCHAR(255),
    release_date VARCHAR(255)
);

CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    skill_name VARCHAR(255),
    skill_shortcut VARCHAR(255),
    champion_id INT REFERENCES champions(id) ON DELETE CASCADE
);