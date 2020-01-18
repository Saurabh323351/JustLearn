from django.test import TestCase

# Create your tests here.
import warnings

def test_me():
    x=4
    assert 4==x


import warnings


def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1


def test_one():
    assert api_v1() == 1


from flask import jsonify
import requests,pytest
import json
import pprint
base_url='http://127.0.0.1:8000/'
endpoint='emp_crud/'

def test_get_emp():

    url=base_url+endpoint

    main_response=requests.get(url)
    print(main_response)
    response=json.loads(main_response.text)

    pprint.pprint(response,indent=4)

    print(main_response.headers['Content-Type'])
    assert main_response.status_code == 200
    # assert main_response.headers['Content-Type'] == 'application/json'

# @pytest.mark.skip(reason="it is perfectly working,so i want to skip it")
def test_post():

    url = base_url + endpoint

    data={
      "eno": 13,
      "ename": "saurabh_test",
      "esal": 0,
      "eaddr": "ka",
      "user": "s"
}
    data_to_send=json.dumps(data)

    headers={
        'Content-Type':'application/json'
    }
    main_response = requests.post(url,data=data_to_send,headers=headers)
    print(main_response)
    response = json.loads(main_response.text)

    pprint.pprint(response, indent=4)

    assert main_response.status_code == 201
    # assert main_response.headers['Content-Type'] == 'application/json'



