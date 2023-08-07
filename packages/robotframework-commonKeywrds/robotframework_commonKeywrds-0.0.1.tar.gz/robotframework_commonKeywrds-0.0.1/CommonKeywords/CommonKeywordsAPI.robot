*** Settings ***
Library  SeleniumLibrary
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Library   OperatingSystem
Library    String
Resource  ../Properties.robot
Resource        ../CommonKeywords/CommonKeywordsUI.robot
Resource        ../CommonKeywords/CommonKeywordsRDS.robot


*** Variables ***
${firstname}    QA
${lastname}     Test
${emailId}      QATest@deloitte.com

############## Implemented by Ritika ############################
*** Keywords ***
Get Method
     [Arguments]  ${base_url}  ${resource_url}   ${params}
     ${response}=   Get  ${base_url}/${resource_url}   params=${params}
     ${jsobject}      Set Variable   ${response.json()}
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}
     Log   ${jsobject}

Get Method With Headers
     [Arguments]  ${base_url}  ${resource_url}   ${params}  ${accessToken}
     ${Headers}  create dictionary  Authorization=${accessToken}   Content-Type=application/json
     ${response}=   Get  ${base_url}/${resource_url}   params=${params}   headers=${Headers}
     Set Global Variable  ${response}znxnm
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}
     Log   ${jsobject}

Get Method With Headers no params
     [Arguments]  ${base_url}  ${resource_url}   ${accessToken}
     ${Headers}  create dictionary  Authorization=${accessToken}   Content-Type=application/json
     ${response}=   Get  ${base_url}/${resource_url}     headers=${Headers}
     Set Global Variable  ${response}
     ${jsobject}      Set Variable   ${response.json()}
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}
     Log   ${jsobject}

Post Method
     # Create a dictionary name ReqstBody and pass the required json in this dictionary
     [Arguments]  ${base_url}  ${resource_url}   ${ReqstBody}
     ${response}=   Post  ${base_url}/${resource_url}   json=${ReqstBody}
     ${jsobject}      Set Variable   ${response.json()}
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}
     Log   ${jsobject}

Post Method With Headers
     # Create a dictionary name ReqstBody and pass the required json in this dictionary
     # Create a dictionary name header and pass the accesstoken and content-type in this dictionary
     [Arguments]  ${base_url}  ${resource_url}   ${ReqstBody}    ${accessToken}    ${expectedStatus}=200
     ${Headers}  create dictionary  Authorization=${accessToken}   Content-Type=application/json
     ${response}=   Post  ${base_url}/${resource_url}   json=${ReqstBody}   headers=${Headers}   expected_status= ${expectedStatus}
     ${jsobject}      Set Variable   ${response.json()}
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}

PUT Method
     # Create a dictionary name ReqstBody and pass the required json in this dictionary
     [Arguments]  ${base_url}  ${resource_url}   ${ReqstBody}
     ${response}=   Put  ${base_url}/${resource_url}   json=${ReqstBody}
     ${jsobject}      Set Variable   ${response.json()}
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}
     Log   ${jsobject}

JsonReading
    [Arguments]    ${InputFile}  ${level1}    ${level2}
    ${INPUT1}=    get file    ${InputFile}
    ${json}    evaluate    json.loads('''${INPUT1}''')    json
    [Return]   ${json[${level1}][${level2}]}

Validate content of the response
     [Arguments]  ${jsobject}  ${ContentToExtract}  ${ActualValue}
     ${tarAvail}=   Get Value From Json  ${jsobject}  ${ContentToExtract}
     ${text}=   Convert To String  ${tarAvail}
     Log   ${text}
     Should Be Equal As Strings   ${text}  ${ActualValue}


Validate status code
     [Arguments]  ${ExpectedStatusCode}  ${ResponseStatusCode}
     should be equal  ${ResponseStatusCode}  ${ExpectedStatusCode}

## Fetch the token to execute API's ###
Get authToken
     ${ReqstBody}=    Create Dictionary      SecretKey=xyz     ClientId=xyz
     ${headers}=   Create Dictionary     X-Amz-Target=AWSCognitoIdentityProviderService.InitiateAuth       Content-Type=application/x-amz-json-1.1
     ${resp}=    Post   ${baseUrl}   json=${ReqstBody}    headers=${Headers}
     ${jsobject}      Set Variable   ${resp.json()}
     Should Be Equal As Strings  ${resp.status_code}     200
     ${value} =	 Get Value From Json	${jsobject} 	$.AuthenticationResult.AccessToken
     ${value}=  convert to string   ${value}
     ${value}  Remove String   ${value}    ['
     ${value}  Remove String   ${value}    ']
     ${Access_token} =   Catenate    Bearer ${value}
     Set Global Variable   ${Access_Token}
     #${Access_Token}=    Get Auth Token Workaround
     ${Access_token} =   Catenate    Bearer ${Access_Token}
     Set Global Variable   ${Access_Token}

VerifyAPIResponse
    [Arguments]   ${InputFilePath}  ${jsonObject}     ${jsonPath}
    ${Input}=   get file    ${InputFilePath}
    ${data}    evaluate    json.loads('''${Input}''')    json
    @{actual_field_List}=   Get Value From Json   ${jsonObject}  ${jsonPath}
    ${actual_field}=  Get From List   ${actual_field_List}  0
    Should Be Equal    ${actual_field}  ${data["${jsonPath}"]}

Evaluate Type of data
    [Tags]      Common Keyword
    [Arguments]     ${V_element}
    ${type}	    Run Keyword And Ignore Error	    Evaluate    type(${V_element}).__name__
    ${type_substring}    Get Substring    ${type}[1]    0    10
    Return From Keyword     ${type_substring}

Get API data
    [Arguments]     ${base_url}     ${ResourceURL}   ${params}  ${AttKey}      ${AttValue}
    ${Response}     Get Method With Headers    ${base_url}     ${ResourceURL}   ${params}     ${Access_token}
    ${Length}   Get Length    ${JSobject}[data]
    FOR    ${Element}    IN RANGE    0    ${Length}
            Get Data from API response      ${JSobject}[data][${Element}]     ${AttKey}      ${AttValue}
    END

Get Data from API response
    [Documentation]  Gets the block of required data from API response
    [Tags]      Common Keyword
    [Arguments]    ${JSONResponse}      ${AttrKey}   ${AttrValue}
    set Global Variable   ${AttrKey}
    set global variable   ${AttrValue}
    Recursive Call  ${JSONResponse}
Recursive Call
    [Documentation]     Input : Dictionary, Action : Traverses and fetch the required data from
    ...     nested Dictionaries and lists. Attkey and Attvalue should be specified in global variables
    ...     to check the condition.
    [Tags]      Common Keywords
    [Arguments]     ${Dict}
    ${Values}   Get Dictionary Values    ${Dict}
    ${Keys}     Get Dictionary Keys    ${Dict}
    Get Length    ${Values}
    ${bool}     Run Keyword and Return Status    List Should Contain Value    ${Values}      ${AttrValue}
    FOR  ${element}  IN     @{Values}
        IF      ${bool}
           ${index}     Get Index From List    ${Values}      ${AttrValue}
           ${Key}       Get From List    ${Keys}    ${index}
           IF    "${Key}"=="${AttrKey}"
                &{DATA}     Copy Dictionary     ${Dict}
                Set Global Variable    ${Data}
#               Return From Keyword  ${Dict}
#                Pass Execution    PASSED
                Exit For Loop
           END
        ELSE
            ${type}     Evaluate type of data   ${element}
            IF   "${type}"=="dict"
                Recursive Call    ${element}
            ELSE

                     IF   "${type}"=="list"
                        ${length}       Get length  ${element}
                        FOR    ${index}   IN RANGE    0   ${length}
                            ${type1}     Evaluate type of data   ${element}[${index}]
                            ${bool}     Run Keyword And Return Status    Should be Equal    ${type1}   dict
                            Exit For Loop If    "${bool}"=="False"

                            Log     ${element}[${index}]
                            Recursive Call    ${element}[${index}]

                        END

                END

            END
        END

    END


Verify if Name displayed on UI is same as in API response
    [Arguments]      ${Element}      ${resourceUrl}      ${params}     ${Path}
    Wait Until Element Is Visible    ${Element}       30
    ${Actual_Name}=  get text    ${Element}
    Set Global Variable    ${Actual_Name}
    Get Method With Headers       ${base_url}      ${resourceUrl}     ${params}     ${Access_token}
    #Log To Console    ${ResponseStatusCode}
    Validate content of the response  ${jsobject}    ${Path}    ['${Actual_Name}']

Wrapping the JSON response in a dictionary
    &{Dict2}    Copy Dictionary    ${jsobject}
    Set Global Variable    &{Dict2}


Comparing RDS and API response
    ${Result1}=     run keyword and Return status   should be equal     ${dict1}[companyName]  ${Dict2}[companyName]
    IF  ${Result1}
       log to console      TestCase Pass
    END

PUT Method for API
     [Arguments]  ${base_url}  ${resource_url}    ${Data}   ${Headers}
     ${Headers}  create dictionary  Authorization=${accessToken}   Content-Type=application/json
     ${response}=   Put  ${base_url}/${resource_url}   params=${Data}   headers=${Headers}
     ${jsobject}      Set Variable   ${response.json()}
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}

Validate data from tables
    [Arguments]      ${Table_query}      ${Table_Columnheader}   ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    Connect To RDS     ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    @{list}=    create list
    @{QueryValue}=      Query     ${Table_query}
    @{column}=          query      ${Table_Columnheader}
    ${length}=    get length    ${column}
    FOR   ${i}   IN     ${column}
        FOR  ${index}  IN RANGE    0       ${length}
           append to list    ${list}    ${i}[${index}][0]
         END
    END
    FOR        ${row}       IN     @{QueryValue}
            &{dict1}=    ListToDict     ${list}     ${row}
            #log to console      ${dict1}
            Set Global Variable  ${dict1}
    END

Delete method with Headers
     [Arguments]       ${base_url}      ${resource_url}      ${accessToken}
     ${Headers}  create dictionary  Authorization=${accessToken}   Content-Type=application/json
     ${response}=   Delete  ${base_url}/${resource_url}     headers=${Headers}
     ${jsobject}      Set Variable   ${response.json()}
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}
     Log   ${jsobject}


Put Method With Headers
     # Create a dictionary name ReqstBody and pass the required json in this dictionary
     # Create a dictionary name header and pass the accesstoken and content-type in this dictionary
     [Arguments]  ${base_url}  ${resource_url}   ${ReqstBody}    ${accessToken}
     ${Headers}  create dictionary  Authorization=${accessToken}   Content-Type=application/json
     ${response}=   Put  ${base_url}/${resource_url}   json=${ReqstBody}   headers=${Headers}
     ${jsobject}      Set Variable   ${response.json()}
     Set Global Variable  ${jsobject}
     ${ResponseStatusCode}=  convert to string  ${response.status_code}
     Set Global Variable  ${ResponseStatusCode}

Comparable String
    [Arguments]     ${API_value}
    ${String1}      Convert to String       ${API_value}
    ${String}      Remove String       ${String1}      [       ]
    [Return]        ${String}

Get File Link
    [Arguments]    ${resource_url}     ${params}        ${jsonTag}=$.data
    Get Method With Headers    ${base_url}     ${resource_url}    ${params}      ${AccessToken}
    ${actual_field_List}=   Get Value From Json   ${jsobject}       ${jsonTag}
    ${actual_field}=  Get From List   ${actual_field_List}  0
    [Return]   ${actual_field}
