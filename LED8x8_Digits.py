class Digits:
 ZERO = [
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 1, 0, 0, 0, 1, 1, 0,], 
[0, 1, 0, 0, 1, 0, 1, 0,], 
[0, 1, 0, 1, 0, 0, 1, 0,], 
[0, 1, 1, 0, 0, 0, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 ONE = [
[0, 0, 0, 1, 0, 0, 0, 0,], 
[0, 0, 0, 1, 0, 0, 0, 0,], 
[0, 1, 1, 1, 0, 0, 0, 0,], 
[0, 0, 0, 1, 0, 0, 0, 0,], 
[0, 0, 0, 1, 0, 0, 0, 0,], 
[0, 0, 0, 1, 0, 0, 0, 0,], 
[0, 1, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 TWO = [
[0, 1, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 1, 0, 0, 0, 0, 0, 0,], 
[0, 1, 0, 0, 0, 0, 0, 0,], 
[0, 1, 1, 1, 1, 1, 1, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 THREE = [
[0, 1, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 1, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 FOUR = [
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 1, 1, 1, 1, 1, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 FIVE = [
[0, 1, 1, 1, 1, 1, 1, 0,], 
[0, 1, 0, 0, 0, 0, 0, 0,], 
[0, 1, 0, 0, 0, 0, 0, 0,], 
[0, 1, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 1, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 SIX = [
[0, 0, 1, 1, 1, 1, 1, 0,], 
[0, 1, 0, 0, 0, 0, 0, 0,], 
[0, 1, 0, 0, 0, 0, 0, 0,], 
[0, 1, 1, 1, 1, 1, 0, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 SEVEN = [
[0, 1, 1, 1, 1, 1, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 EIGHT = [
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]

 NINE = [
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 1, 0, 0, 0, 0, 1, 0,], 
[0, 0, 1, 1, 1, 1, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 0, 0, 0, 0, 1, 0,], 
[0, 0, 1, 1, 1, 1, 0, 0,], 
[0, 0, 0, 0, 0, 0, 0, 0,], 
  ]
