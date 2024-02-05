from services.reparatur import Reparatur
from services.inspektion import Inspektion
from services.versicherung import Versicherung
from services.garantie import Garantie

class Main:
    def __init__(self):
        self.service_list = []

    def add_service(self, service):
        self.service_list.append(service)

    def book_service(self, service_id):
        for service in self.service_list:
            if service.id == service_id:
                if service.is_bookable():
                    service.book()
                    print("Service booked")
                else:
                    print("Service unavailable")
                break

if __name__ == "__main__":
    main = Main()
    main.add_service(Reparatur())
    main.add_service(Inspektion())
    main.add_service(Versicherung())
    main.add_service(Garantie())

    # Book a service by its ID
    main.book_service(1)