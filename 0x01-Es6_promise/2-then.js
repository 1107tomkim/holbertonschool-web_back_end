export default function handleResponseFromAPI(promise) {
  // Append three handlers to the func

  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
