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