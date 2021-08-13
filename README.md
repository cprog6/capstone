Backend
    From the backend folder run 'pip install requirements.txt'. All of the requirements will be in the requirements.txt file

    To run the application run the following commands on the command line
        'export FLASK_APP=app'
        'export FLASK_DEBUG=true'
        'source setup.sh'
        'flask run'

    The application is run on 'http://127.0.0.1:5000/' by default and is a proxy in the frontend configuration.

    Tests
        In order to run tests navigate to the backend folder and run the following commands:
            'dropdb capstone_test'
            'createdb capstone_test'
            'python test_app.py'

        The first time you run the test, omit the dropdb command.

        All tests are kept in that file and should be maintained as updates are made to app functionality.

API Reference

    Getting Started
        Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, 'http://127.0.0.1:5000/', which is set as a proxy in the frontend configuration.

    Error Handling
        Errors are returned as JSON objects in the following format:
            {
                "success": False,
                "error": 400,
                "message": "bad request"
            }

        The API will return three error types when requests fail:
            400: Bad Request
            404: Resource Not Found
            422: Not Processable

Endpoints
GET /drivers
General:
Returns a list of driver objects, success value, and all of the names given in the table.

            Sample: 'curl http://127.0.0.1:5000/drivers'
                "driver_list": [
                    {
                    "age": "22",
                    "gender": "male",
                    "id": 1,
                    "name": "gggg",
                    "truck_id": 1
                    },
                    {
                    "age": "6",
                    "gender": "male",
                    "id": 3,
                    "name": "Kaden",
                    "truck_id": 1
                    },
                    {
                    "age": "18",
                    "gender": "Male",
                    "id": 6,
                    "name": "Jack",
                    "truck_id": 1
                    },
                    {
                    "age": "18",
                    "gender": "Male",
                    "id": 7,
                    "name": "Jack",
                    "truck_id": 1
                    },
                    {
                    "age": "18",
                    "gender": "Male",
                    "id": 8,
                    "name": "Jack",
                    "truck_id": 1
                    },
                    {
                    "age": "18",
                    "gender": "Male",
                    "id": 9,
                    "name": "Jack",
                    "truck_id": 1
                    }
                ],
                "name_list": [
                    "gggg",
                    "Kaden",
                    "Jack",
                    "Jack",
                    "Jack",
                    "Jack"
                ],
                "success": true
                }

    POST /trucks/
        General:
            Creates a new truck using the submitted model, year, color, haul capacity, and driver ID. Returns the id of the created, and all of the values inserted in.

        curl http://127.0.0.1:5000/trucks/ -X POST -H "Content-Type: application/json" -d '{"model":"Ram 2500", "year":2020, "color":"Blue", "haul_capacity":15000, "driver_id":1}'

            {
                "trucks": [
                    {
                        "success": true,
                        "color": "Blue",
                        "driver_id": 1,
                        "haul_capacity": 15000,
                        "model": "Ram 2500",
                        "year": 2020
                    }
                ],
            }

    DELETE /trucks/<int:truck_id>/
        General:
            Deletes the truck of the given ID if it exists. All it returns is the value of success.

        curl -X DELETE http://127.0.0.1:5000/trucks/<int:truck_id>/
            {
                "success": true
            }

Authorization
    The Auth0 JWT includes claims for permissions based on the user's role within the Auth0 system. This project makes use of these claims using the decorator @requires_auth() method which checks if particular permissions exist within the JWT permissions claim of the currently logged in user.

    RBAC - Role Based Access Control
        
        RBAC is controlled by third party authorization control service, Auth0.com.

        Roles for this application with the following permissions:

            Driver:
                get:trucks
                get:drivers

            Admin:
                get:trucks
                get:drivers
                post:trucks
                post:drivers
                delete:trucks
                delete:drivers
                patch:trucks
                patch:drivers


Deployment locally
    From 'app' directory, run the following commands

        export FLASK_APP=app
        export FLASK_DEBUG=true
        pip install -r requirements.txt
        flask run

Testing
    Import the postman collection to test the endpoints in productions on the heroku platform
    https://shrouded-garden-71376.herokuapp.com

Authors
Trey Snyder

Motivation
    1. A company wants me to help them build a web and mobile application to track their trucks and drivers.
    2. Able to build a cross channel application
    3. Continuous learning of programming and development
