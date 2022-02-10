export default function getStudentIdsSum(studentList) {
  // Return sum of all the students ids

  return Object.values(studentList).reduce((total, { id }) => total + id, 0);
}
