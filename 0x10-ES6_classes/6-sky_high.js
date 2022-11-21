import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  /* captador de pies cuadrados */
  get sqft() {
    return this._sqft;
  }

  /* setter pies cuadrados */
  set sqft(value) {
    this._sqft = value;
  }

  /* captador de pisos */
  get floors() {
    return this._floors;
  }

  /* setter pisos */
  set floors(value) {
    this._floors = value;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
