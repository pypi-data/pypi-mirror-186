"""
matha
=====

Quick description
"""


def my_sum(a: float, b: float) -> float:
    print(a + b)


def van(cf: list, rate: list, norm: str = 'composed'):
    """
    Parameters
    ----------
    
    Return a new array with the same shape and type as a given array.

    Parameters
    ----------
    cf : array_like
        List of cashflow (start at period 1).
    rate : array_like
        Curve rate.
    norm : string
        Norm used : continue or composed (use exp or 1/(1+r)).

    Returns
    -------
    out : float
        Array of uninitialized (arbitrary) data with the same
        shape and type as `prototype`.

    See Also
    --------
    ones_like : Return an array of ones with shape and type of input.
    zeros_like : Return an array of zeros with shape and type of input.
    full_like : Return a new array with shape of input filled with value.
    empty : Return a new uninitialized array.

    Notes
    -----
    This function does *not* initialize the returned array; to do that use
    `zeros_like` or `ones_like` instead.  It may be marginally faster than
    the functions that do set the array values.

    Examples
    --------
    >>> a = ([1,2,3], [4,5,6])                         # a is array-like
    >>> np.empty_like(a)
    array([[-1073741821, -1073741821,           3],    # uninitialized
           [          0,           0, -1073741821]])

    """

    # Arguments validation
    if norm not in ['continue', 'composed']:
        raise ValueError(f"""
        Norm argument need to be 'continue' or 'composed'
        and it is for now: "{norm}". Please change this argument.
        """)

    if (len(cf) < len(rate)):
        raise ValueError(f"""
        The rate list need at least to be as long as the cf list.
        """)

    # Use vector
    cf = np.array(cf)
    rate = np.array(rate)


    # Get number of period
    n_period = len(cf)

    # Create discounted curve
    if norm == 'continue':
        discounted = 0

    return norm

