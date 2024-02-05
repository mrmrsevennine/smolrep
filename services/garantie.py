```python
from service import Service

class Garantie(Service):
    def __init__(self, service_id, status):
        super().__init__(service_id, status)

    def book_service(self):
        if self.status == "available":
            self.status = "booked"
            return self.service_messages["book_success"]
        else:
            return self.service_messages["book_fail"]

    def add_service(self, service_data):
        if self.validate_service_data(service_data):
            self.service_data = service_data
            return self.service_messages["add_success"]
        else:
            return self.service_messages["add_fail"]
```