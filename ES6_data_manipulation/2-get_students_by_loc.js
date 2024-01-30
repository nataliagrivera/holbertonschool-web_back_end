// 0-get_students.js

export default function getStudentsByLocation(students) {
  return students.filter(student => student.location === 'San Francisco');
}
