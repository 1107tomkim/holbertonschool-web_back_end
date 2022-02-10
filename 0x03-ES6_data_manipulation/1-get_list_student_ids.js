export default function getListStudentIds(arr) {
  // Return an array of ids from a list of obj

  if (arr instanceof Array) {
    return arr.map((student) => student.id);
  }
  return [];
}
