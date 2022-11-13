export default function createIteratorObject(report) {
    return Object.values(report.allEmployees).reduce((acc, val) => acc + val, []);
}
