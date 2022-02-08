export default class Airport {
// exporting Airport

  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  get [Symbol.toStringTag]() {
    return `${this.code}`;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value === 'string') {
      this._name = value;
    } else {
      throw new TypeError('Must be a string');
    }
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value === 'string') {
      this._code = value;
    } else {
      throw new TypeError('Must be a string');
    }
  }
}
