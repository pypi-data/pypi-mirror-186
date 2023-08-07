*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    JSONLibrary
Library    Collections
Library    OperatingSystem
#Library    CryptoLibrary    variable_decryption=True
Library    Screenshot
Library    String
Library    DateTime
Library    DateTime1.py
Resource  ../Properties.robot
Documentation    This file contains all the common keywords required in project

*** Keywords ***
Launch Chrome
    [Arguments]    ${URL}
    ${ChromeOptions} =    evaluate    sys.modules['selenium.webdriver'].ChromeOptions() sys, selenium.webdriver
    call method    ${ChromeOptions}    add_argument     --ignore-certificate-errors
#### implemented by Sai Saranya ###
Before Suite
    [Documentation]     Logs in to the application
    [Arguments]     ${URL}
    SeleniumLibrary.Set Screenshot Directory  ../../../Screenshots
    Open Browser and go to URL      ${URL}
    #Login to the application    ${USERNAME}    ${Password}

After Test
    [Documentation]  Generates screenshots in directory and Current page control shifts to Globe page
    [Arguments]    ${locator}    ${value}
    #Run Keyword If Test Failed      Capture Page Screenshot     ${TEST NAME}-${TEST STATUS}.png
    Wait and Click Element    ${locator}    ${value}

After Suite
    [Documentation]     Closes the browser
    Close Browser

Open Browser and go to URL
    [Documentation]     Starts Browser and goes to the URL specified in environment variables
    [Arguments]     ${URL}
    open browser    ${URL}    ${BROWSER}   options=add_argument("--ignore-certificate-errors")     executable_path=${DriverPath}
#   open browser   ${URL}    ${BROWSER}    options=add_argument("--ignore-certificate-errors")   remote_url=https://selenium.sdlc.deloitteinnovation.us
#    Create webdriver    ${Browser}  executable_path=${DriverPath}
    Maximize Browser Window
    reload page
    sleep   2s
    Set Selenium Timeout    30s
    #Go To   ${URL}
    ##open browser    ${PocUrl}    ${BROWSER}   executable_path=${DriverPath}

wait and set text
    [Arguments]    ${locator}    ${value}
    wait until element is visible    ${locator}    40
    input text    ${locator}    ${value}

wait and select from dropdown
    [Arguments]    ${field}    ${value}    ${NameDropdown}
    wait until element is visible    ${field}    30
    input text    ${field}  ${value}
    wait until element is visible   ${NameDropdown}    30
    click element    ${NameDropdown}

wait and select from list
    [Arguments]    ${field}    ${fielddrop}
    wait until element is visible    ${field}    30
    click element    ${field}
    wait until element is visible    ${fielddrop}
    click element    ${fielddrop}

wait and get text
    [Arguments]    ${field}
    wait until element is visible    ${field}   30
    ${text}=   get text    ${field}
    [Return]    ${text}

wait and get value
    [Arguments]    ${field}
    wait until element is visible    ${field}   10
    ${value}=   get value    ${field}
    [Return]    ${value}

Asserting Field Value
    [Arguments]    ${field}    ${value}
    log to console    ${field}_${value}
    wait until page contains element    ${field}
    element attribute value should be    ${field}  value    ${value}

############## Implemented by Sam ############################
Selecting the Radio button
    [Documentation]     Selecting the Radio Button
    [Arguments]    ${L_Radiobutton}
    wait until element is visible       ${L_Radiobutton}
    click element   ${L_Radiobutton}

Test Convert To Integer
    [Documentation]     Converting string to integer
    [Arguments]    ${V_item}
    ${V_act} =    Convert To Integer    ${V_item}

Select Calendar Date
    [Documentation]     Select a Calendar Date on UI
    [Arguments]     ${L_DateCalendarIcon}     ${V_ExpecetdMonthYear}  ${L_Arrowbutton}    ${L_date}   ${V_ExpectedDate}    ${L_MonthWebElement}
    click element      ${L_DateCalendarIcon}
    FOR     ${Index}    IN RANGE    13
        ${MonthYear}=  get webelement  ${L_MonthWebElement}
        ${MonthYearText}=   get text    ${MonthYear}
        #log to console      ${MonthYearText}
        exit for loop if  '${MonthYearText}'=='${V_ExpecetdMonthYear}'
        click button  ${L_Arrowbutton}
        sleep  1
    END
    ${TotalDateList}=  get webelements   ${L_date}
    FOR     ${RequiredDate}    IN   @{TotalDateList}
        ${RequiredDateText}=    get text    ${RequiredDate}
        #log to console  ${RequiredDateText}
        run keyword if    '${RequiredDateText}'=='${V_ExpectedDate}'     click element   ${RequiredDate}
        sleep   2
        exit for loop if    '${RequiredDateText}'=='${V_ExpectedDate}'
    END


Validating text
    [Documentation]     Validating text Messages
    [Arguments]     ${L_txtmessage}     ${expected_message}
    wait until element is visible   ${L_txtmessage}
    element text should be      ${L_txtmessage}       ${expected_message}

Uploading a file to UI
    [Documentation]     Uploading any file to upload cases on UI
    [Arguments]     ${L_uploadpath}     ${FilePath}
    Wait Until Element Is Enabled    ${L_uploadpath}
    # Is there an equal to sign here
    ${Normal_FilePath}    Normalize Path  ${FilePath}
    choose file     ${L_uploadpath}     ${Normal_FilePath}

Uploading an image to UI
    [Documentation]     Uploading any image to upload cases on UI
    [Arguments]     ${L_uploadpath}     ${FilePath}
    Wait Until Element Is Enabled    ${L_uploadpath}
    # Is there an equal to sign here
    ${Normal_FilePath}    Normalize Path  ${FilePath}
    choose file     ${L_uploadpath}     ${Normal_FilePath}

click on element using JavaScript
    [Arguments]     ${locator}
    Wait Until Element Is Visible    ${locator}     30s
    ${clickElement}    Get WebElement    ${locator}
    Execute Javascript    arguments[0].click();     ARGUMENTS       ${clickElement}

Element should have class
    [Arguments]     ${element}  ${className}
    Wait Until Page Contains Element    ${element}\[@class='${className}']

#### implemented by Sai Saranya ###
Wait and Click Button
    [Arguments]     ${Locator}  ${V_Duration}
    Wait Until Element is Visible    ${Locator}        ${V_Duration}
    Click Button    ${Locator}

Wait and Click Element
    [Arguments]     ${Locator}  ${V_Duration}
    Wait Until Element is Visible    ${Locator}        ${V_Duration}
    Click Element    ${Locator}

Wait and DoubleClickElement
    [Arguments]     ${Locator}  ${V_Duration}
    Wait Until Element is Visible    ${Locator}        ${V_Duration}
    Double Click Element    ${Locator}

Wait and Choose File
    [Arguments]  ${L_fileUpload}  ${V_File_Path}  ${V_Duration}
    Wait Until Element Is Visible    ${L_fileUpload}    ${V_Duration}
    Choose File    ${L_fileUpload}    ${V_File_Path}
    Sleep    10s
    #Click Element    ${L_Submit}

Select the text from the dropdown by Value
    [Arguments]     ${V_Value}   ${L_dropdown}
    Scroll Element Into View    ${L_dropdown}
    Wait Until Element Is Visible   ${L_dropdown}
    Select From List By Value       ${L_dropdown}  ${V_Value}

Select the text from the dropdown by Index
    [Arguments]     ${V_Value}   ${L_dropdown}    ${V_Index}
    Scroll Element Into View    ${L_dropdown}
    Wait Until Element Is Visible   ${L_dropdown}
    Select From List By Index       ${L_dropdown}  ${V_Index}

Enter text into textbox
    [Arguments]     ${L_TextBox}    ${V_Text}   ${V_Duration}
    Wait Until Element Is Visible    ${L_TextBox}   ${V_Duration}
    Input Text    ${L_TextBox}    ${V_Text}

Get CSS Property Value
    [Documentation]  Get the CSS property value of a web element
    [Arguments]    ${locator}    ${attribute name}
    ${css}=         Get WebElement    ${locator}
    ${prop_val}=    Call Method       ${css}    value_of_css_property    ${attribute name}
    [Return]     ${prop_val}

##Example: smar-automationsuite/UI/D2DScreens/D2DTestCases/OEETest.robot
Get text values of the WebElements list
   [Documentation]     Takes Webelements list as input and returns the list with text of those webelements
   [Arguments]     ${V_List}
   @{V_textList}  create list
   FOR  ${element}  IN  @{V_List}
        Wait Until Element Is Visible    ${element}     40
        ${text}=  Get Text  ${element}
        Append To List  ${V_textList}  ${text}
   END
   set global variable  ${V_textList}
   return from keyword  ${V_textList}


Select an element from the list
    [Documentation]     Clicks on a webelement by selecting it using "text of the element" from the list of webelements
    [Arguments]     ${V_Text}   ${V_List}
    FOR   ${element}  IN    @{V_List}
        Wait Until Element Is Visible    ${element}
        IF    "${element.text}"== ${V_Text}
            Click Element    ${element}
            Sleep    20s
            Exit For Loop
        ELSE
            Continue For Loop
        END
    END

#### Implemented by Sowmyashree  ####
Selecting the Checkbox
        [Arguments]     ${L_checkbox}
        wait until element is visible  ${L_checkbox}
        Select Checkbox     ${L_checkbox}

Unselecting the checkbox
        [Arguments]     ${L_unselectcheckbox}
        wait until element is visible  ${L_unselectcheckbox}
        unselect checkbox  ${L_unselectcheckbox}

Selecting complete text
        [Arguments]     ${L_originaltextmessage}    ${ExpectedText}
        wait until element is visible   ${L_originaltextmessage}
        ${completetext}=   get webelement  ${L_originaltextmessage}
        ${text}=    get text    ${completetext}
        Element Text Should Be  ${text}  ${ExpectedText}

Selecting partial text
        [Arguments]     ${L_originaltextmessage}    ${ExpectedText}     ${V_splittext}     ${V_indexofrequiredtext}
        wait until element is visible  ${L_originaltextmessage}
        ${original_message}=    get text        ${L_originaltextmessage}
        log to console      ${original_message}
         @{message_list}=     split string        ${original_message}     ${V_splittext}
         log to console       ${message_list}
         ${splited_required_text}    get from list   ${message_list}     ${V_indexofrequiredtext}
         log to console      ${splited_required_text}
        Element Should Contain    ${splited_required_text}      ${ExpectedText}

Verify empty text field of an element
    [Arguments]     ${Locator}
    Element Should Be Enabled    ${Locator}
    ${value}     Get Element Attribute    ${Locator}    value
    Should Be Empty    ${value}

#Implemented by Paras
Get Date
      [Documentation]  This Keyword will return current or future date depending upon Argument passed.
      [Arguments]   ${AddDays}=0
      ${date}=      Get Current Date      UTC      exclude_millis=yes
      ${newdate}=   Add Time to Date      ${date}   ${AddDays} Days
      ${convert}=      Convert Date      ${newdate}      result_format=%m_%d_%Y
      [Return]   ${convert}

#Implemented by Prachi
Date to Epoch Convertor
    [Documentation]     This Keyword will convert date to millisecond epoch.
    [Arguments]    ${date}
    ${epochdate}=    convert date   ${date}     epoch      date_format=%m_%d_%Y    exclude_millis=Yes
    ${epochdate}=    convert to string   ${epochdate}
    ${epochdate}    get substring   ${epochdate}  0  10
    ${millisecondEpochDate}      Evaluate  ${epochdate}*1000
    [Return]    ${millisecondEpochDate}


###Implemented by Saranya
Select dropdown value
    # Ex:Select dropdown value in system administration page   {L_Roledropdown}   {L_RolesAvailable}      'Plant Manager'
    [Arguments]       ${dropdown}   ${list}   ${V_Valuetobeselected}
    Set Browser Implicit Wait    5s
    Get dropdown values in list    ${dropdown}   ${list}
    List Should Contain Value    ${Values_UI}    ${V_Valuetobeselected}
    ${index}    Get Index From List    ${Values_UI}    ${V_Valuetobeselected}
    #adding index of "select value " such as select role/bu...   greyedout text index
    ${locatorofvalue}   Catenate    (${list})     [${index+1}]
    Element Should Be Enabled       ${locatorofvalue}
    Wait and click Element          ${locatorofvalue}      20s

Get dropdown values in list
    [Arguments]      ${dropdown}   ${list}
    Wait and click element  ${dropdown}   20s
    Wait Until Element Is Visible    ${list}     30s
    @{list1}    Get WebElements    ${list}
    @{Values_UI}    Get text values of the WebElements list    ${list1}
#    Wait and Click Element    ${L_BU_global}     30s
#   Log To Console    Values of dropdown:${Values_UI}
    Set Global Variable    ${Values_UI}

Logout from application
    [Arguments]    ${Arrow}    ${button}
    wait until element is visible    ${Arrow}   20s
    Sleep    20s
    click element    ${Arrow}
    click element    ${button}

Close Browser and Open it again
    #Close the Browser and Open it again
    Close Browser
    Open Browser and go to URL      ${URL.QA}

#### Implemented by Ritika #####
Verify attribute values
     [Arguments]       ${L_RoleNameText}       ${Text}     ${AttributeValue}
     Element Should Be Enabled    ${L_RoleNameText}
     ${id}    Get Element Attribute        ${L_RoleNameText}       ${AttributeValue}
#     log to console     ${id}
     Should Be Equal As Strings      ${id}      ${Text}

Clear Text field and input Text
     [Arguments]       ${Locator}       ${Text}    ${timeout}
     wait until element is visible     ${Locator}      60s
     press keys     ${Locator}   CTRL+A+DELETE
     sleep      ${timeout}
     input text     ${Locator}      ${Text}

Verify if Save button is disabled
      [Arguments]           ${Locator}
      wait until element is visible       ${Locator}       30
      element should be visible    ${Locator}

Verify if Save button is enabled
      [Arguments]           ${Locator}
      wait until element is visible       ${Locator}       30
      element should be visible    ${Locator}

Verify Error Message
        [Arguments]         ${Locator}      ${Message}
        ${NotEmptyText}=         get text       ${Locator}
        should be equal as strings      ${NotEmptyText}         ${Message}

Clear Input Field
        [Arguments]           ${Locator}
        Sleep       1s
        click element         ${Locator}
        Sleep       1s
        Press Keys            ${Locator}             CTRL+A
        Sleep       3s
        Press Keys            None             BACKSPACE

Click on Save Button
      [Arguments]           ${Locator}
      wait until element is visible         ${Locator}        20
      Sleep         2s
      click on element using javascript         ${Locator}
      Sleep         2s

Verify Successfull Message
      [Arguments]           ${Locator}      ${Message}   ${Element}   ${timeout}  ${StringToVerify}   ${String}
      wait until element is visible     ${Locator}        50
      element should be visible     ${Locator}
      element text should be        ${Locator}      ${Message}
      wait until element is visible         ${Element}         ${timeout}
      ${CompletedText}=      get text      ${Element}
      should be equal as strings     ${StringToVerify}         ${String}

erify Successfull Message after clicking on Save
      [Arguments]           ${Locator}      ${Message}     ${timeout}
      wait until element is visible     ${Locator}       ${timeout}
      element should be visible     ${Locator}
      element text should be        ${Locator}      ${Message}

Verify Successfull Message After Uploading File
      [Arguments]           ${Locator}      ${Message}     ${timeout}
      wait until element is visible     ${Locator}        ${timeout}
      element should be visible     ${Locator}
      element text should be        ${Locator}      ${Message}

Select Dropdown value for RefreshRate
        [Arguments]         ${Locator}      ${Value}     ${timeout}
        wait until element is visible       ${Locator}        ${timeout}
        Sleep       5s
        click element       ${Locator}
        wait until element is visible       ${Value}        ${timeout}
        sleep       5s
        click on element using javascript       ${Value}
        ${TimeText}=        get text        ${Locator}
        set global variable     ${TimeText}

Upload the XLSX File
        [Arguments]         ${File_Input}       ${File_Path}
        sleep      10s
        ${File_Path1}    Normalize Path  ${File_Path}
        choose file         ${File_Input}       ${File_Path1}

Get current dateTime for Asia
    ${Current_Date}     currentDateTime
    Set Global variable      ${Current_Date}
    [Return]        ${Current_Date}

Get current date for Asia
    ${Current_Date}     currentDateTime1
    Set Global variable      ${Current_Date}
    [Return]        ${Current_Date}

Click and Verify Save Message Displayed
        [Arguments]         ${Savebtn}       ${Locator}         ${Message}
        Verify if Save button is enabled        ${Savebtn}
        click element       ${Savebtn}
        Log To Console    Clicked on Save button
        wait until element is visible        ${Locator}        40
        element text should be          ${Locator}          ${Message}
        Log To Console    Success message post save button is verified

Wait and Hover On Element
    [Arguments]    ${Hover_Element}
    Wait Until Element Is Visible    ${Hover_Element}      50s
    Mouse Over     ${Hover_Element}

Remove XLSX File
        [Arguments]         ${FilePath}      ${ResourcesDir}
        Remove File         ${FilePath}
        @{L2}  List Files in Directory     ${ResourcesDir}      absolute= true




