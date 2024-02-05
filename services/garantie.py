```python
from service import Service, ServiceSchema
from marshmallow import ValidationError

class Garantie(Service):
    def __init__(self, service_id, details):
        super().__init__(service_id, details)

    def book_service(self):
        if self.is_bookable():
            # Code to book the service goes here
            pass
        else:
            return "service-unavailable"

    def is_bookable(self):
        # Code to check if the service is bookable goes here
        return True

def create_garantie_service(service_id, details):
    schema = ServiceSchema()
    try:
        data = schema.load(details)
        return Garantie(service_id, data)
    except ValidationError as err:
        return err.messages
```