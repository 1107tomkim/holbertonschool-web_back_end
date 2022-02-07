export default function guardrail(mathFunction) {
  // Returns an array named queue

  try {
    return [mathFunction(), 'Guardrail was processed'];
  } catch (e) {
    return [`${e.name}: ${e.message}`, 'Guardrail was processed'];
  }
}
