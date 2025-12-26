// Day 137 — 2025-12-25
// https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-25

function generateSnowflake(crystals) {
  let sf = [];
  crystals
    .split("\n")
    .forEach((line) => sf.push(line + line.split("").reverse().join("")));
  return sf.join("\n");
}

console.log(generateSnowflake("*   *\n * * \n* * *\n * * \n*   *"));
