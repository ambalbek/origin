def score(x):
    if x>90:
        return "A"
    elif x<=90 or x>80:
        return "B"
    elif x<=80 or x>70:
        return "C"
    elif x<=70 or x>60:
        return "D"
    else:
        return "F"


def main():
    grades = (43,78,90,37,99,57,89,68,83,85,88)
    grades = sorted(grades)
    letters = list(map(score,grades))
    print(letters)


if __name__=="__main__":
    main()