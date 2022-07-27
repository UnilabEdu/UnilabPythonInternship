// PROBLEM 1: SLEEPING IN
function sleepIn(weekday, vacation) {
    if (!weekday || vacation) {return true} else {return false}
}
sleepIn(true, false)


// PROBLEM 2: MONKEY TROUBLE
function monkeyTrouble(aSmile, bSmile) {
    if (aSmile === bSmile) {return true} else {return false}
}
monkeyTrouble(true, true)

// PROBLEM 3: STRING TIMES
function stringTimes(str, n) {
    console.log(str.repeat(n));
}
stringTimes("Hi", 2)

// PROBLEM 4: LUCKY SUM
function luckySum(a, b, c){
    if (a !== 13 && b !== 13 && c !== 13) {return a+b+c}
    else if (a === 13) {return 0}
    else if (b === 13) {return a}
    else if (c === 13) {return a+b}
}
luckySum(1, 13, 3)
// PROBLEM 5:
function caught_speeding(speed, is_birthday){
    let a = 60
    let b = 80
  if (is_birthday === true) {a += 5; b += 5}
  if (speed <= a) {
          return 0
      } else if (a < speed <= b) {
          return 1
      } else if (speed > b) {
          return 2
      }
}
caught_speeding(65, true)

// BONUS: MAKE BRICKS
function makeBricks(small, big, goal){
  let max_length = small*1 + big*5
  if (max_length < goal) {return false}
  if (goal % 5 > small) {return false}
  return true
}
makeBricks(3, 1, 8)
makeBricks(3, 1, 9)
makeBricks(3, 2, 10)