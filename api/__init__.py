from librouteros.query import Key


def get_filters_list(filters_dict):
    filters_list = []

    for k, v in filters_dict.items():
        if v:
            if "|" in v:
                operator, v = v.split("|")

                if operator == "==":
                    filters_list.append(Key(k) == v)
                
                elif operator == "!=":
                    filters_list.append(Key(k) != v)
                
                elif operator == ">":
                    filters_list.append(Key(k) > v)
                
                elif operator == "<":
                    filters_list.append(Key(k) < v)
            
            else:
                filters_list.append(Key(k) == v)
    
    return filters_list