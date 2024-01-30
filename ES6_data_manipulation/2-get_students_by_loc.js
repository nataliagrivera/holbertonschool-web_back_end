// 0-get_students.js

export default function getStudentsByLocation(students, targetLocation) {
  return students.filter(student => student.location === targetLocation);
}
