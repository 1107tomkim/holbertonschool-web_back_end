export default function getStudentsByLocation(listStudents, city) {
  // Return array of obj who are located in a specific city

  return listStudents.filter((student) => student.location === city);
}
