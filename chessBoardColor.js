// Given two cells on the standard chess board, determine whether they have the same color or not.

function chessBoardCellColor(cell1, cell2) {
    const colorsMap = {
        even: {
            light: [
                'A', 'C', 'E', 'G'
            ],
            dark: [
                'B', 'D', 'F', 'H'
            ]
        },
        odd: {
            light: [
                'B', 'D', 'F', 'H'
            ],
            dark: [
                'A', 'C', 'E', 'G'
            ]
        }
    };

    const [letter1, number1] = cell1.split('');
    const [letter2, number2] = cell2.split('');

    let object1, object2;

    if (Number(number1) % 2 === 0) {
        object1 = colorsMap.even;
    } else object1 = colorsMap.odd;

    if (Number(number2) % 2 === 0) {
        object2 = colorsMap.even;
    } else object2 = colorsMap.odd;

    if (object1.dark.includes(letter1)) {
        if (object2.dark.includes(letter2)) {
            return true;
        } else return false;
    }

    if (object1.light.includes(letter1)) {
        if (object2.light.includes(letter2)) {
            return true;
        } else return false;
    }
}
