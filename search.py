def search_json(json_data, search_string):
    results = []

    for item in json_data:
        for key, value in item.items():
            if search_string.lower() in key.lower() or search_string.lower() in str(value).lower():
                results.append(item)
                break  

    return results
