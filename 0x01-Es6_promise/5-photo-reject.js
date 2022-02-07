export default function uploadPhoto(filename) {
  // Return Promise rejecting with an error and string

  return Promise.reject(Error(`${filename} cannot be processed`));
}
