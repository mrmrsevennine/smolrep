```python
from service import Service
from service_schema import ServiceSchema
from service_messages import ServiceMessages

class Garantie(Service):
    def __init__(self, service_id, service_status):
        super().__init__(service_id, service_status)
        self.service_schema = ServiceSchema({
            "service_id": service_id,
            "service_status": service_status
        })

    def add_service(self):
        super().add_service()
        print(ServiceMessages.ADD_SERVICE_MESSAGE.format(self.service_id))

    def book_service(self):
        super().book_service()
        print(ServiceMessages.BOOK_SERVICE_MESSAGE.format(self.service_id))

    def update_service_status(self, new_status):
        super().update_service_status(new_status)
        print(ServiceMessages.UPDATE_SERVICE_STATUS_MESSAGE.format(self.service_id, self.service_status))
```