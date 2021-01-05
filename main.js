console.log("HELLO WORLD");

document.getElementById("color-select").oninput = (e)=>{
    let data = JSON.stringify({color:e.target.value});
    fetch("/color",{
        method:"POST",
        body:data
    }).then(res=>{
        if(res.status === 200);
        else console.log(res);
    }).catch(err=>{
        console.log(err);
    })
};