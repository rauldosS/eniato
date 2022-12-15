export default class StringNormalizer {
  static normalize (string) {
    // Normalize special characteres. Ex: à -> a, É -> e.
    return string.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase()
  }
}
