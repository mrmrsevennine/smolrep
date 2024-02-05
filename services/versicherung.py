```python
from service import Service

class Versicherung(Service):
    def __init__(self, service_id, service_status):
        super().__init__(service_id, service_status)

    def add_service(self, service_data):
        if self.validate_service_data(service_data):
            self.service_data = service_data
            self.service_status = "Available"
            return self.service_messages["service_added"]
        else:
            return self.service_messages["invalid_data"]

    def book_service(self):
        if self.service_status == "Available":
            self.service_status = "Booked"
            return self.service_messages["service_booked"]
        else:
            return self.service_messages["service_unavailable"]

    def validate_service_data(self, service_data):
        return self.service_schema.validate(service_data)
```