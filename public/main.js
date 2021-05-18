let next_request = null;

let colorPicker = new iro.ColorPicker("#picker");
colorPicker.on("color:change", function (color) {
    // log the current color as a HEX string
    let data = JSON.stringify({ color: color.hexString });
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
});

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

document.getElementById("ripple").onclick = (e) => {
    next_request = {
        url: "/ripple",
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
setInterval(post, 50);

document.getElementById("stripe-add").onclick = function () {
    let el = document.createElement("div");
    el.innerHTML = `<div class="stripe-color">
    <div><div class="stripe-delete">x</div></div>
    <input type="color" value="#0000ff" class = "stripe-color-input">
    <input class="stripe-width" type="number" value="2">
</div>`;
    el = el.firstChild;
    el.getElementsByClassName("stripe-delete")[0].onclick = function () {
        el.remove();
    };
    document.getElementById("stripe").insertBefore(el, this);
};

document.getElementById("stripe-post").onclick = function () {
    let data = {
        colors: [],
        interval: 0
    };
    for (let el of document.getElementsByClassName("stripe-color")) {
        const color = el.getElementsByClassName("stripe-color-input")[0].value;
        const width = el.getElementsByClassName("stripe-width")[0].value;
        data.colors.push({ color: color, width: width });
    }
    data.interval = document.getElementById("stripe-interval").value;

    let post_data = JSON.stringify(data);
    next_request = {
        url: "/stripe",
        data: {
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            method: "POST",
            body: post_data
        }
    };
};
