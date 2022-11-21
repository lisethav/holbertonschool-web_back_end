export default class Building {
    constructor(sqft) {
        if (this.constructor !== Building && typeof this.evacuationWarningMessage === 'undefined') throw new Error('Class extending Building must override evacuationWarningMessage');
        this._sqft = sqft;
    }

    /* captador de pies cuadrados */
    get sqft() {
        return this._sqft;
    }

    /* setter pies cuadrados */
    set sqft(value) {
        this._sqft = value;
    }
}
