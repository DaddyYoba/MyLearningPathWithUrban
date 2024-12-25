def count_calls():
    global calls
    calls += 1

def string_info(string: str):
    count_calls()
    containing = (len(string), string.upper(), string.lower())
    return tuple(containing)

def is_contains(string: str, list_to_search: list):
    count_calls()
    for stringer in list_to_search:
        if string.lower() == stringer.lower():
            return True
    return False

calls = 0
print(string_info('Capybufeta'))
print(string_info('Carmageddon'))
print(is_contains('Urban', ['imban', 'hisBaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('through', ['thorough', 'thought', 'though'])) # No matches
print(calls)