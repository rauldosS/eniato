import Axios from 'axios'

export default class Paginator {
  constructor ({ count, next, results, requester, page, factory }) {
    this.requester = requester || Axios
    this._factory = factory
    this._count = count
    this._nextUrl = next
    this._page = page || 1
    this._results = this.buildResult(results, factory)
  }

  get results () { return this._results }
  get count () { return this._count }
  get currentPage () { return this._page }
  get hasNext () { return !!this._nextUrl }

  buildResult (results, factory) {
    factory = factory || this._factory
    if (this._factory) {
      return factory(results)
    }
    return results
  }

  next () {
    return this.requester.get(this._nextUrl).then(({ data }) => {
      this._nextUrl = data.next
      this._count = data.count
      this._results = this.buildResult(data.results)
      this._page += 1
      return this.results
    })
  }
}
