import Building from './5-building';
// Importing previous task 5

export default class SkyHighBuilding extends Building {
  // an implemented class

  constructor(sqft, floors) {
    super().sqft = sqft;
    this.floors = floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }

  get floors() {
    return this._floors;
  }

  set floors(value) {
    if (typeof value === 'number') {
      this._floors = value;
    } else {
      throw new TypeError('Floors must be a number');
    }
  }
}
