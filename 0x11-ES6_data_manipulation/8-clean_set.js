export default function cleanSet(set, startString) {
    const arrayToStr = [];
    if (startString) {
      for (const value of set) {
        if (value.startsWith(startString)) {
          arrayToStr.push(value.slice(startString.length));
        }
      }
    }
    return arrayToStr.join('-');
  }
