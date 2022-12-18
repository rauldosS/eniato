export default class Mask {
  static money (string) {
    const formatter = new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    })

    return formatter.format(string)
  }
}
