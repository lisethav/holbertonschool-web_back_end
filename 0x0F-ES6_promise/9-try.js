export default function guardrail(mathFunction) {
  const q = [];
  try {
    q.push(mathFunction());
  } catch (err) {
    q.push(err.toString());
  }
  q.push('Guardrail was processed');
  return q;
}
