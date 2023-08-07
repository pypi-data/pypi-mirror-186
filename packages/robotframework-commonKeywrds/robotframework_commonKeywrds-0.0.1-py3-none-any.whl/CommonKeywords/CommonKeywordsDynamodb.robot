*** Settings ***
Documentation  Traverse through the API response and get the required data to verify with Dynamo DB with UI/API data.
Library      dbKeywords.py
Resource     CommonKeywordsAPI.robot
Library        data_type_conversion.py

*** Variables ***
${AttValue}     KANSAS_PLANT
${AttKey}       entityId
${table}    SFW_OEEIntermediateTable

*** Keywords ***
#### Implemented by Saranya #############
Get DB data
    [Arguments]     ${table}    ${AttKey}      ${AttValue}    ${AWSAccessKey}    ${AWSSecretKey}
    ${Response}     Connect To Db     ${table}      ${AttKey}       ${AttValue}    ${AWSAccessKey}    ${AWSSecretKey}   ${regionname}


Write Date and Test Name to CSV file
    [Arguments]    ${Filepath}    ${Date}    ${TestCaseName}
    toWriteDateAndTestName     ${Filepath}    ${Date}    ${TestCaseName}


Write Data Traceability to CSV File
    [Arguments]    ${JsonFilepath}    ${Data}    ${CSVFilepath}    ${message}
    createJsonFile     ${JsonFilepath}    ${Data}
    dataTraceabilityFunction     ${CSVFilepath}    ${message}

Write data to CSV file
    [Arguments]    ${Filepath}    ${message}    ${Data}
    toWriteToCSV    ${Filepath}    ${message}    ${Data}
