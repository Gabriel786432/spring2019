computational_expression = ["html", [ ["head",[ ["title", "Learning the Buddha Way"] ]], ["body", [ ["h1", "The Four Noble Truths"], ["ul", [ ["li", "What's suffering?"], ["li", "The cause of suffering"], ["li", "The end of suffering"], ["li", "A path to the end of suffering"] ]] ]] ]]

total = []
count = 0
def eval_expression(expression):
    global count
    if type(expression) == list:
        count += 1
        length = len(expression)
        no_lists = True
        for i in expression:
            if type(i) is list:
                no_lists = False
            eval_expression(i)
        if no_lists:
            count -= 3
    else:
        total.append(" "*count+expression)

eval_expression(computational_expression)
for i in total:
    print(i)
