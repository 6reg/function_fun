const aba = (str) => {
  let arr = str.split();
  let res = [];
  for (let item in arr) {
    if (item == /[aeiouAEIOU]/) {
      res.push(arr[item] + "b" + arr[item]);
    } else {
      res.push(arr[item])
    } 
  }
    let newArr = res.join()
    return newArr
  }

console.log(aba("Cats and dogs"))
