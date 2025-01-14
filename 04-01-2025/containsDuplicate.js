const arr = [1, 2, 3, 5, 8];

function containsDuplicate(nums) {
  const set = new Set(nums);

  return set.size !== nums.length;
}

console.log(containsDuplicate(arr));

/*

in js to find length of a set we use .size

*/ 
