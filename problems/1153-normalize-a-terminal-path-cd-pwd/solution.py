def normalize_path(cwd, dest, home="/home/user", env=None):
    env = env or {}

    # Step 1: expand '~' and '$NAME' components in dest (before normalization)
    if dest == "~" or dest.startswith("~/"):
        dest = home + dest[1:]
    parts = []
    for comp in dest.split("/"):
        if comp.startswith("$") and len(comp) > 1:
            parts.append(env.get(comp[1:], ""))
        else:
            parts.append(comp)
    dest = "/".join(parts)

    # Step 2: choose the starting point
    full = dest if dest.startswith("/") else cwd + "/" + dest

    # Step 3: normalize with a stack
    stack = []
    for comp in full.split("/"):
        if comp == "" or comp == ".":
            continue
        if comp == "..":
            if stack:
                stack.pop()
        else:
            stack.append(comp)
    return "/" + "/".join(stack)