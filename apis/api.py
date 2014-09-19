from flask import Flask, request
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)

resources = {}

class ResourceSimple(Resource):
	def get(self, resource_id):
		return {resource_id: resources[resource_id]}
	
	def put(self, resource_id):
		resources[resource_id] = request.form['data']
		return {resource_id: resources[resource_id]}

api.add_resource(ResourceSimple, '/<string:resource_id>')

if __name__ == '__main__':
	app.run(debug=True)
