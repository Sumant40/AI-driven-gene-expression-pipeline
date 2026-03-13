async function runAnalysis(){

const loading = document.getElementById("loading")
const fileInput = document.getElementById("fileInput")
const aiBox = document.getElementById("aiOutput")

if(fileInput.files.length === 0){
alert("Please upload a dataset first.")
return
}

loading.style.display = "block"
aiBox.innerText = "Running AI analysis..."

const file = fileInput.files[0]

let formData = new FormData()
formData.append("file", file)

try{

const response = await fetch("http://localhost:8000/upload",{
method:"POST",
body:formData
})

if(!response.ok){
throw new Error("Server error: "+response.status)
}

const result = await response.json()

loading.style.display = "none"

/* -------- Volcano Plot -------- */

const plotData = JSON.parse(result.plot)

Plotly.newPlot(
"plot",
plotData.data,
plotData.layout
)

/* -------- Top Genes Table -------- */

displayGenes(result.genes)

/* -------- AI Interpretation -------- */

displayAI(result.ai)

}
catch(error){

loading.style.display = "none"

console.error(error)

aiBox.innerText = "Error running analysis. Check console."

}

}

/* -------- Top Genes -------- */

function displayGenes(genes){

let table=document.querySelector("#geneTable tbody")
table.innerHTML=""

genes.forEach(g=>{

let row=document.createElement("tr")

row.innerHTML=`
<td>${g.gene_id}</td>
<td>${Number(g.logFC).toFixed(3)}</td>
<td>${Number(g["P.Value"]).toExponential(2)}</td>
`

table.appendChild(row)

})

}

/* -------- AI Output -------- */

function displayAI(text){

const aiBox=document.getElementById("aiOutput")

if(!text || text.length === 0){
aiBox.innerText="No AI interpretation returned."
return
}

aiBox.innerText=text

}