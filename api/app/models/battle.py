"""
    hello
"""
from app import db
from ..serializer import Serializer

class Battle(db.Model, Serializer):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	year = db.Column(db.Integer, default=0)
	battle_number = db.Column(db.Integer, default=0)
	attacker_king = db.Column(db.String)
	defender_king = db.Column(db.String)
	attacker_1 = db.Column(db.String)
	attacker_2 = db.Column(db.String)
	attacker_3 = db.Column(db.String)
	attacker_4 = db.Column(db.String)
	defender_1 = db.Column(db.String)
	defender_2 = db.Column(db.String)
	defender_3 = db.Column(db.String)
	defender_4 = db.Column(db.String)
	attacker_outcome = db.Column(db.String)
	battle_type = db.Column(db.String)
	major_death = db.Column(db.Integer, default=0)
	major_capture = db.Column(db.Integer)
	attacker_size = db.Column(db.Integer, default=0)
	defender_size = db.Column(db.Integer, default=0)
	attacker_commander = db.Column(db.String)
	defender_commander = db.Column(db.String)
	summer = db.Column(db.Integer, default=0)
	location = db.Column(db.String)
	region = db.Column(db.String)
	note = db.Column(db.String)

	def __init__(self, name, year, battle_number, attacker_king, defender_king, attacker_1, attacker_2, attacker_3, attacker_4, defender_1, defender_2, defender_3, defender_4, attacker_outcome, battle_type, major_death, major_capture, attacker_size, defender_size, attacker_commander, defender_commander, summer, location, region, note):
		self.name = name
		self.year = year
		self.battle_number = battle_number
		self.battle_type = battle_type
		self.attacker_king = attacker_king
		self.defender_king = defender_king
		self.attacker_1 = attacker_1
		self.attacker_2 = attacker_2
		self.attacker_3 = attacker_3
		self.attacker_4 = attacker_4
		self.defender_1 = defender_1
		self.defender_2 = defender_2
		self.defender_3 = defender_3
		self.defender_4 = defender_4
		self.attacker_outcome = attacker_outcome
		self.battle_type = battle_type
		self.major_death = major_death
		self.major_capture = major_capture
		self.attacker_size = attacker_size
		self.defender_size = defender_size
		self.attacker_commander = attacker_commander
		self.defender_commander = defender_commander
		self.summer = summer
		self.location = location
		self.region = region
		self.note = note
		
