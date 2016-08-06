
################## Test Data (Model) ################### 
####### Convert to Database access Later #######

class SparksModel(object):
    def __init__(self):
        self.counter = 0
        self.sparks = []

    def get_all(self):
        return self.sparks;

    def get(self, id):
        for spark in self.sparks:
            if spark['id'] == id:
                return spark
        api.abort(404, "Spark {} doesn't exist".format(id))

    def create(self, data):
        spark = data
        spark['id'] = self.counter = self.counter + 1
        self.sparks.append(spark)
        return spark

    def update(self, id, data):
        spark = self.get(id)
        spark.update(data)
        return spark

    def delete(self, id):
        spark = self.get(id)
        self.sparks.remove(spark)
