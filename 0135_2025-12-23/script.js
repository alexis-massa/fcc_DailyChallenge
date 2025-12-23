// Day 135 — 2025-12-23
// https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-23

function countEmailMarkers(subject) {
  const matches = subject.match(/\b(fw:|fwd:|re:)/gi);
  return matches ? matches.length : 0;
}
