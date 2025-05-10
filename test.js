// https://dummyjson.com/posts/


fetch('https://dummyjson.com/posts/')
  .then(res => res.json())
  .then(console.log(res.data))
  .catch(error => console.log(error))

