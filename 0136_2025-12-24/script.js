// Day 136 — 2025-12-24
// https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-24

function parseImage(markdown) {
    const [, alt, src] = markdown.match(/!\[(.*?)\]\((.*?)\)/);
    return `<img src="${src}" alt="${alt}">`;
}

console.log(parseImage("![Cute cat](cat.png)"))