// Write a function that reverses characters in (possibly nested) parentheses in the input string.

// Input strings will always be well-formed with matching ()s.

// Examples

// For inputString = "(bar)", the output should be
// reverseInParentheses(inputString) = "rab";

// For inputString = "foo(bar)baz(blim)", the output should be
// reverseInParentheses(inputString) = "foorabbazmilb";

// For inputString = "foo(bar(baz))blim", the output should be
// reverseInParentheses(inputString) = "foobazrabblim".

function deepestParentheses(string) {
    const startIndex = string.lastIndexOf('(');
    const stopIndex = string.indexOf(')', startIndex) + 1;

    const subString = string.slice(startIndex, stopIndex);
    return string.replace(subString, subString.replace(/\(|\)/g, '').split('').reverse().join(''));
}

let testingString = 'foo(bar)baz(blim)';

while (testingString.indexOf('(') > -1) {
    testingString = deepestParentheses(testingString);
}

console.log(testingString);
