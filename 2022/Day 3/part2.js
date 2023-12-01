const fs = require('fs');

function getValue(char) {
    // if char > 'a' && char < 'z' { return char - 64 }
    // else { return char - 96 }
    if (char.charCodeAt(0) > 96) return char.charCodeAt(0) - 96;
    else return char.charCodeAt(0) - 38;
}

const data = fs.readFileSync('input.txt').toString().split('\n');

let sum = 0;
let count = 0;
let firstSet = new Set();
let secondSet = new Set();

for (let line of data) {
    count += 1;
    if (count == 1) {
        for (let char of line) {
            firstSet.add(char);
        }
    } else if (count == 2) {
        for (let char of line) {
            secondSet.add(char);
        }
    } else {
        for (let char of line) {
            if (firstSet.has(char) && secondSet.has(char)) {
                sum += getValue(char);
                break;
            }
        }
        count = 0;
        firstSet.clear();
        secondSet.clear();
    }
}

console.log(sum);