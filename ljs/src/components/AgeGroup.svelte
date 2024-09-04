<script>

  import "../style.css"
  import Passport from "../svg/Passport.svelte"
  import Hospital from "../svg/Hospital.svelte"
  import Baby from "../svg/Baby.svelte"
  import Address from "../svg/Address_Change.svelte"
  import Marriage from "../svg/Marriage.svelte"
  import Divorce from "../svg/Divorce.svelte"
  import ExitCountry from "../svg/ExitCountry.svelte"
  import EnterCountry from "../svg/EnterCountry.svelte"
  import Name from "../svg/NameChange.svelte"

  export let name
  export let age_group


</script>

<style>
.panel {
  width:400px;
  height:200px;
  background : var(--lightGrey);
  border-radius : 10px;
  margin: 10px
}

.title {
  font-size: 20px;
  margin-left:20px;
  padding-top:10px;
  font-weight:600;
}

.line {
  display: flex;
  flex-wrap: wrap;
  margin-left: 20px;
}

.age_input {
  width:25px;
  font-size:15px;
  text-align: center;
  line-height:16px;
}

.death_prob {
  width:40px;
  font-size:15px;
  text-align: center;
  line-height:16px
}

.hr {
  margin-left : 20px;
  margin-right : 20px;
  margin-bottom:10px;
  margin-top:5px;
  width:360px;
  height:1px;
  background-color:black;
}

.prob {
  width : 30px;
  font-size:12px;
}

.event {
  margin-right:5px;
}

</style>


<div class="panel">
  <div class="title">{name}</div>
  <div class="hr" />

  <div class="line">
    <div style="font-size:18px; margin-right:6px">Age: </div><input class="age_input" bind:value={age_group["start_age"]}/>-<input class="age_input" bind:value={age_group["end_age"]}/>
  </div>

  <div class="hr"/>

  <div class="line">
    <div style="font-size:18px; margin-right:6px">Death chance: </div><input class="death_prob" bind:value={age_group["death"]}/>
  </div>

  <div class="line" style="height:100px">
    <div class="event"> <Passport /><input class="prob"     bind:value={age_group["events"]["passport"]}/></div>
    <div class="event"> <Hospital /><input class="prob"     bind:value={age_group["events"]["hospital"]}/></div>
    <div class="event"> <Baby /><input class="prob"         bind:value={age_group["events"]["baby"]}/></div>
    <div class="event"> <Address /><input class="prob"      bind:value={age_group["events"]["address change"]}/></div>
    <div class="event"> <Marriage /><input class="prob"     bind:value={age_group["events"]["marriage"]}/></div>
    <div class="event"> <Divorce /><input class="prob"      bind:value={age_group["events"]["devorce"]}/></div>
    <div class="event"> <ExitCountry /><input class="prob"  bind:value={age_group["events"]["exit country"]}/></div>
    <!--<div class="event"> <EnterCountry /><input class="prob" bind:value={age_group["events"]["passport"]}/></div>-->
    <div class="event"> <Name /><input class="prob"         bind:value={age_group["events"]["name change"]}/></div>





    

  </div>

</div>