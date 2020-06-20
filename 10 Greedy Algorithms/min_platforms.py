def min_platforms(arrival, departure):
  arrival.sort()
  departure.sort()  
  
  max_platforms = 0
  total_platforms = 0
  
  a = 0
  d = 0

  while a < len(arrival) and d < len(departure):    
    if arrival[a] < departure[d]:
      a += 1
      total_platforms += 1
      
      if total_platforms > max_platforms:
        max_platforms = total_platforms      
    else:
      d += 1
      total_platforms -= 1    

  return max_platforms

def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)