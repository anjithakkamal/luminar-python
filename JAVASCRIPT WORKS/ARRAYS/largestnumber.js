// function sortArray(arr){
//     arr.sort(function compare(first,second) {
//         var firstsecond ='' + first + second;
//         var secondfirst ='' + second + first;
//         return firstsecond>secondfirst ? -1:1;
//     })
// }

// function getLargestNumber(arr){
//     var largestNumber = arr.join('')
//     return largestNumber
// }
// var arr = [13,2,4,7,89]
// sortArray(arr)
// var result = getLargestNumber(arr)
// console.log(result)

nums.sort((a, b) => `${b}${a} - ${a}${b}`)
return nums[0] === 0 ? ''+nums[0] : nums.join('');