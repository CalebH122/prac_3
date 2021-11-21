def main():
    score = float(input("Enter score: "))
    while score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    score_parameter(score)


def score_parameter(score):
    if score > 100:
        print("Invalid score")
    elif 50 <= score < 90:
        print("Passable")
    elif 90 <= score <= 100:
        print("Excellent")
    elif score < 50:
        print("Bad")

main()
