
#from flask.ext.restful import fields

####### Convert to Database access Later #######

#spark = api.model('Spark', {
#    'id': fields.Integer(readOnly=True, description='The unique identifier'),
    #'fires': fields.List(fields.Integer()),
#    'title': fields.String(required=True, description='The Title of the spark'),
#    'body': fields.String(required=True, description='The Body of the spark'),
    #'messages': fields.List(fields.Integer(required=False, description='message id')),
    #'owner': fields.Integer(required=True, description='Owner id'),
    #'rouse_user_list':  fields.List(fields.Integer(required=False, description='Users who liked this spark')),
    #'douse_user_list':  fields.List(fields.Integer(required=False, description='Usuers who did not like this spark')),
    #'reignite_user_list':  fields.List(fields.Integer(required=False, description='Users who reposted this on other fires'))
#})

class SparksModel(object):
    def __init__(self):
        self.counter = 0
        self.sparks = []

    def get_all(self):
        return self.sparks;

    def get(self, id):
        print("In get Spark" + str(id))
        for spark in self.sparks:
            if spark['id'] == id:
                return spark
        api.abort(404, "Spark {} doesn't exist".format(id))

    def create(self, data):
        print ("In SparksModel.create")
        print(data)
        spark = {}
        spark = data
        spark['id'] = self.counter = self.counter + 1
        spark['messages'] = []
        spark['rouse_user_list'] = [] 
        spark['douse_user_list'] = []
        spark['reignite_user_list'] = []
        self.sparks.append(spark)
        return spark

    def update(self, id, data):
        spark = self.get(id)
        spark.update(data)
        return spark

    def delete(self, id):
        spark = self.get(id)
        self.sparks.remove(spark)
