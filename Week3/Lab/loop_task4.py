# TASK: Amend your previous solution so that if any value within the list is found to be over
# 100 then the loop should break immediately

numbers = [10,36, 200, 30, 22, 11,2,244,12]
for i in numbers:
    if i>100:
        break
    else:
        print(i)