```python
from service import Service
from service_schema import ServiceSchema
from book_service import book_service

class Reparatur(Service):
    def __init__(self, service_id, details):
        super().__init__(service_id, details)
        self.service_schema = ServiceSchema({
            "service_id": {"type": "string"},
            "details": {"type": "dict"},
        })

    def book(self):
        if self.is_available():
            book_service(self.service_id)
            return {"message": "service-booked"}
        else:
            return {"message": "service-unavailable"}

    def is_available(self):
        # Implement logic to check if the service is available
        pass
```