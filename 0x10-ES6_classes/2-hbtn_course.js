export default class HolbertonCourse {
    constructor(name, length, students) {
        if (typeof name !== 'string') throw TypeError('Name must be a string');
        if (typeof length !== 'number') throw TypeError('Length must be a number');
        if (!Array.isArray(students)) throw TypeError('Stundents must be an array of Strings');
        if (students.every((student) => typeof student !== 'string')) throw TypeError('Stundents must be an array of Strings');

        this._name = name;
        this._length = length;
        this._students = students;
    }

    /* nombre del captador */
    get name() {
        return this._name;
    }

    /*nombre del colocador*/
    set name(value) {
        if (typeof value !== 'string') throw TypeError('Name must be a string');
        this._name = value;
    }

    /* longitud del captador */
    get length() {
        return this._length;
    }

    /* longitud del setter */
    set length(value) {
        if (typeof value !== 'number') throw TypeError('Length must be a number');
        this._length = value;
    }

    /* estudiantes captadores */
    get students() {
        return this._students;
    }

    /* estudiantes setter */
    set students(value) {
        if (!Array.isArray(value)) throw TypeError('Stundents must be an array of Strings');
        if (value.every((student) => typeof student !== 'string')) throw TypeError('Stundents must be an array of Strings');
        this._students = value;
    }
}