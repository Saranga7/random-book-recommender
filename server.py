from concurrent import futures
import time
import random
import grpc
from arango_db_create import db

import books_pb2 
import books_pb2_grpc

_ONE_DAY_IN_SECONDS=86400


class GenreBooksList(books_pb2_grpc.RecommendationsServicer):

    def Recommend(self,request,context):
        # if request.category not in books_by_category:
        #     context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        cursor = db.aql.execute(f'FOR doc IN books FILTER doc.category == "{request.category}" RETURN doc ')

        book_list=[doc for doc in cursor]
        random_book=random.choice(book_list)

        response=books_pb2.BookRecommendation()
        response.title=random_book['title']
        response.author=random_book['author']
        response.category=random_book['category']

        return response



def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    books_pb2_grpc.add_RecommendationsServicer_to_server(GenreBooksList(),server)
    server.add_insecure_port("[::]:50051")
    print("Server started at port 50051")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__=='__main__':
    serve()