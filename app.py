from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json
import base64
import s3fs

fs = s3fs.S3FileSystem(anon=False)

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')

# @app.route('/post',methods=['POST'])
class test(Resource):
    def get(self):
        import os
        return os.listdir()

    def post(self):
        jsonData = parser.parse_args()
        # jsonData = json.loads(data)
        # print(jsonData)
        with fs.open('zappa-3czvv42gy/data.json','w') as f:
            json.dump(jsonData,f)
        return jsonData, 201
        # return jsonify(isError= False,
        #                 message= "Success",
        #                 statusCode= 200, data=jsonData), 200

# class download(Resource):
#     def post():
        # data = request.data
        # jsonData = json.loads(data)
        # pic = jsonData['picture']
        # imgdata = base64.b64decode(pic)
        # with open('img.png','wb') as f:
        #     f.write(imgdata)
        # return jsonify(isError= False,
        #                 message= "Success",
        #                 statusCode= 200), 200


api.add_resource(test, '/test')

if __name__ == '__main__':
    app.run()