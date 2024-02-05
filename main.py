```python
from services.reparatur import Reparatur
from services.inspektion import Inspektion
from services.versicherung import Versicherung
from services.garantie import Garantie

class MainApp:
    def __init__(self):
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def book_service(self, service_id):
        for service in self.services:
            if service.id == service_id:
                service.book()

if __name__ == "__main__":
    app = MainApp()

    reparatur = Reparatur()
    inspektion = Inspektion()
    versicherung = Versicherung()
    garantie = Garantie()

    app.add_service(reparatur)
    app.add_service(inspektion)
    app.add_service(versicherung)
    app.add_service(garantie)

    # Book a service by its ID
    app.book_service(reparatur.id)
```