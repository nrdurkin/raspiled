console.log("HELLO WORLD");

document.getElementById("color-select").oninput = (e)=>{
    let data = JSON.stringify({color:e.target.value});
    fetch("/color",{
        headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
        method:"POST",
        body:data
    }).then(res=>{
        if(res.status === 200);
        else console.log(res);
    }).catch(err=>{
        console.log(err);
    })
};

document.getElementById("fade").onclick = (e)=>{
    fetch("/fade",{
        headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
        method:"POST"
    }).then(res=>{
        if(res.status === 200);
        else console.log(res);
    }).catch(err=>{
        console.log(err);
    })
};