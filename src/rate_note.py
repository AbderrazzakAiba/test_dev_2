def rate_note(note :int)->str:
    if note<10 :
     return "unsuccessful"
    if note==12:
        return "good"
    return "acceptable"
