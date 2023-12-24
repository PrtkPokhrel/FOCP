# TASK: Amend your previous solution once again, so that the message “all numbers
# processed” is printed when the loop completes, but only if all values were less or equal to
# 100 (i.e. the loop did not break early)


numbers = [10, 336, 100, 30, 22, 11, 2, 44, 12]

for i in numbers:
    if i > 100:
        break
    else:
        print(i)
else:
    print("Loop is complete")


