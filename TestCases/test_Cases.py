import pytest
import requests


#API URL
Base_url = "http://127.0.0.1:5000"

@pytest.mark.run(order=1)
def test_get_list_off_all_task():

    #Send GET request
    response = requests.get(Base_url+"/tasks")

    #Fetch status code of request
    status_code = response.status_code

    ##validating response code
    assert int(status_code)==200


#URL
@pytest.mark.run(order=2)
def test_verify_URL_of_get_request():

    # Send GET request
    response = requests.get(Base_url + "/tasks")

    #Request URL
    URL_of_request = response.url

    #Excepted URL stored in expected_url variable
    expected_url = "http://127.0.0.1:5000/tasks"

    #Verify request URL is equals to excepted URL
    assert  URL_of_request== expected_url


#create task
@pytest.mark.run(order=3)
def test_verify_new_task_create_successfully():

    #Data to be post on server
    payload = {"task": "add task", "completed": "False"}

    #Make post request with JSON input body
    response = requests.post(Base_url + "/tasks", json=payload)

    status_code = response.status_code

    #validating response code
    assert int(status_code) == 200

#update task
@pytest.mark.run(order=4)
def test_verify_task_updated_successfully():

    # Send GET request
    response = requests.get(Base_url + "/tasks")

    #Fetch status code of the request
    print(response.status_code)

    resp = response.json()

    # parse id from JSON response
    a = resp[0]["id"]


    #Data tobe update on server
    payload = {"task": "add task 212", "completed": "False"}

    #Make PUT request with JSON input body
    response = requests.put(Base_url + "/tasks/" + str(a), json=payload)

    assert response.status_code == 200

#delete task
@pytest.mark.run(order=5)
def test_verify_task_deleted_successfully():

    # Send GET request
    response = requests.get(Base_url + "/tasks")

    # Fetch status code of the request
    print(response.status_code)

    resp = response.json()

    # parse id from JSON response
    a = resp[0]["id"]

    response = requests.delete(Base_url+"/tasks/"+ str(a))

    assert response.status_code == 200

#Fetch server name
@pytest.mark.run(order=6)
def test_verify_API_server():

    # Send GET request
    response = requests.get(Base_url + "/tasks")

    #Fetch server name
    server = response.headers.get('Server')

    #Excepted server name
    expected_server = "Werkzeug/0.15.5 Python/2.7.16"

    #Validation server name
    assert server==expected_server





