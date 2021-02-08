from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members",  methods=['POST'])
def create_member():
    member_name = (request.form['name'])
    member_age = (request.form['age'])
    member_type = (request.form['type'])
    new_member = Member(member_name, member_age, member_type)
    members.append(new_member)
    return redirect('/members')

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    sessions = member_repository.sessions(member)
    return render_template("members/show.html", member=member, sessions=sessions)
