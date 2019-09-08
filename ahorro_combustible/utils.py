from typing import Dict, Tuple, Sequence
import collections

def count_brands(gas_stations) -> Sequence[Tuple[int, str]]:
    '''Count all the brands in the `gas_stations` input. It can be considered that
    the ``Rotulo`` entry contains the brand name of the gas station.

    Parameters
    ----------
    gas_stations : dict
        A dictionary that contains at least the equivalent structure to the
        following example.

        { 'ListaEESSPrecio': [ { 'Rótulo': 'ES DULANTZI REPSOL' }, ... ]}

    Returns
    -------
    Sequence[Tuple[int, str]]
        A sorted sequence of tuples being the first part of each tuple the count
        number of the second part, the brand name.

        The items will be sorted by the count number (highest, first) and the
        brand name.

    Examples
    --------

    >>> count_brands({'ListaEESSPrecio': [ {'Rótulo': 'A' },
    ...                                    {'Rótulo': 'B' },
    ...                                    {'Rótulo': 'A' }]})
    [(2, 'A'), (1, 'B')]

    >>> count_brands({'ListaEESSPrecio': [ {'Rótulo': 'A' },
    ...                                    {'Rótulo': 'C' },
    ...                                    {'Rótulo': 'C' },
    ...                                    {'Rótulo': 'B' }]})
    [(2, 'C'), (1, 'A'), (1, 'B')]
    '''
        
    # Through this loop I take the petrol stations brands and their quantity.
      
    lst_tup_pet_sts = [brand["Rótulo"] for brand in gas_stations["ListaEESSPrecio"]]        

    # In order to count the petrol stations brands in an efficient way we will take
    # advantage from de "Collections module".
    
    # With the "Counter method" we will create a dictionary with the whole brands and their quantity.
        
    cnt_brand_dict = collections.Counter()
    for brand in lst_tup_pet_sts:
        cnt_brand_dict[brand] += 1

    # With the "most_common method" will turn the dictionary we have, in a list of tuples,
    # ordered from most common brand to less common brand.
        
    cnt_brand_tup = cnt_brand_dict.most_common()

    # Finally, we will swap the elements in the tuples, to comply with the functions requirements.
    
    return [(b, a) for a, b in cnt_brand_tup]