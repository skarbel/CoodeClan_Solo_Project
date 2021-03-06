from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.champion import Champion
import repositories.champion_repository as champion_repository
import repositories.skill_repository as skill_repository
import pdb

champions_blueprint = Blueprint("champions", __name__)

@champions_blueprint.route('/champions', methods=['GET'])
def champions():
    champions = champion_repository.select_all()
    return render_template('/champions/index.html', title = "Champion list", champions = champions)

@champions_blueprint.route('/champions/<id>', methods=['GET'])
def show_champion(id):
    champion = champion_repository.select(id)
    skills = champion_repository.skills(champion)
    return render_template('champions/show.html', title = champion.champion_name, champion = champion, skills = skills)

@champions_blueprint.route('/champions/<id>/delete', methods=['GET'])
def delete_champion(id):
    champion_repository.delete(id)
    return redirect('/champions')




@champions_blueprint.route('/champions/new', methods=['GET'])
def new_champion():
    return render_template('champions/new.html', title = "New")

@champions_blueprint.route('/champions',  methods=['POST'])
def create_champion():
    champion_name  = request.form['champion_name']
    champion_title = request.form['champion_title']
    champion_class  = request.form['champion_class']
    release_date  = request.form['release_date']
    champion = Champion(champion_name, champion_title, champion_class, release_date)
    champion_repository.save(champion)
    return redirect('/champions')




@champions_blueprint.route('/champions/<id>/edit', methods=['GET'])
def edit_champion(id):
    champion = champion_repository.select(id)
    return render_template('champions/edit.html', title = "Edit", champion = champion)

@champions_blueprint.route('/champions/<id>', methods=['POST'])
def update_champion(id):
    champion_name = request.form['champion_name']
    champion_title = request.form['champion_title']
    champion_class = request.form['champion_class']
    release_date  = request.form['release_date']
    champion = Champion(champion_name, champion_title, champion_class, release_date, id)
    champion_repository.update(champion)
    return redirect('/champions')


@champions_blueprint.route('/about')
def home():
    return render_template('/about.html', title = "About")