from ExampleMessageProducerGen import GreetResponse, hello_world

response: GreetResponse = hello_world(
    message="Hello", greet_message="greetings", repeat=5
)
print(response)
