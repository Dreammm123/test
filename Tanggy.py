""""Grade"""
def main():
    """Grade"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00:
        sec = 4-grade
        print("%.2f" %sec)
    else:
        print("I'm so happy.")
main()
