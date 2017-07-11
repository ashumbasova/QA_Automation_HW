#HW2_Task_1

l = input("Please provide the line: ")

print(
    "#1. The 3rd symbol of the line: ", l[2],
    "#2. Pre-last symbol: ", l[-2],
    "#3. First 5 symbols: ", l[:5],
    "#4. Line without two last symbols: ", l[:-2],
    "#5. Only even symbol indexes: ", l[::2],
    "#6. Only odd symbol indexes: ", l[1::2],
    "#7. Reverse line: ", l[::-1],
    "#8. Reverse line: ", l[-1:0:-2],
    "#9. Length of the line is:", len(l),
    sep="\n"

)

