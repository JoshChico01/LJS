<script>

    import Sidebar from "../../components/Sidebar.svelte"

    import LineGraph from "../../components/LineGraph.svelte"
    import Slider from "../../components/Slider.svelte";
    import BarGraph from "../../components/BarGraphV2.svelte";

    import data from "../../data/data.json"


    let year_selected = 2000



    $: ages = data["Ages"][year_selected - 2000]

    $: console.log(ages)

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


<h2>Population Age Distribution Overtime</h2>
<div style="width:1000px">
<Slider on:change={(e) => year_selected = e.detail.value} min={2000} max={2249} id="slider-for-barplot"/>
</div>


<h3>Year: {year_selected}</h3>
<BarGraph bind:ages={ages}/>





</div>
