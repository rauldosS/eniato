import Axios from 'axios'

export default class Interceptor {
  static enable = () => {
    this.loginInterceptor = Axios.interceptors.response.use(undefined, function (error) {
      if (error.response.status === 403) {
        location.reload()
      }
      return Promise.reject(error)
    })
  }

  static disable = () => {
    if (this.loginInterceptor) {
      Axios.interceptors.request.eject(this.loginInterceptor)
    }
  }
}
