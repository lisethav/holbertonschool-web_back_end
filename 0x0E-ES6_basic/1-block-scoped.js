export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;

    if (trueOrFalse) {
        // list
        const task = true;
        // line
        const task2 = false;
    }

    return [task, task2];
}
