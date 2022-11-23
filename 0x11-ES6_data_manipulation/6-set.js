export default function setFromArray(array) {
    if (!Array.isArray(array)) {
      return 0;
    }
    const set = new Set(array);
    return set;
  }
