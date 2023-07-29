# Python API Automation Framwork

## Integration test cases for the Restful Booker

URL -https://restful-booker.herokuapp.com/booking

1. Verify - GET, POST, PATCH, DELETE , PUT
2. response body, headers, status code.
2. Auth - basic Auth , Cokkie based Auth
3. JSON Schemas validation

## tech Stck (python packages used)

1. Request module
2. Ptest,Pytest-html
3. Allure Report
4. Faker, CSV, JSON, YAML
5. Run via coomand line - Jenkins

### P.s -- DB Connecion (In future)

## instll pip packages 
--  'pip install requests pytest pytest-html faker allure-pytest jsonschema'    

pip freeze > requirements.txt

pip install requirements.txt

## How to run Via Jenkins ?

## How to run coomand
''pytest .\pyAPIAutomation\test_scripts\ -s -v --html=html.report --alluredir=./report ''
