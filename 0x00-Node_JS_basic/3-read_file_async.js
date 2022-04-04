const fs = require('fs').promises;

const countStudents = async (path) => {
  let content;
  try {
    content = await fs.readFile(path);
  } catch (error) {
    throw Error('Cannot load the database');
  }
  let lines = content.toString().split('\n');
  lines = lines.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  const field = lines.map((line) => line.split(',')[3]);
  const eachField = [...new Set(field)];

  const dict = {};
  for (let x = 0; x < eachField.length; x += 1) {
    const numStudents = field.filter((field) => field === eachField[x]).length;
    const studentsPerField = lines.filter((line) => line.split(',')[3] === eachField[x]);
    const names = studentsPerField.map((student) => student.split(',')[0]);
    console.log(`Number of students in ${eachField[x]}: ${numStudents}. List: ${names.join(', ')}`);
    dict[eachField[x]] = {
      numStudents,
      names,
    };
  }
  return dict;
};

module.exports = countStudents;
