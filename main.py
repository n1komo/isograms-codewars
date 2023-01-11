def is_isogram(string):
    if len(string) == 0: return True
    string_lowercase = string.lower()
    new_set = set(string_lowercase)
    if len(new_set) == len(string_lowercase): return True
    else: return False