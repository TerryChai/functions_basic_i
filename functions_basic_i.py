#1
# def number_of_food_groups():
#    return 5
# print(number_of_food_groups())
#Question 1 comment: I predict the functin will return 5 because number_of_food_groups"()" parentheses is Literal[5]
#Prediction: Right[x] or Wrong[]?

#2
# def number_of_military_branches():
#    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Question 2 comment: I predict the function will return an error because "number_of_days_in_a_week_silicon_or_triangle_sides()" is undefined.
#Prediction: Right[x] or Wrong[]?

#3
# def number_of_books_on_hold():
#    return 5
#    return 10
# print(number_of_books_on_hold())
#Question 3 comment: I predict the function will return five because the "()" in the funtion's name is Literal to 5. Which means it will not be able to return twice since "return 10" is unreachable.
#Prediction: Right[x] or Wrong[]?

#4
# def number_of_fingers():
#    return 5
#    print(10)
# print(number_of_fingers()) 
#Question 4 comment: I predict that the function "number_of_fingers()" is going to return 5 because "print(10)" is unreachable. "print(number_of_fingers())" is reachable because it's calling the function."
#Prediction: Right[x] or Wrong[]?

#5
# def number_of_great_lakes():
#    print(5)
# x = number_of_great_lakes()
# print(x)
#Question 5 comment: I predict the function will print 5 first then x = number_of_great_lakes() second since it's the next line after print(5).
#Prediction: Right[] or Wrong[x]?

#6
# def add(b,c):
#    print(b+c)
# print(add(1,2) + add(2,3))
#Question 6 comment: I predict the function will print "b+c" since it's taking the function's parameters.\
# the function did not go through because of print(add(1,2) + add(2,3)). Since "add" isn't the same as the function name it would not work.
#Prediction: Right[] or Wrong[x]?

#7
# def concatenate(b,c):
#    return str(b)+str(c)
# print(concatenate(2,5))
#Question 7 comment: the function will return 25 because of str() is taking from b and c's class.
#Prediction: Right[x] or Wrong[]?

#8
# def number_of_oceans_or_fingers_or_continents():
#    b = 100
#    print(b)
#    if b < 10:
#        return 5
#    else:
#        return 10
#    return 7
# print(number_of_oceans_or_fingers_or_continents())
#Question 8 comments: The function will print b first and return 10 2nd because b is set to 100 and is greater than 10. Since b isn't less than 10 it goes to "else:".
#Prediction: Right[x] or Wrong[]?

#9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#    if b<c:
#        return 7
#    else:
#        return 14
#    return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Question 9 comment: I predict the function will return 7,14,21 because in order to run the function's intructions you have to make the parameters have a value in the function. So you would take the numbers in the "print()" statement and plug it into the function's parameters.
#Prediction: Right[x] or Wrong[]?

#10
# def addition(b,c):
#    return b+c
#    return 10
# print(addition(3,5))
#Question 10 comments: This function will return 8 because the numbers in "print(addition(3,5))" replaces the parameters in the function. Return 10 gets excluded because it is unreachable or has nothing to return for.
#Prediction: Right[x] or Wrong[]?

#11
# b = 500
# print(b)
# def foobar():
#    b = 300
#    print(b)
# print(b)
# foobar()
# print(b)
#Question 11 comments: The function will print the value of b and the go through the function twice. it'll then print b's new value 300 twice because of "foobar()" and "print(b)" is wrote multiple times.
#Prediction: Right[x] or Wrong[]?

#12
# b = 500
# print(b)
# def foobar():
#    b = 300
#    print(b)
#    return b
# print(b)
# foobar()
# print(b)
#Question 12 comment: Function will print the value of b first which will give us 500. The def foobar() function then changes the value of b and give it 300. Finally it'll print b and return b = 500.
#Prediction: Right[x] or Wrong[]?

#13
# b = 500
# print(b)
# def foobar():
#    b = 300
#    print(b)
#    return b
# print(b)
# b=foobar()
# print(b)
#Question 13 comment: The function will print the value 500 first then the new value of b(300). it'll return the first value b = 500 and then 500 twice.
# the function returned 500 500 300 500. I believe it came back with 500 twice before instead of after because "return b" only returns the variable/value of b = 300. "print(b)" remains reachable to b = 500.
#Prediction: Right[] or Wrong[x]?



#14
# def foo():
#    print(1)
#    bar()
#    print(2)
# def bar():
#    print(3)
# foo()
#Question 14 comments: Function foo() and bar would not run because there isn't anything calling the function or giving the function a list of instructions. SO it will return 1,2,3 because of print(1), print(2), and print(3).
#Prediction: Right[x] or Wrong[]?

#15
# def foo():
#    print(1)
#    x = bar()
#    print(x)
#    return 10
# def bar():
#    print(3)
#    return 5
# y = foo()
# print(y)
#Question 15 comment: the function would run 1,3,5,10 because it loops and takes other keys.
#Prediction: Right[x] or Wrong[]?