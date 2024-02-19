from concurrent import futures

import grpc
import calculator_pb2 as calculator_messages
import calculator_pb2_grpc as calculator_service

class CalculatorServicer(calculator_service.CalculatorServicer):
    def Sum(self, request, context):
        print("received `sum` operation")
        response = calculator_messages.CalculatorResponse()
        response.result = request.x + request.y
        return response

    def Sub(self, request, context):
        print("received `sub` operation")
        response = calculator_messages.CalculatorResponse()
        response.result = request.x - request.y
        return response

    def Mult(self, request, context):
        print("received `mult` operation")
        response = calculator_messages.CalculatorResponse()
        response.result = request.x * request.y
        return response

    def Div(self, request, context):
        print("received `div` operation")
        response = calculator_messages.CalculatorResponse()
        response.result = int(request.x / request.y)
        return response

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    calculator_service.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()

if __name__== "__main__":
    server()
