*** Settings ***
Documentation    Suite description
Library         customLibrary/TestCases.py
Library         customLibrary/TabBar.py
#Library         customLibrary/AppuimSessionHandler.py
Library         customLibrary/General.py
Library         customLibrary/Tradestab.py




*** Test Cases ***
NOBIAPP52
    [Tags]    DEBUG
    open application
    trades tab
    ${average_price}=   get average price
    send price  ${average_price}
    send ammount  0.1
    click buy
    find no funds


NOBIAPP53
    [Tags]    DEBUG
    open application
    trades tab
    select order type changer
    select fast order type
    click 100 percent
    click increase amount
    click buy
    find no funds

NOBIAPP54
    [Tags]    DEBUG
    open application
    trades tab
    select order type changer
    select trigger order type
    send trigger ammount   4444
    click 100 percent
    click increase amount
    click increase amount
    click buy
    find no funds
NOBIAPP59
    [Tags]    DEBUG
    open application
    trades tab
    select order type changer
    select fast order type
    click 100 percent
    click increase amount
    click buy
    find no funds
NOBIAPP60
    [Tags]    DEBUG
    NOBIAPP60
NOBIAPP55
    [Tags]    DEBUG
    open application
    trades tab
    select sell button
    ${average_price}=   get average price
    send price  ${average_Price}
    click 100 percent
    click increase amount
    click increase amount
    click sell
    find no funds
NOBIAPP61
    [Tags]    DEBUG
    NOBIAPP61
NOBIAPP56
    [Tags]    DEBUG
    open application
    trades tab
    select sell button
    select order type changer
    select fast order type
    click 100 percent
    click increase amount
    click increase amount
    click sell
    find no funds
NOBIAPP57
    [Tags]    DEBUG
    open application
    trades tab
    select order type changer
    select trigger order type
    ${average_price}=  get average price
    send price  ${average_price}
    send trigger ammount  ${average_price}
    click 100 percent
    click increase amount
    click increase amount
    click buy
    find no funds


