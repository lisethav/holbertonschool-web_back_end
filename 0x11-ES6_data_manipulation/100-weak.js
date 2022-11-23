const weakMap = new WeakMap();
let t = 1;

function queryAPI(endpoint) {
  weakMap.set(endpoint, t);
  t += 1;
  const querys = weakMap.get(endpoint);
  if (querys >= 5) {
    throw new Error('Endpoint load is high');
  }
}

export { queryAPI, weakMap };
