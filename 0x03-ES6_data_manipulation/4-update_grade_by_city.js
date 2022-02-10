export default function updateStudentGradeByCity(studentList, city, newGrades) {
  // Returns an array of students for a specific city w their new grade

  return studentList
    .filter((student) => student.location === city)
    .map((student) => {
      let addGrade = 'N/A';
      newGrades.forEach((grade) => {
        if (grade.studentId === student.id) {
          addGrade = grade.grade;
        }
      });
      return { ...student, grade: addGrade };
    });
}
