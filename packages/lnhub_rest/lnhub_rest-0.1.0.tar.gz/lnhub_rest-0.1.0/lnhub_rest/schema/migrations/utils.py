def include_name(name, type_, parent_names):
    if type_ == "schema":
        return name in {None, "core"}  # only consider public schema
    else:
        return True
