// Day 145 — 2026-01-02
// https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-02

function nthFibonacci(n) {
  if (n < 0) {
    throw Error("n must be non-negative");
  }
  let a = 0;
  let b = 1;
  let c = 0;
  for (let i = 1; i < n - 1; i++) {
    c = a + b;
    a = b;
    b = c;
  }
  return b;
}

console.log(nthFibonacci(75));
