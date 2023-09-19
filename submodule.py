def extract_first_number_from_string(string_to_search):
    import re
    pattern = r'\d+'
    match = re.search(pattern, string_to_search)
    if match:
        matched_number = match.group()        
        return int(matched_number)
    else:
        return -1