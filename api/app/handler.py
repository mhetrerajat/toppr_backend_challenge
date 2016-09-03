from datetime import datetime
from flask import jsonify, request
from app import db, app, Serializer, Battle
from sqlalchemy import func


@app.route('/')
def hello():
	data = []
	return jsonify({'result' : data})


@app.route('/list', methods=['GET'])
def get_places_list():
	response = None
	query_type = request.args.get('type')
	if query_type == "region":
		places_maps = { item[0] : item[1] for item in db.session.query(Battle.region, func.count(Battle.id)).group_by(Battle.region).all()}
		response = jsonify(dict(type=query_type, result=places_maps))
	elif query_type == "location":
		places_maps = { item[0] : item[1] for item in db.session.query(Battle.location, func.count(Battle.id)).group_by(Battle.location).all()}
		response = jsonify(dict(type=query_type, result=places_maps))
	else:
		places_list = Battle.query.all()
		response = jsonify({ 'result' : Serializer.serialize_list(places_list)})
	return response


@app.route('/count', methods=['GET'])
def get_count():
	data_count = Battle.query.count()
	return jsonify({'result' : { 'count' : data_count }})


@app.route('/search', methods=['GET'])
def search():
	response = None
	name_query = request.args.get('name')
	king_query = request.args.get('king')
	type_query = request.args.get('type')
	location_query = request.args.get('location')

	if name_query:
		# search for name
		result_list = Battle.query.filter(Battle.name.contains(name_query)).all()
		response = jsonify({'result' : Serializer.serialize_list(result_list)})
	elif king_query:
		# search for king
		result_list = Battle.query.filter_by(Battle.king.contains(king_query)).all()
		response = jsonify({'result' : Serializer.serialize_list(result_list)})
	elif type_query:
		# search for type
		result_list = Battle.query.filter_by(Battle.type.contains(type_query)).all()
		response = jsonify({'result' : Serializer.serialize_list(result_list)})
	elif location_query:
		# search for location
		result_list = Battle.query.filter_by(Battle.location.contains(location_query)).all()
		response = jsonify({'result' : Serializer.serialize_list(result_list)})
	else:
		response = jsonify({'result' : "Please type your query."}) 
	return response


@app.route('/stats', methods=['GET'])
def show_stats():

	attacker_outcome_map = {item[1] : item[0] for item in db.session.query(func.count(Battle.id), Battle.attacker_outcome).group_by(Battle.attacker_outcome).all()}
	distinct_battle_type = [item[0] for item in db.session.query(Battle.battle_type).distinct().all()]

	defender_size_map = {}
	defender_size_min_max = db.session.query(func.max(Battle.defender_size).label('max'), func.min(Battle.defender_size).label('min')).filter(Battle.defender_size != 0).all()
	defender_size_map.update({ 'max' : defender_size_min_max[0][0], 'min' : defender_size_min_max[0][1]})
	defender_size_avg = db.session.query(func.avg(Battle.defender_size).label('average')).all()
	defender_size_map.update({ 'average' : defender_size_avg[0][0]})


	most_active_map = {}
	most_active_attacker_king ={item[1] : item[0] for item in db.session.query(func.count(Battle.id), Battle.attacker_king).group_by(Battle.attacker_king).all()}
	most_active_attacker_king = sorted(most_active_attacker_king.items(), key=lambda x: x[1], reverse=True)[0][0]
	most_active_map.update({ 'attacker_king' : most_active_attacker_king})

	most_active_defender_king ={item[1] : item[0] for item in db.session.query(func.count(Battle.id), Battle.defender_king).group_by(Battle.defender_king).all()}
	most_active_defender_king = sorted(most_active_defender_king.items(), key=lambda x: x[1], reverse=True)[0][0]
	most_active_map.update({ 'defender_king' : most_active_defender_king})

	most_active_region ={item[1] : item[0] for item in db.session.query(func.count(Battle.id), Battle.region).group_by(Battle.region).all()}
	most_active_region = sorted(most_active_region.items(), key=lambda x: x[1], reverse=True)[0][0]
	most_active_map.update({ 'region' : most_active_region})

	most_active_name = [item[1] for item in db.session.query(func.count(Battle.id), Battle.name).group_by(Battle.name).all()]	
	most_active_map.update({ 'name' : most_active_name})

	return jsonify(dict(attacker_outcome=attacker_outcome_map, battle_type=distinct_battle_type, defender_size=defender_size_map, most_active=most_active_map))


@app.errorhandler(404)
def not_found_error(error):
    """
        Page not found
        404
    """
    return jsonify(dict(result="Page not found.", status=404)), 404

@app.errorhandler(500)
def internal_error(error):
    """
        Internal Server Error
        500
    """
    return jsonify(dict(result="Oops! Something went wrong with server. Please try again", status=500)), 500
