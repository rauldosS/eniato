import Axios from 'axios'

export default class ExternalDownload {
  static download (url, fileName) {
    Axios.get(url, { responseType: 'blob' })
      .then(response => {
        const blob = new Blob([response.data])
        const link = document.createElement('a')
        link.href = URL.createObjectURL(blob)
        link.download = fileName
        link.click()
        URL.revokeObjectURL(link.href)
      }).catch(console.error)
  }
}
