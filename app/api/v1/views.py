from flask_restful import Resource
from flask import jsonify, make_response, request
from datetime import datetime

#from .models import  RedFlagFrame
 




REDFLAG =  [
{
	'id':101,
	'createdOn':datetime.now(),
	'createdBy':'user1',
	'location': '101101',
	'status':'draft',
	'images':'img1',
	'video':'vid1',
	'comment':'nihilism'
},
{
	'id':102,
	'createdOn':datetime.now(),
	'createdBy':'user2',
	'location': '202202',
	'status':'draft',
	'images':'img1',
	'video':'vid1',
	'comment':'solipsism'
}
]


all_redflags=REDFLAG

class RedFlags(Resource):
	def __init__(self):
		self.db = all_redflags

	def post(self):
		data = request.get_json()
		Id = data['id']
		createdOn=datetime.now()
		Type=data['type']
		location=data['location']
		status=data['status']
		images=data['images']
		video=data['video']
		comment=data['comment']


		newREDFLAG = {
		      'id':Id,
		      'createdOn':createdOn,
		      'type':Type,
		      'location':location,
		      'status':status,
		      'images':images,
		      'video':video,
		      'comment':comment
		      }
		
		self.db.append(newREDFLAG)
		return make_response(jsonify({
            'status':201,
            'data':[{
            'id':Id,
            'message':'Created red-flag record'
            }]
		    }), 201)

	#get all redflags
	def get(self):
		return make_response(jsonify({
			'status':200,
			'Reported redflags are ':self.db,
			'Message': 'Success!'
			}),200)
    
    #update redflac comment
	def patch (self,Id,newComment='newComment'):
		for redflag in all_redflags:
			if redflag['id'] == Id:
				redflag['comment'] = newComment

				return make_response(jsonify({
        									'status':204,
        									'data' : [{
        										'id':Id,
        										'message':'Updated red-flag record’s comment'
        									}]
        								}))
		return {'Message': 'Unable to update redflag comment'}

#class for reaching a single record. Methods are GET, DELETE AND PATCH
class RedFlagSpec(Resource):
	"""docstring for ClassName"""
	def __init__(self):
		self.db= all_redflags

		
	#get  a specific redflag
	def get(self,Id):
		for redflag  in self.db:
			if redflag['id'] == Id:
				return make_response(jsonify({
					'status':200,
					'data': [{
					'id':Id,
				     'message':'redflag successfully  fetched'
					}]
					}))

		#redflag matching the id is not found		
		return {'status':404, 'message':'redflag not found'}


    #delete  a redflag
	def delete(self,Id):
		for redflag in all_redflags:
			if redflag['id'] == Id:
				all_redflags.remove(redflag)

				return make_response(jsonify({
    								'status':204 ,
    								'data':[{
    								'id':Id, 
    		 						'message': 'redflag record has been deleted'
    		 						}]
    							}),204)
		#record for deletion is not found
		return {'status':404,'message':'redflag does not exist!'}

    #update redflag location
	def patch (self,Id,newLocation='newLocation'):
		for redflag in all_redflags:
			if redflag['id'] == Id:
				redflag['location'] = newLocation
				return make_response(jsonify({
        								'status':204,
        								'data' : [{
        								'id':Id,
        								'message':'Updated red-flag record’s location'
        								}]
        							}))
		return {'Message': 'Unable to update redflag location'}

	




