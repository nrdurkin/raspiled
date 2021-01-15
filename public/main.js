let next_request = null;
document.getElementById("color-select").oninput = (e) => {
    let data = JSON.stringify({ color: e.target.value });

    next_request = {
        url: "/color",
        data: {
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            method: "POST",
            body: data
        }
    };
};

document.getElementById("fade").onclick = (e) => {
    next_request = {
        url: "/fade",
        data: {
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            method: "POST"
        }
    };
};

function test() {
    if (next_request) {
        let request = JSON.parse(JSON.stringify(next_request));
        next_request = null;

        fetch(request.url, request.data)
            .then((res) => {
                if (res.status === 200);
                else console.log(res);
            })
            .catch((err) => {
                console.log(err);
            });
    }
}

var colorPicker = new iro.ColorPicker("#picker");

setInterval(test, 50);
