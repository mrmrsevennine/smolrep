```python
from services.reparatur import Reparatur
from services.inspektion import Inspektion
from services.versicherung import Versicherung
from services.garantie import Garantie

def main():
    reparatur_service = Reparatur()
    inspektion_service = Inspektion()
    versicherung_service = Versicherung()
    garantie_service = Garantie()

    services = [reparatur_service, inspektion_service, versicherung_service, garantie_service]

    for service in services:
        service.add_service()
        service.book_service()

if __name__ == "__main__":
    main()
```