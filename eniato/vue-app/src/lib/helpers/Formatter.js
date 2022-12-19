export default class Formatter {
  static currency (num) {
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(num)
  }
}
