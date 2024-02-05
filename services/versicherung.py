```python
from service import Service
from service_schema import ServiceSchema
from service_messages import ServiceMessages
from service_status import ServiceStatus

class Versicherung(Service):
    def __init__(self, service_id, service_schema, service_messages, service_status):
        super().__init__(service_id, service_schema, service_messages, service_status)

    def add_service(self, service_data):
        if self.service_schema.validate(service_data):
            self.service_data = service_data
            self.service_status = ServiceStatus.ADDED
            print(self.service_messages.get_message('service_added'))
        else:
            print(self.service_messages.get_message('invalid_service_data'))

    def book_service(self):
        if self.service_status == ServiceStatus.ADDED:
            self.service_status = ServiceStatus.BOOKED
            print(self.service_messages.get_message('service_booked'))
        else:
            print(self.service_messages.get_message('service_not_bookable'))
```