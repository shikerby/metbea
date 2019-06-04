const all = (arr, fn = Boolean) => arr.every(fn);
const allEqual = arr => arr.every(val => val === arr[0]);

const any = (arr, fn = Boolean) => arr.some(fn);
