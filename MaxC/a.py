
def add(uu,okok,abc):
    uu[okok] = abc
    return(okok,"added!")
def remove(uu,okok):
    uu.pop(okok)
    return(okok,"are deleted!")
def prunt(uu):
    oo = ""
    oo += """
phone         last name         first name 
========================================="""
    for k in (uu):
        uu[k]
        oo += f"""
{k:13} {uu[k][1]:17} {uu[k][0]}"""
    return(oo)

