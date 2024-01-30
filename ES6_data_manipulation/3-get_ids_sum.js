export default function getStudentIdsSum(students) {
  const sumofIds = students.reduce ((total, student) => total + student.id, 0);
  return sumofIds;
}