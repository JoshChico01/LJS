<script>

  import Sidebar from "../../components/Sidebar.svelte"
  import AgeGroup from "../../components/AgeGroup.svelte"

  import "../../style.css"

  import schema from "../../schema.json"

  let groups = Object.keys(schema)

  let age_group = {
    "title" : "New Born",
    "start_age" : 0,
    "end_age" : 1,
    "death_chance" : 0.05
  }

</script>
<Sidebar active="options"/>

<div class="content">
<h1>Life Journey Simulator</h1>


{#each groups as group}
  <AgeGroup name={group} age_group = {schema[group]} />
{/each}

</div>