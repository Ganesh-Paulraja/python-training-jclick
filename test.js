// https://dummyjson.com/posts/

data = {
    "id": 1,
    "title": "His mother had always taught him",
    "body": "His mother had always taught him not to ever think of himself as better than others. He'd tried to live by this motto. He never looked down on those who were less fortunate or who had less money than him. But the stupidity of the group of people he was talking to made him change his mind.",
    "tags": [
        "history",
        "american",
        "crime"
    ],
    "reactions": {
        "likes": 192,
        "dislikes": 25
    },
    "views": 305,
    "userId": 121
}


// fetch('https://dummyjson.com/posts/')
//   .then(res => res.json())
//   .then(data => console.log(data))
//   .catch(error => console.log(error))

fetch('https://dummyjson.com/posts/add', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
.then(res => res.json())
.then(data => console.log(data))
.catch(error => console.log(error))