<script>

export let xlab
export let ylab

export let data

export let title

</script>




<div>
<div style="margin-bottom:20px">Title</div>
<svg width="300" height="150" style="margin:0">
	<!-- x axis -->
	<line x1="0" x2="300" y1="150" y2="150"></line>
	<g class="x" transform="translate(0,170)">
		<text x="0">0</text>
		<text x="60">2</text>
		<text x="120">4</text>
		<text x="180">6</text>
		<text x="240">8</text>
		<text x="300">10</text>
	</g>
	
	<!-- y axis -->
	<line x1="0" x2="0" y1="0" y2="150"></line>
	<g class="y" transform="translate(-10,0)">
		<text y="150">0</text>
		<text y="100">50</text>
		<text y="50">100</text>
		<text y="0">150</text>
	</g>
	
	<!-- data -->
	<polyline style="stroke: red; stroke-width: 2" points="
		0,150
		30,149
		60,146
		90,141
		120,134
		150,125
		180,114
		210,101
		240,86
		270,69
		300,50
	"></polyline>
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