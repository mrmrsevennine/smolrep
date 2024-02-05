```python
from service import Service
from service_schema import ServiceSchema
from marshmallow import ValidationError

class VersicherungService(Service):
    def __init__(self, service_id, details):
        super().__init__(service_id, details)

    def book_service(self):
        if self.is_bookable():
            # Code to book the service
            return "service-booked"
        else:
            return "service-unavailable"

    def is_bookable(self):
        # Code to check if the service is bookable
        return True

    def validate_service_details(self, details):
        schema = ServiceSchema()
        try:
            schema.load(details)
            return True
        except ValidationError as err:
            return False
```