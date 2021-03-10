export const omit = (object, ...props) => {
  const copy = { ...object }
  for (const prop of props) {
    delete copy[prop]
  }
  return copy
}
