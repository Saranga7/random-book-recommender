import grpc
from books_pb2_grpc import RecommendationsStub
from books_pb2 import GenreRequest


channel=grpc.insecure_channel('localhost:50051')
client=RecommendationsStub(channel)

genre=input("Enter genre: ")

request=GenreRequest(
    user_id=1,category=genre
    )
response=client.Recommend(request)

print(response)





