## Convert Distance Units w/ Functions (Numpy Doc String)

def miles_to_kilometers(mi):
    
    """
    Converts from miles to kilometers
    PARAMETERS
    ----------
    mi: float
        distance in miles
    RETURNS
    -------
    km : float
        distance in km
    """
   
    
    km = mi * 1.60934
    
    return km


def kilometers_to_miles(km):
    
    """
    Converts from km to mi
    PARAMETERS
    ----------
    km: float
        distance in kilometers
    RETURNS
    -------
    mi : float
        distance in miles
    """
    
    mi = km / 1.60934
    
    return mi