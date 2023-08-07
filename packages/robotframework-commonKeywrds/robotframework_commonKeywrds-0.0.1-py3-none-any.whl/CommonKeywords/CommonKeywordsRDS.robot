#### Implemented by Sam and Sowmyashree  ####
*** Settings ***
Library         DatabaseLibrary
Library         OperatingSystem
Library         SeleniumLibrary
Library         Collections
Library         String
Library         ../CommonKeywords/data_type_conversion.py
Resource        ../Properties.robot

*** Keywords ***

Connect To RDS
    [Arguments]      ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    Log to console   ++++    ${DBUser}
    Connect To Database  pymysql  ${DBName}   ${DBUser}   ${DBPass}   ${DBHost}   ${DBPort}

Disconnect DB
    Disconnect From Database

Validate data from RDS tables
    [Arguments]      ${Table_query}      ${Table_Columnheader}    ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    Connect To RDS    ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    @{list}=    create list
    @{QueryValue}=      Query     ${Table_query}
    @{column}=          query      ${Table_Columnheader}
    ${length}=    get length    ${column}
    FOR   ${i}   IN     ${column}
        FOR  ${index}  IN RANGE    0       ${length}
           append to list    ${list}    ${i}[${index}][0]
         END
    END
    FOR	    ${row}	IN	    @{QueryValue}
            &{dict1}=    ListToDict     ${list}     ${row}
            #log to console      ${dict1}
            Set Global Variable  ${dict1}
    END

Validate values from table
    [Arguments]     ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}    ${query}
    Connect To RDS     ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    @{list}=    create list
    @{QueryValue}=      Query     ${query}
    #log to console   ${QueryValue}
    &{dict4}=    Convert To Dictionary  ${QueryValue}
    #log to console  ${dict4}
    Set Global Variable  ${dict4}

Validate data from RDS tables using lists
    [Arguments]      ${Table_query}      ${Table_Columnheader}    ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    Connect To RDS    ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    @{query_list}=  create list
    @{list}=    create list
    @{QueryValue}=      Query     ${Table_query}
    @{column}=          query      ${Table_Columnheader}
    ${length}=    get length    ${column}
    FOR   ${i}   IN     ${column}
        FOR  ${index}  IN RANGE    0       ${length}
           append to list    ${list}    ${i}[${index}][0]
         END
    END

    FOR	    ${row}	IN	    @{QueryValue}
            ${val}=     convert to list     ${row}
            append to list      ${query_list}   ${val}
    END
    Set Global Variable  ${query_list}
    
Validate data from RDS tables
    [Arguments]      ${DB_query}     ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    Connect To RDS     ${DBUser}     ${DBName}    ${DBPass}     ${DBHost}     ${DBPort}
    @{QueryValue}=      Query     ${DB_query}
    ${length}=    get length    ${QueryValue}
    @{BusinessUnitsRDS}     create list
    FOR     ${ele2}     IN RANGE        0       ${length}

            ${name}=        Convert to List     ${QueryValue}[${ele2}]
            Append To List     ${BusinessUnitsRDS}     ${name[0]}
    END
    Set Global Variable     ${BusinessUnitsRDS}

To execute RDS query for respective data
    [Arguments]      ${DB_query}    ${column}    ${columnValue}
    ${DB_query1}=       Replace String      ${DB_query}     ${column}        ${columnValue}
    @{QueryValue}=      Query     ${DB_query1}
    Set Global Variable    ${QueryValue}

