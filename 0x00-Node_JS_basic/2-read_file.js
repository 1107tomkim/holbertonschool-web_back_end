const fs = require('fs');

const countStudents = (path) => {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }
  const content = fs.readFileSync(path);
  let lines = content.toString().split('\n');
  lines = lines.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  const field = lines.map((line) => line.split(',')[3]);
  const eachField = [...new Set(field)];

  for (const fieldName of eachField) {
    const studentsPerField = lines
      .filter((line) => line.endsWith(fieldName))
      .map((line) => {
        const stdnt = line.split(',');
        return stdnt[0];
      });
    console.log(
      `Number of students in ${fieldName}: ${
        studentsPerField.length
      }. List: ${studentsPerField.join(', ')}`,
    );
  }
};

module.exports = countStudents;
