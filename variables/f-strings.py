pi = 3.14159265359

# f strings are a simpler way to format strings with data inputs.

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f"Pi to 3 decimal places: {str(pi)[:5]}")

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f"Pi to 3 decimal places: {str(pi)[:7]}")

score = 16

max_score = 26

score_as_decimal = score / max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f"You scored {score_as_decimal}")


# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f"You scored {score_as_decimal * 100} %")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g.
# 'You scored 61.54%'
print(f"You scored {score_as_decimal:.2%}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g.
# 'You scored 62%'
print(f'You scored {round(score_as_decimal * 100)}%')

