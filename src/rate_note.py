def rate_note(note :int)->str:
    if note<10 :
     return "unsuccessful"
    if note==10 or note==11:
        return "acceptable"
    if note== 12 or note==13 :
     return "good"

