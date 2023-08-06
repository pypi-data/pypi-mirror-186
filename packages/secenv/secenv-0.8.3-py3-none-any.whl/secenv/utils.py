def escape(s) -> str:
    s = repr(str(s))
    if "$" in s and s[0] == '"':
        s = s.replace("$", "\\$")
    if "\\'" in s and s[0] == "'":
        s = s.replace("\\'", "'\"'\"'")
    return s
