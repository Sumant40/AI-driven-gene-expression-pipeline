async function upload(){

const file = document.getElementById("fileInput").files[0];

let formData = new FormData();
formData.append("file", file);

const response = await fetch("http://localhost:8000/upload", {
method: "POST",
body: formData
});

const plot = await response.json();

Plotly.newPlot(
"plot",
JSON.parse(plot).data,
JSON.parse(plot).layout
);

}