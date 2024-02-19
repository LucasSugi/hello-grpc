import grpc

import calculator_pb2 as calculator_messages
import calculator_pb2_grpc as calculator_service

def calculator_request(x: int, y: int, operation: str) -> int:
    with grpc.insecure_channel('localhost:50051') as channel:
        calculator_stub = calculator_service.CalculatorStub(channel)
        if operation == "Sum":
            response = calculator_stub.Sum(calculator_messages.CalculatorRequest(x=x, y=y))
        elif operation == "Sub":
            response = calculator_stub.Sub(calculator_messages.CalculatorRequest(x=x, y=y))
        elif operation == "Mult":
            response = calculator_stub.Mult(calculator_messages.CalculatorRequest(x=x, y=y))
        elif operation == "Div":
            response = calculator_stub.Div(calculator_messages.CalculatorRequest(x=x, y=y))
        else:
            raise KeyError("operation `{}` its invalid".format(operation))
    return response.result

def run():

    operation = 0
    operation_fromto = {
        1: "Sum",
        2: "Sub",
        3: "Mult",
        4: "Div",
    }

    while(True):
        print("Type your operation:\n0 - Exit\n1 - Sum\n2 - Sub\n3 - Mult\n4 - Div")
        operation = int(input())

        if operation == 0:
            break

        print("Type number: x = ", end="")
        x = int(input())

        print("Type number: y = ", end="")
        y = int(input())

        response = calculator_request(x, y, operation_fromto.get(operation, "invalid"))
        print("Response: `{}`".format(response))

if __name__ == "__main__":
    run()
