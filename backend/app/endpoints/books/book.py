from flask_restx import Resource, Namespace


ns: Namespace = Namespace("Book", description="Books Transaction", path="/books")

@ns.route("/")
class Book(Resource):
    def get(self, ):
        """Test Output"""
        return {"Status" : "Success"}