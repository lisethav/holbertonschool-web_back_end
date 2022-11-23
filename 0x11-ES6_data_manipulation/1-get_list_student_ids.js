export default function getListStudentIds(listStudents) {
    if (!Array.isArray(listStudents)) {
      return [];
    }
    const arrIds = listStudents.map((item) => item.id);
    return arrIds;
  }
