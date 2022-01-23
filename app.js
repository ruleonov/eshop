let stuff = "Hello!!!";
let html;

html = `
    <ul>
        <h1>JS sandbox</h1>    
        <li> ${stuff}</li>
    </ul>
`

document.body.innerHTML = html;

