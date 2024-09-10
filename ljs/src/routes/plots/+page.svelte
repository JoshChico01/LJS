<script>

import Sidebar from "../../components/Sidebar.svelte"

import LineGraph from "../../components/LineGraph.svelte"
import Slider from "../../components/Slider.svelte";
//import BarGraph from "../../components/BarGraph.svelte";

import data from "../../data/data.json"


let year_selected = 2000

</script>


<style>
    .hr {
        width: 80%;
        height: 1px;
        background-color: black;
        margin: 40px;
    }

</style>

<Sidebar active="plots"/>


<div style= "margin-left:200px">
<LineGraph data={data} x="Year" y="People_Count" title="Population Simulation" ylab="People Count" xlab="Year"/>

<div class="hr"/>

<div style="width:80%">
<Slider on:change={(e) => year_selected = e.detail.value} min={2000} max={2499} id="slider-for-barplot"/>
</div>


<h1>{year_selected}</h1>
<!--<BarGraph />-->



</div>
