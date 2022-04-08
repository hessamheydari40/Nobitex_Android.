*** Settings ***
Documentation    Suite description
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
NOBIAPP5
    [Tags]    DEBUG
    open application
    trades tab
    select order type changer
    select fast order type
    click 100 percent
    click buy
    click confirm
    find succesfull
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
NOBIAPP4
    [Tags]    DEBUG
    open application
    trades tab
    click 100 percent
    click buy
    click confirm
    find succesfull
NOBIAPP6
    [Tags]    DEBUG
    open application
    trades tab
    select order type changer
    select trigger order type
    click 100 percent
    send trigger ammount  12333
    click buy
    click confirm
    find succesfull
NOBIAPP7
    [Tags]    DEBUG
    open application
    trades tab
    select sell button
    ${average_price}=   get average price
    send price  ${average_price}
    click 100 percent
    click sell
    click confirm
    find succesfull
NOBIAPP8
    [Tags]    DEBUG
    open application
    trades tab
    select sell button
    select order type changer
    select fast order type
    click 100 percent
    click sell
    click confirm
    find succesfull
NOBIAPP9
    [Tags]    DEBUG
    open application
    trades tab
    select sell button
    select order type changer
    select trigger order type
    click 100 percent
    ${average_price}=   get average price
    send price  ${average_price}
    send trigger ammount  111112
    click sell
    click confirm
    find succesfull
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


