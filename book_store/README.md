[Real Python tutorial about gRPC](https://realpython.com/python-microservices-grpc/)

### Commands
- To generate Python code from the protobufs, run the following:
````
    python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
````
Run this inside recommendations and marketplace directories.

This will generate 2 files:
- **recommendations_pb2**: Type definitions
- **recommendations_pb2_grpc**: The framework for a client and a server

- Build and run docker image from command line: 
````
docker build . -f recommendations/Dockerfile -t recommendations
docker build . -f marketplace/Dockerfile -t marketplace
docker network create microservices
docker run -p 127.0.0.1:50051:50051/tcp --network microservices \
        --name recommendations recommendations
docker run -p 127.0.0.1:5000:5000/tcp --network microservices \
        -e RECOMMENDATIONS_HOST=recommendations marketplace

docker run -p 127.0.0.1:5000:5000/tcp marketplace
````
- Or just use docker-compose:
````
docker-compose up
````
- Run tests for the project:
````
$ docker-compose build
$ docker-compose up
$ docker-compose exec marketplace pytest marketplace_integration_test.py
````

### Client sample Code

````
    import grpc
    from recommendations_pb2_grpc import RecommendationsStub
    from recommendations_pb2 import BookCategory, RecommendationRequest
    channel = grpc.insecure_channel("localhost:50051")
    client = RecommendationsStub(channel)
    request = recomendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
    client.Recommend(request)
````
