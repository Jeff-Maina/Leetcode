function findDisappearedNums(nums) {
  const num_set = new Set(nums);
  let len = nums.length;
  let result = [];

  for (i = 1; i < len + 1; i++) {
    if (!num_set.has(i)) {
      result.push(i);
    }
  }

  return result;
}

console.log(findDisappearedNums([4, 3, 2, 7, 8, 2, 3, 1]));
