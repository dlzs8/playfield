function evenOnly(n) {
    return !String(n).match(/[13579]/);
}

function evenDigitsOnly(n) {
    const stringified = String(n).split('');

    for (let num of stringified) {
        if (num % 2 !== 0) return false;
    }
    return true;
}


console.log(
    evenOnly(44144)
);