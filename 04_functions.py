def result_for(score):
    if score >= 50:
        return "Pass"
    return "Try again"


print(result_for(64))
print(result_for(42))
