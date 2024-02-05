1. Service Class: A base class that each service (Reparatur, Inspektion, Versicherung, Garantie) will inherit from. This class will contain common properties and methods that all services share.

2. Service Schema: A data schema that defines the structure of a service. This will be used in each service file to validate and structure the data.

3. Service ID: A unique identifier for each service. This will be used in the DOM elements and JavaScript functions to reference each service.

4. Add Service Function: A function that will be used to add a new service. This function will be shared across all service files.

5. Service Messages: A set of predefined messages that will be used to communicate the status of the services. These messages will be shared across all service files.

6. Book Service Function: A function that will be used to book a service. This function will be shared across all service files.

7. Service Status: A variable that will be used to track the status of each service. This will be shared across all service files.

8. Main Function: A function in the main.py file that will call the functions in the service files. This function will be shared across all service files.