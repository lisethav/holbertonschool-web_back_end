export default function createInt8TypedArray(length, position, value) {
    const typedArray = new Int8Array(length);
    typedArray[position] = value;
    return typedArray;
  }
