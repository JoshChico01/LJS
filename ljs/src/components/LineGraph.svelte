<script>

export let data

export let x
export let y

export let xlab
export let ylab

export let title

let x_sorted= data[x].toSorted()
let y_sorted= data[y].toSorted()



let xrange = [x_sorted[0], data[x].toSorted()[data[x].length -1]]
let yrange = [y_sorted[0], data[y].toSorted()[data[y].length -1]]



let y_factor = (yrange[1] - yrange[0]) / 250
let x_factor = (xrange[1] - xrange[0]) / 250


let text=""
for (let i = 0; i < data[x].length; i++){
	text += (data[x][i] - xrange[0]) / x_factor + "," + ((yrange[1] -yrange[0])  - (data[y][i] - yrange[0])) / y_factor + "\n"
}

let x_max_coords = (xrange[1] - xrange[0]) / x_factor
let y_max_coords = (yrange[1] -yrange[0]) / y_factor

</script>






<div>
<div style="margin-bottom:20px">{title}</div>
<svg width={x_max_coords} height={y_max_coords} style="margin:0">
	<!-- x axis -->
	<line x1={0} x2={x_max_coords} y1={y_max_coords} y2={y_max_coords}></line>
	<g class="x" transform="translate(0,{y_max_coords + 20})">
		<text x={0}>{xrange[0]}</text>
		<text x={x_max_coords}>{xrange[1]}</text>
	</g>
	
	<!-- y axis -->
	<line x1="0" x2="0" y1="0" y2={y_max_coords}></line>
	<g class="y" transform="translate(-10,0)">
		<text y={y_max_coords}>{yrange[0]}</text>
		<text y="0">{(yrange[1])}</text>
	</g>
	
	<!-- data -->
	<polyline style="stroke: red; stroke-width: 2" points={text}></polyline>
</svg>
</div>

<style>
	svg {
		overflow: visible;
		margin: 3em;
	}
	
	line, polyline {
		fill: none;
		stroke: black;
	}
	
	.x text {
		text-anchor: middle;
	}
	
	.y text {
		text-anchor: end;
		dominant-baseline: middle;
	}
</style>