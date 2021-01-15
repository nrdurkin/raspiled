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

document.getElementById("fairy-submit").onclick = (e) => {
    let min = document.getElementById("fairy-min").value;
    let max = document.getElementById("fairy-max").value;
    let count = document.getElementById("fairy-count").value;

    let data = JSON.stringify({
        minSpeed: min,
        maxSpeed: max,
        count: parseInt(count)
    });
    next_request = {
        url: "/fairy",
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

function post() {
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

setInterval(post, 50);
