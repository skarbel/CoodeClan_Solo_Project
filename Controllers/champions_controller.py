from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.champion import Champion
from models.skill import Skill
import repositories.champion_repository as champion_repository
import repositories.skill_repository as skill_repository

champions_blueprint = Blueprint("champions", __name__)

@champions_blueprint.route('/champions', methods=['GET'])
def champions():
    champions = champion_repository.select_all()
    return render_template('/champions/index.html', champions = champions)

@champions_blueprint.route('/champions/<id>', methods=['GET'])
def show_champion(id):
    champion = champion_repository.select(id)
    skill = champion_repository.skills(id)
    return render_template('champions/show.html', champion = champion, skill = skill)

@champions_blueprint.route('/champions/<id>/delete', methods=['POST'])
def delete_champion(id):
    champion_repository.delete(id)
    return redirect('/champions')




@champions_blueprint.route('/champions/new', methods=['GET'])
def new_champion():
    skills = skill_repository.select_all()
    return render_template('champions/new.html', all_skills = skills)

@champions_blueprint.route('/champions',  methods=['POST'])
def create_champion():
    champion_name  = request.form['champion_name']
    champion_title = request.form['champion_title']
    champion_class  = request.form['champion_class']
    release_date  = request.form['release_date']
    # skill = skill_repository.select(request.form['skill_id'])
    champion = Champion(champion_name, champion_title, champion_class, release_date)
    champion_repository.save(champion)
    return redirect('/champions')




@champions_blueprint.route('/champions/<id>/edit', methods=['GET'])
def edit_champion(id):
    champion = champion_repository.select(id)
    skills = skill_repository.select_all()
    return render_template('champions/edit.html', champion = champion, all_skills = skills)

@champions_blueprint.route('/champions/<id>', methods=['POST'])
def update_champion(id):
    champion_name = request.form['champion_name']
    champion_title = request.form['champion_title']
    champion_class = request.form['champion_class']
    release_date  = request.form['release_date']
    skill = skill_repository.select(request.form['skill_id'])
    champion = Champion(champion_name, champion_title, champion_class, release_date, skill, id)
    champion_repository.update(champion)

    skill = Skill(champion,skill_name, skill_shortcut, id)
    skill_repository.update(skill)

    return redirect('/champions')