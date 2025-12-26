// Day 138 — 2025-12-26
// https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-26

function sumDivisors(n) {
    let sum = 0;
    for (let i = 1; i < n + 1; i++) {
        if (n % i == 0) sum += i;
    }
    return sum;
}

console.log(sumDivisors(9348));
