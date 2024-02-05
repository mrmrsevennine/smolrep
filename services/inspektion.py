```python
from service import Service, ServiceSchema
from marshmallow import ValidationError

class InspektionService(Service):
    def __init__(self, service_id, details):
        super().__init__(service_id, details)

    def book_service(self):
        if self.is_bookable():
            # Code to book the service
            pass
        else:
            raise Exception("Service is not available for booking")

    def is_bookable(self):
        # Code to check if the service is bookable
        return True

def validate_service_data(service_data):
    schema = ServiceSchema()
    try:
        schema.load(service_data)
    except ValidationError as e:
        return False, e.messages
    return True, "Service data is valid"

def create_inspektion_service(service_id, service_data):
    is_valid, message = validate_service_data(service_data)
    if is_valid:
        return InspektionService(service_id, service_data)
    else:
        raise Exception(message)
```