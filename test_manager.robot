*** Settings ***
Documentation    Suite description
Library         customLibrary/TabBar.py
#Library         customLibrary/AppuimSessionHandler.py
Library         customLibrary/General.py
Library         customLibrary/Tradestab.py
Library         customLibrary/Menutab.py
Library         customLibrary/MarketsTab.py
Library         customLibrary/DashboardTab.py




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
    select sell section button
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
    select sell section button
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
    select sell section button
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
    select sell section button
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
    select sell section button
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
NOBIAPP95
    [Tags]  DEBUG
    open application
    account tab
    select security
    click enable pin code
    select auto lock
    send auto lock minute  1
    click confirm auto lock
    background application  62
    find enter pin
NOBIAPP96
    [Tags]  DEBUG
    open application
    account tab
    select security
    click enable pin code
    select auto lock
    send auto lock minute  2
    click confirm auto lock
    background application  122
    find enter pin
NOBIAPP97
    [Tags]  DEBUG
    open application
    account tab
    select security
    click enable pin code
    select auto lock
    send auto lock minute  3
    click confirm auto lock
    background application  182
    find enter pin

NOBIAPP98
    [Tags]  DEBUG
    open application
    account tab
    select security
    click enable pin code
    select auto lock
    send auto lock minute  4
    click confirm auto lock
    background application  242
    find enter pin
NOBIAPP41
    [Tags]  DEBUG
    open application
    account tab
    logout click
NOBIAPP100
    [Tags]  DEBUG
    open application
    markets tab
    nobitex coins click subtab
    btc irt star click favorite
    dashboard tab
    refresh dashboard tab
    find btc starred favoriute
NOBIAPP102
    [Tags]  DEBUG
    open application
    markets tab
    nobitex coins click subtab
    nobitex toman subtab click
    click btc market
    click buy in market detail
    find btc tarde page

NOBIAPPtest
    open application
    markets tab
    nobitex coins click subtab
    nobitex toman subtab click
    nobitex tether subtab click




