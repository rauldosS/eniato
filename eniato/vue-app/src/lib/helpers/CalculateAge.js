export default class CalculateAge {
  static calculate (birthday) {
    const ageDifMs = new Date() - new Date(birthday).getTime()
    const ageDate = new Date(ageDifMs)
    return Math.abs(ageDate.getUTCFullYear() - 1970)
  }
}
