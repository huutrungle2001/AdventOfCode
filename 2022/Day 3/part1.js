// import fs module to read file
const fs = require('fs');

function findCommonChars(str1, str2) {
    // Create a set of characters from str1
    const set1 = new Set(str1.split(''));
    // If a character from str2 is in set1, return it
    for (let char of str2) {
        if (set1.has(char)) return getValue(char);
    }
}

function getValue(char) {
    // if char > 'a' && char < 'z' { return char - 64 }
    // else { return char - 96 }
    if (char.charCodeAt(0) > 96) return char.charCodeAt(0) - 96;
    else return char.charCodeAt(0) - 38;
}

// open file "input.txt" and split it into an array of lines
const input = fs.readFileSync('input.txt').toString().split('\n');

// for each line, find the common characters between its first and second halves, and add them to the sum
let sum = 0;
for (let line of input) {
    left = line.substring(0, line.length / 2);
    right = line.substring(line.length / 2);
    sum += findCommonChars(left, right);
}

// print the sum
console.log(sum);