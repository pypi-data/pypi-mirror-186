def getter(dict_or_obj, field_name, default):
    if isinstance(dict_or_obj, dict):
        return dict_or_obj.get(field_name, default)
    else:
        getattr(dict_or_obj, field_name, default)
