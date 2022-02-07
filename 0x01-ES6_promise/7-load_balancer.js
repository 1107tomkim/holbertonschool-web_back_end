export default function loadBalancer(chinaDownload, USDownload) {
  // Returns val returned by the promised thats resolved first

  return Promise.race([chinaDownload, USDownload]);
}
