# WMUL-FM Test Untilities

These are utilities that help with testing WMUL-FM's other python modules.

1. `make_namedtuple` creates one-off named tuples for concisely passing data from the fixture method to the test methods.

2. `generate_true_false_matrix_from_named_tuple` creates a list of true and false values, and a list of corresponding ids, to be passed into a pytest test fixture.

3. `assert_has_only_these_calls` receives a `unittest.mock` object and asserts that it has been called with the specified calls and only the specified calls. The counts are compared and then the `mock_calls` list is checked for the calls.

## make_namedtuple(class_name, **fields)
`class_name`: The name of the tuple class. Same as `namedtuple(class_name=)`.

`fields`: A keyword dictionary of field names and values. The names are the same as `namedtuple(field_names=)`.

`returns` A namedtuple of type `class_name`, with `field_names` corresponding to the keys of the fields dictionary and field values corresponding to the values of the fields dictionary.

`enterprise = make_namedtuple("Starship", name="U.S.S. Enterprise", registry_number="NCC-1701")`

is the same as

`starship_tuple = namedtuple("Starship", ["name", "registry_number"])`  
`enterprise = starship_tuple("U.S.S. Enterprise", "NCC-1701")`

This is useful when you want to make a one-off namedtuple. It can be used to pass data concisely from a testing fixture to the test methods.

## generate_true_false_matrix_from_namedtuple(input_namedtuple)
`input_namedtuple` A named tuple whose fields will be used to generate the True False matrix.

`returns` Two lists: true_false_matrix and test_ids. The True-False matrix is a list of the namedtuples that is of size len(input_tuple) and with the fields set to every combination of True and False. The list of ids is a list of strings that describe the corresponding tuples.

Given: `input_tuple = namedtuple("burger_toppings", ["with_cheese", "with_ketchup", "with_mustard"])`

`true_false_matrix` will be:  
```
[
    burger_toppings(with_cheese=False, with_ketchup=False, with_mustard=False),
    burger_toppings(with_cheese=True,  with_ketchup=False, with_mustard=False),
    burger_toppings(with_cheese=False, with_ketchup=True,  with_mustard=False),
    burger_toppings(with_cheese=True,  with_ketchup=True,  with_mustard=False),
    burger_toppings(with_cheese=False, with_ketchup=False, with_mustard=True),
    burger_toppings(with_cheese=True,  with_ketchup=False, with_mustard=True),
    burger_toppings(with_cheese=False, with_ketchup=True,  with_mustard=True),
    burger_toppings(with_cheese=True,  with_ketchup=True,  with_mustard=True)
]
```

and `test_ids` will be:
```
[
    'burger_toppings(with_cheese=False, with_ketchup=False, with_mustard=False)',
    'burger_toppings(with_cheese=True,  with_ketchup=False, with_mustard=False)',
    'burger_toppings(with_cheese=False, with_ketchup=True,  with_mustard=False)',
    'burger_toppings(with_cheese=True,  with_ketchup=True,  with_mustard=False)',
    'burger_toppings(with_cheese=False, with_ketchup=False, with_mustard=True)',
    'burger_toppings(with_cheese=True,  with_ketchup=False, with_mustard=True)',
    'burger_toppings(with_cheese=False, with_ketchup=True,  with_mustard=True)',
    'burger_toppings(with_cheese=True,  with_ketchup=True,  with_mustard=True)'
]
```

Note that true_false_matrix is a list of namedtuples and test_ids is a list of the string representations of those same namedtuples.

## generate_true_false_matrix_from_list_of_strings(name, input_strings):
A convenience function. It takes a string name and a list of strings, and 
returns the true-false matrix built from those values.

```
generate_true_false_matrix_from_list_of_strings(
    "burger_toppings",
    ["with_cheese", "with_ketchup", "with_mustard"]
)
```

is the equivalent of

```
burger_toppings = namedtuple(
    "burger_toppings", 
    ["with_cheese", "with_ketchup", "with_mustard"]
)
generate_true_false_matrix_from_namedtuple(burger_toppings)
```

## assert_has_only_these_calls(mock, calls, any_order=False)
`mock` a `unittest.mock` object.

`calls` a list of calls.

If `any_order` is False (the default) then the calls must be
sequential. 

If `any_order` is True then the calls can be in any order, but
they must all appear in `mock_calls`.

assert the mock has been called with the specified calls and only
the specified calls. The counts are compared and then `assert_has_calls` is called.

This is the natural continuation of `assert_called_once_with` and is based on that method.
