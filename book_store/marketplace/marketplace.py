# Flask app to display a webpage to the user.
# It'll call the Recommendations microservice to get book recommendations to display on the page.
import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

# Note: In this example, you create the gRPC channel and stub as globals. Usually globals are a no-no, 
# but in this case an exception is warranted.
# The gRPC channel keeps a persistent connection to the server to avoid the overhead of
# having to repeatedly connect. It can handle many simultaneous request and will reestablish
# dropped connections. However, if you create a new channel before each request, then Python will garbage
# collect it, and you won't get most of the benefits of a persistent connection.
# You want the channel to stay open so you don't need to reconnect to the recommendations
# microservice for every request.
recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(recommendations_request)
    return render_template("homepage.html", recommendations=recommendations_response.recommendations)