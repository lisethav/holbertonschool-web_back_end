export default function appendToEachArrayValue(array, appendString) {
    const ar = [];
    for (const value of array) {
        ar.push(appendString + value);
    }

    return ar;
}
