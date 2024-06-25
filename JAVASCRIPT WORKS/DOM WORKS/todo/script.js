fetch("https://jsonplaceholder.typicode.com/todos").then(res=>res.json()).then(data=>displayTodos(data))

function displayTodos(todos){
    
    let htmlData=``

    for(let t of todos){

        htmlData+=`
        <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">${t.userId}</h5>
          <h6 class="card-subtitle mb-2 text-body-secondary">${t.title}</h6>
          <p class="card-text">${t.completed}</p>
          <a href="#" class="card-link">Card link</a>
          <a href="#" class="card-link">Another link</a>
        </div>
      </div>`
    }
    document.querySelector("#root").innerHTML=htmlData

}