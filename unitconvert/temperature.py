# Define functions for Temperature

def fahrenheit_to_celsius(F):
    
    """
    Converts from Fahrenheit to Celsius.
    PARAMETERS
    ----------
    F : float
        Temp in Fahrenheit
    RETURNS
    -------
    C : float
         Temp in Celcius
 
    
    """
    
    C = (F - 32)*(5/9)
   
    return C


def celcius_to_fahrenheit(C):
    """
    
    Converts from Celcius to Fahrenheit.
    PARAMETERS
    ----------
    C : float
        Temp in Celcius
    RETURNS
    -------
    F : float
         Temp in Fahrenheit

    """
    
    
    F = (C*9/5) + 32
    
    return F
