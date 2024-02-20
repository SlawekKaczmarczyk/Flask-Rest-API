from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required = True)
video_put_args.add_argument("views", type=int, help="Views of the video", required = True)
video_put_args.add_argument("rating", type=int, help="Rating of the video out of 10", required = True)
 
videos={}

def abortV(video_id): # if video doesn't exist
    if video_id not in videos:
        abort(404, message="Video id not found!")

class Video(Resource):
    def get(self,video_id):
        abortV(video_id)
        return videos[video_id] # return a json format
    
    def put(self,video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args 
        return videos[video_id], 201 #201 stands for created
    

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
 

