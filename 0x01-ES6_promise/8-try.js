export default function divideFunction(numerator, denominator) {
  // func that accepts 2 arg and return num divided by deno

  if (denominator === 0) {
    throw Error('cannot divide by 0');
  } else {
    return (numerator / denominator);
  }
}
