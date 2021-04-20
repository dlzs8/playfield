// Variable name convention checker

function variableName(name) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'
    let newString = '';

    name.split('').forEach(letter => {
        newString += alphabet[alphabet.indexOf(letter) + 1 >= alphabet.length ? 0 : alphabet.indexOf(letter) + 1];
    });

    return newString;
}

console.log(
    variableName(
        'crazy'
    )
)