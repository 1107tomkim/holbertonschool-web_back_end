export default function hasValuesFromArray(setToCheck, arrayValues) {
  // Return boolean if all elements in array exists within set

  return arrayValues.every((num) => setToCheck.has(num));
}
