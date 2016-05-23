def to_lower(s):
    char_map = {
        u"I": u"ı",
        u"İ": u"i",
    }

    for key, value in char_map.items():
        s = s.replace(key, value)

    return s.lower()


def to_upper(s):
    char_map = {
        u"ı": u"I",
        u"i": u"İ",
    }

    for key, value in char_map.items():
        s = s.replace(key, value)

    return s.upper()


def to_title(s):
    titled_s = ""
    words = s.split()

    for word in words:
        titled_s += to_upper(word[0]) + to_lower(word[1:]) + " "

    return titled_s[0:-1]
