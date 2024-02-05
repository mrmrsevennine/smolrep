```python
from service import Service

class Inspektion(Service):
    def __init__(self, service_id, service_status):
        super().__init__(service_id, service_status)

    def add_service(self):
        super().add_service()
        self.service_status = "Available"

    def book_service(self):
        if self.service_status == "Available":
            self.service_status = "Booked"
            return self.service_messages['book_success']
        else:
            return self.service_messages['book_error']

    def get_service_status(self):
        return self.service_status
```