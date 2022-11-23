export default function getStudentsByLocation(listStudents, city) {
    if (!Array.isArray(listStudents)) {
      return [];
    }
    const arrayByLocation = listStudents.filter((item) => item.location === city);
    return arrayByLocation;
  }
