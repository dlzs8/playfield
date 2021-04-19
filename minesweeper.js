// In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

// Example

// For

// matrix = [[true, false, false],
//           [false, true, false],
//           [false, false, false]]
// the output should be

// minesweeper(matrix) = [[1, 2, 1],
//                        [2, 1, 1],
//                        [1, 1, 1]]

function minesweeper(matrix) {
    const newMatrix = [];

    matrix.forEach((row, rowIndex) => {
        const newRow = [];

        row.forEach((cell, cellIndex) => {
            const minesAround = Number(Boolean(row[cellIndex - 1])) +
            Number(Boolean(row[cellIndex + 1])) +
            Number(Boolean(matrix[rowIndex - 1]?.[cellIndex - 1])) +
            Number(Boolean(matrix[rowIndex - 1]?.[cellIndex])) +
            Number(Boolean(matrix[rowIndex - 1]?.[cellIndex + 1])) +
            Number(Boolean(matrix[rowIndex + 1]?.[cellIndex - 1])) +
            Number(Boolean(matrix[rowIndex + 1]?.[cellIndex])) +
            Number(Boolean(matrix[rowIndex + 1]?.[cellIndex + 1]));

            newRow.push(minesAround);
        });

        newMatrix.push(newRow);
    });

    return newMatrix;
}

console.log(
    minesweeper([[true, false, false],
    [false, true, false],
    [false, false, false]])
);