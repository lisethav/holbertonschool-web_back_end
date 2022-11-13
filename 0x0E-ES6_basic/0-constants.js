export function taskFirst() {
    const t = 'I prefer const when I can.';
    return t;
}

export function getLast() {
    return ' is okay';
}

export function taskNext() {
    let com = 'But sometimes let';
    com += getLast();

    return com;
}
