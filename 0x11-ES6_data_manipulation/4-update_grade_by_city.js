export default function updateStudentGradeByCity(listStudents, city, newGrades) {
    if (!Array.isArray(listStudents)) {
      return [];
    }
    return listStudents
      .filter((item) => item.location === city)
      .map((item) => {
        let data;
        newGrades.forEach((grade) => {
          if (grade.studentId === item.id) {
            data = { ...item, grade: grade.grade };
          }
        });
        if (!data) {
          return { ...item, grade: 'N/A' };
        }
        return data;
      });
  }
