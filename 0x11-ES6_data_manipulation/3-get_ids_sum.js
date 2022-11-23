export default function getStudentIdsSum(listStudents) {
    if (!Array.isArray(listStudents)) {
      return [];
    }
    const idSum = listStudents.reduce((acc, item) => acc + item.id, 0);
    return idSum;
  }
