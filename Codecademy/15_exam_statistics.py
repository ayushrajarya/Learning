#2
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print(grade)
    return 0
print_grades(grades)

#4
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(grades):
    s=0
    for grade in grades:
        s+=grade  
    return s
print(grades_sum(grades))

#5
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(grades):
    s=0
    for grade in grades:
        s+=grade
    return s

def grades_average(grades_input):
    s=grades_sum(grades_input)
    return s/float(len(grades_input))

print(grades_average(grades))

#7
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average=grades_average(scores)
  variance=0
  for curr_score in scores:
    variance+= (average-curr_score)**2
  return variance/float(len(scores))

print(grades_variance(grades))

#8
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average=grades_average(scores)
  variance=0
  for curr_score in scores:
    variance+= (average-curr_score)**2
  return variance/float(len(scores))

def grades_std_deviation(variance):
  return variance**0.5

variance= (grades_variance(grades))
print(grades_std_deviation(variance))

#9
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grade(grades):
  for grade in grades:
    print(grade)
  return 0
print_grade(grades)  

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
print(grades_sum(grades))

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average
print(grades_average(grades))

def grades_variance(scores):
  average=grades_average(scores)
  variance=0
  for curr_score in scores:
    variance+= (average-curr_score)**2
  return variance/float(len(scores))

def grades_std_deviation(variance):
  return variance**0.5

variance= (grades_variance(grades))
print(variance)
print(grades_std_deviation(variance))