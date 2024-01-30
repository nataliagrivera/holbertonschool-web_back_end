function getListStudentIds(students) {
  if (students === null) {
    return [];
  }
  return students.map((student) => student.id);
}
