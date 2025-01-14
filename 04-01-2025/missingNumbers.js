const arr = [3, 0, 1];

function findMissingNumber(nums) {
  return nums.sort().filter((number, i) => number !== i) - 1;
}


// math formular to get sum of numbers in a range => (startNum + endNum) * numCount / 2

function findMissingNumber2(nums) {
  let len = nums.length;
  let result = (1 + len) * (len / 2);

  return result - nums.reduce((a, b) => a + b);
}

console.log(findMissingNumber2(arr));
