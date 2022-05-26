function isCharacterMatch(string1, string2) {
  return (string1.toLowerCase().split('').sort().join('') === string2.toLowerCase().split('').sort().join(''));
};

console.log(isCharacterMatch('charm', 'mArch'));
console.log(isCharacterMatch('abcde2', 'c2abed'));
