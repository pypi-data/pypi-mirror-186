# How to define and use custom data types
In the hello world example from the quick-start guide we only used the string data type.
Here we will show you how to define more complex composite data types and use them either as function parameters or return values.

Therefore we extend the previous HelloWorld example.

## Exposing classes
In order to support most use case scenarios you can not just expose individual functions via DASF, but entire classes. 
So before we dive into custom data types, let's convert our tiny `hello_world` function into a hello world class.

```{code-block} python
---
lineno-start: 1
caption: HelloWorld class
---
from typing import List


class HelloWorld:
    def __init__(self, message: str):
        self.message = message

    def repeat_message(self, repeat: int) -> List[str]:
        return [self.message] * repeat
```

The given HelloWorld class defines a constructor that expects a string parameter called `message` and a single function called `repeat_message` that takes an integer and returns a list of strings. Now the idea is, that objects of this HelloWorld class are instantiated with a message string, that then will be used in its `repeat_message` along with the `repeat` parameter to generate the list of strings (repeating the message parameter `repeat` times) that are returned.

Now, to expose this class through a DASF backend module all we have to do is import and call the `main` function from the `demessaging` package and register the class via `__all__`. So our example above becomes:

```{code-block} python
---
lineno-start: 1
caption: HelloWorld class exposed via a HelloWorld backend module.
---
from typing import List
from demessaging import main

__all__ = ["HelloWorld"]


class HelloWorld:
    def __init__(self, message: str):
        self.message = message

    def repeat_message(self, repeat: int) -> List[str]:
        return [self.message] * repeat


if __name__ == "__main__":
    main(
        messaging_config=dict(topic="hello-world-class-topic")
    )
```

### Configuring exposed classes and functions through annotations

Sometimes you might not want to expose all functions of a class, like private/internal ones. This can be configured via the `@configure` annotation. Furthermore you might want to assert a certain value range for the method arguments or returns. This can also be configured via the `@configure` annotation.

```{code-block} python
---
lineno-start: 1
caption: Exposed HelloWorld class configured through @configure annotation.
---
from typing import List
from demessaging import main, configure

__all__ = ["HelloWorld"]


@configure(methods=["repeat_message"])
class HelloWorld:
    def __init__(self, message: str):
        self.message = message

    @configure(field_params={"repeat": {"ge": 0}})
    def repeat_message(self, repeat: int) -> List[str]:
        return [self.message] * repeat

    def unexposed_method(self) -> str:
        return self.message


if __name__ == "__main__":
    main(
        messaging_config=dict(topic="hello-world-class-topic")
    )
```

```{admonition} Class and function configuration parameters
:class: note

For a comprehensive list of configuration parameters see: [`demessaging.config.ClassConfig`](https://git.geomar.de/digital-earth/dasf/dasf-messaging-python/-/blob/master/demessaging/config.py)

Also refer to https://pydantic-docs.helpmanual.io/usage/schema/#field-customisation
```

## Define custom data types

Let's extent our HelloWorld class even further by defining a custom data type/class that we are going to return in one of our exposed functions. In order to define the data type class we have to register it by using the `@registry.register_type` annotation. Let's register a `GreetResponse` as in the following example:

```{code-block} python
---
lineno-start: 1
emphasize-lines: 8-12
caption: Custom data type class defined through @registry.register_type annotation.
---
from typing import List
import datetime
from pydantic import BaseModel
from demessaging import main, configure, registry

__all__ = ["HelloWorld"]

@registry.register_type
class GreetResponse(BaseModel):
    message: str
    greetings: List[str]
    greeting_time: datetime.datetime

@configure(methods=["repeat_message"])
class HelloWorld:
    def __init__(self, message: str):
        self.message = message

    @configure(field_params={"repeat": {"ge": 0}})
    def repeat_message(self, repeat: int) -> List[str]:
        return [self.message] * repeat

    def unexposed_method(self) -> str:
        return self.message


if __name__ == "__main__":
    main(
        messaging_config=dict(topic="hello-world-topic")
    )
```

Note that the registered class has to inherit from the pydantic `BaseModel` class. Once registered we can use it as a function argument type or a return value type, like in the following `greet` function example.

```{code-block} python
---
lineno-start: 1
emphasize-lines: 25-32
caption: Custom data type class defined through @registry.register_type annotation.
---
from typing import List
import datetime
from pydantic import BaseModel
from demessaging import main, configure, registry

__all__ = ["HelloWorld"]


@registry.register_type
class GreetResponse(BaseModel):
    message: str
    greetings: List[str]
    greeting_time: datetime.datetime


@configure(methods=["repeat_message", "greet"])
class HelloWorld:
    def __init__(self, message: str):
        self.message = message

    @configure(field_params={"repeat": {"ge": 0}})
    def repeat_message(self, repeat: int) -> List[str]:
        return [self.message] * repeat

    @configure(field_params={"repeat": {"ge": 0}})
    def greet(self, repeat: int, greet_message: str) -> GreetResponse:
        greetings: List[str] = [greet_message] * repeat
        return GreetResponse(
            message=self.message,
            greetings=greetings,
            greeting_time=datetime.datetime.now(),
        )

    def unexposed_method(self) -> str:
        return self.message


if __name__ == "__main__":
    main(
        messaging_config=dict(topic="hello-world-topic")
    )

```
