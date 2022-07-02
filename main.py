alt = 0
distance = 0
score = 0
slope = 0
warning_zone = 0
sites = []
scores = []

def score_calculation(alt, distance, slope, warning_zone):
  if warning_zone == 2:
    return 10000
  else:
    score = alt + distance + slope + warning_zone

  return score

while True:
  alt = int(input("Altitude: "))
  distance = int(input("Distance: "))
  slope = int(input("Slope: "))
  zone = int(input("Zone: "))
  score = score_calculation(alt, distance, slope, zone)
  print(score)
  scores.append(score)
  print(sorted(scores))
  
