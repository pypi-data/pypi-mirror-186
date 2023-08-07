*** Settings ***
Library         SeleniumLibrary
Library         Collections
Library         String
Resource        ../CommonKeywords/CommonKeywordsUI.robot
Resource        ../Properties.robot
Resource        ../CommonKeywords/CommonKeywordsAPI.robot
Library         ../CommonKeywords/data_type_conversion.py
Resource        ../CommonKeywords/CommonKeywordsRDS.robot
Suite Setup         Before Suite     ${URL.QA}
Suite Teardown      Close All Browsers

*** Variables ***
${SearchBox}       //input[@title='Search']


*** Test Cases ***
#### Google Search ####
Navigate to Google Search page
        [Tags]    Regression
        [Documentation]     Searching python in google
        wait until element is visible      ${SearchBox}       50s
        Input Text    ${SearchBox}     python
        Press Key    ${SearchBox}    \\13

