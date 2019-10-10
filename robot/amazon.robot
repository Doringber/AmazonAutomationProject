*** Settings ***
Library  SeleniumLibrary
Suite Setup     Open Home Page
Suite Teardown  Close Browsers


*** Variables ***
${URL}          https://www.amazon.in/
${BROWSER}      chrome

*** Keywords ***

Open Home Page
    Open browser    ${URL}   ${BROWSER}

Close Browsers
    Close All Browsers


Click search box
    [Arguments]
    Click Button	id:twotabsearchtextbox

Enter Text to search
    [Arguments]      ${text}
    Input Text	   id:twotabsearchtextbox  ${text}

Click on sumbit button
    [Arguments]
    Click Button	css:input[type='submit']

Verify the text found on the screen
    [Arguments]
    wait until page contains  "iphone xr"


*** Test Cases ***
Verify search field on home screen
    [Tags]	    amazon_search sanity
    [Documentation]   As a user can open the amazon home page and see the tagline

    Click search box
    Enter Text to search  iphone xr
    Click on sumbit button
    Verify the text found on the screen



